from __future__ import annotations

from collections import defaultdict
from functools import cached_property
from typing import Any

from prettytable import PrettyTable, TableStyle
from pydantic import BaseModel, ByteSize
from seadex import SeaDexEntry, TorrentRecord


class GroupSizeRecord(BaseModel):
    name: str
    """Name of the group."""
    total_size: ByteSize
    """Total size of the torrents under this group."""
    best_size: ByteSize
    """Total size of the torrents marked as best under this group."""
    total_torrents: int
    """Total number of torrents under this group."""

    @cached_property
    def best_size_percentage(self) -> float:
        return (self.best_size / self.total_size) * 100

    @cached_property
    def average_torrent_size(self) -> ByteSize:
        return ByteSize(self.total_size / self.total_torrents)


class SeaDexSizeCalculator:
    def __init__(self) -> None:
        self.torrents = self._load_torrents()

    def _load_torrents(self) -> tuple[TorrentRecord, ...]:
        torrents: set[TorrentRecord] = set()

        with SeaDexEntry() as se:
            for entry in se.iterator():
                unique_groups = {t.release_group for t in entry.torrents}
                for group in unique_groups:
                    # For every group in an entry, that has both a PT and Public release,
                    # only consider the PT release. If a group does not have a PT release,
                    # then we fallback to public releases.
                    filtered = [t for t in entry.torrents if t.release_group == group and t.tracker.is_private()] or [
                        t for t in entry.torrents if t.release_group == group
                    ]
                    torrents.update(filtered)

        return tuple(torrents)

    def _sizes_by_group(self) -> tuple[GroupSizeRecord, ...]:
        # Only consider the top 99 groups
        top = 50

        data: dict[str, dict[str, Any]] = defaultdict(lambda: {"total_size": 0, "best_size": 0, "total_torrents": 0})

        # Collect the data we want
        for torrent in self.torrents:
            key = torrent.release_group.casefold().strip()
            name = torrent.release_group.strip()
            total_size = data[key]["total_size"] + sum(f.size for f in torrent.files)
            best_size = data[key]["best_size"] + sum(f.size for f in torrent.files if torrent.is_best)
            total_torrents = data[key]["total_torrents"] + 1

            data[key] = {
                "name": name,
                "total_size": total_size,
                "best_size": best_size,
                "total_torrents": total_torrents,
            }

        # Sort by total size in descending order
        sorted_data = sorted(data.items(), key=lambda x: x[1]["total_size"], reverse=True)

        # Split into top entries and others
        top_entries = sorted_data[:top]
        other_entries = sorted_data[top:]

        # Sum up stats for others
        if other_entries:
            others_stats = {
                "name": "Others",
                "total_size": sum(stats["total_size"] for _, stats in other_entries),
                "best_size": sum(stats["best_size"] for _, stats in other_entries),
                "total_torrents": sum(stats["total_torrents"] for _, stats in other_entries),
            }
            top_entries.append(("Others", others_stats))

        return tuple(GroupSizeRecord(**stats) for key, stats in top_entries)

    @cached_property
    def total_size(self) -> ByteSize:
        sizes: list[ByteSize] = []

        for torrent in self.torrents:
            sizes.extend(file.size for file in torrent.files)

        return ByteSize(sum(sizes))

    @cached_property
    def best_size(self) -> ByteSize:
        sizes: list[ByteSize] = []

        for torrent in self.torrents:
            if torrent.is_best:
                sizes.extend(file.size for file in torrent.files)

        return ByteSize(sum(sizes))

    @cached_property
    def realistic_size(self) -> ByteSize:
        """
        This sort of emulates the scenario where you're grabbing the best release
        for each entry and only falling back to alt releases when there's no best release.
        """
        torrents: set[TorrentRecord] = set()

        with SeaDexEntry() as se:
            for entry in se.iterator():
                filtered = (
                    # 1. Best release with dual audio from private tracker
                    [t for t in entry.torrents if t.is_best and t.is_dual_audio and t.tracker.is_private()]
                    # 2. Best release with dual audio from any tracker
                    or [t for t in entry.torrents if t.is_best and t.is_dual_audio]
                    # 3. Best release from private tracker
                    or [t for t in entry.torrents if t.is_best and t.tracker.is_private()]
                    # 4. Best release from any tracker
                    or [t for t in entry.torrents if t.is_best]
                    # 5. Any available release
                    or entry.torrents
                )

                for torrent in filtered:
                    torrents.add(torrent)
                    break

        sizes: list[int] = []

        for _torrent in torrents:
            sizes.append(sum(f.size for f in _torrent.files))

        return ByteSize(sum(sizes))

    @cached_property
    def alt_size(self) -> ByteSize:
        return ByteSize(self.total_size - self.best_size)

    @staticmethod
    def _groupsize_to_markdown_table(data: tuple[GroupSizeRecord, ...]) -> str:
        """Converts the MediaEntryCollection to a Markdown table string."""
        table = PrettyTable()
        table.set_style(TableStyle.MARKDOWN)
        table.align = "l"
        table.field_names = ["Rank", "Group", "Total Size", "Best Size", "Total Torrents"]
        for rank, entry in enumerate(data, start=1):
            table.add_row(
                [
                    rank,
                    entry.name,
                    entry.total_size.human_readable(separator=" "),
                    f"{entry.best_size.human_readable(separator=' ')} ({entry.best_size_percentage:.2f}%)",
                    f"{entry.total_torrents} (~{entry.average_torrent_size.human_readable(separator=' ')} each)",
                ],
            )

        return table.get_formatted_string()

    def generate_markdown_report(self) -> str:
        sizes_by_group = self._sizes_by_group()

        # assert self.total_size == sum(x.total_size for x in sizes_by_group)
        # assert self.best_size == sum(x.best_size for x in sizes_by_group)

        markdown_output = "# Size Statistics\n\n"
        markdown_output += (
            "These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.\n\n"
            'The definition of an entry (or a "complete" torrent) is quite murky. '
            "SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. "
            "Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. "
            "A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.\n\n"
            "All of this and more means that we need to settle on a method to calculate these statistics. "
            "This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent, only the former is considered; otherwise, all torrents are considered. "
            "Exact duplicates are also discarded."
        )
        markdown_output += "\n\n## Overview\n\n"
        markdown_output += f"- Total size: `{self.total_size.human_readable(separator=' ')}`\n"
        markdown_output += f"- Best size: `{self.best_size.human_readable(separator=' ')}`\n"
        markdown_output += f"- Alt size: `{self.alt_size.human_readable(separator=' ')}`\n"
        markdown_output += f"- Realistic size: `{self.realistic_size.human_readable(separator=' ')}`\n\n"
        markdown_output += (
            "The realistic size stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, "
            "fallback to the best single audio release if that's not present, "
            "and again fallback to whatever there is if neither exist."
        )
        markdown_output += "\n\n## Breakdown by Group\n\n"
        markdown_output += self._groupsize_to_markdown_table(sizes_by_group)
        return f"{markdown_output}\n"
