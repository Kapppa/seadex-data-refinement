from __future__ import annotations

from collections import defaultdict
from functools import cached_property

from prettytable import PrettyTable, TableStyle
from pydantic import BaseModel, ByteSize
from seadex import SeaDexEntry, TorrentRecord, Tracker


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
                # For entries that have both AB and Nyaa entries, only consider the former.
                # This is done to avoid useless nyaa batches skewing the results.
                filtered = [t for t in entry.torrents if t.tracker is Tracker.ANIMEBYTES] or entry.torrents
                torrents.update(filtered)

        return tuple(torrents)

    def sizes_by_group(self) -> tuple[GroupSizeRecord, ...]:
        # Only consider the top 99 groups
        top = 99

        data: dict[str, dict[str, int]] = defaultdict(lambda: {"total_size": 0, "best_size": 0, "total_torrents": 0})

        # Collect the data we want
        for torrent in self.torrents:
            name = torrent.release_group
            total_size = data[name]["total_size"] + sum(f.size for f in torrent.files)
            best_size = data[name]["best_size"] + sum(f.size for f in torrent.files if torrent.is_best)
            total_torrents = data[name]["total_torrents"] + 1

            data[name] = {
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
                "total_size": sum(stats["total_size"] for _, stats in other_entries),
                "best_size": sum(stats["best_size"] for _, stats in other_entries),
                "total_torrents": sum(stats["total_torrents"] for _, stats in other_entries),
            }
            top_entries.append(("Others", others_stats))

        return tuple(GroupSizeRecord(name=name, **stats) for name, stats in top_entries)  # type: ignore[arg-type]

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
        sizes_by_group = self.sizes_by_group()

        assert self.total_size == sum(x.total_size for x in sizes_by_group)
        assert self.best_size == sum(x.best_size for x in sizes_by_group)

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
        markdown_output += "\n## Overview\n\n"
        markdown_output += f"- Total Size: {self.total_size.human_readable(separator=' ')}\n"
        markdown_output += f"- Best Size: {self.best_size.human_readable(separator=' ')}\n"
        markdown_output += f"- Alt Size: {self.alt_size.human_readable(separator=' ')}\n"
        markdown_output += "\n## Breakdown by Group\n\n"
        markdown_output += self._groupsize_to_markdown_table(sizes_by_group)
        return f"{markdown_output}\n"
