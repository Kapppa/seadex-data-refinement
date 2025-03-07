from __future__ import annotations

from collections import defaultdict

from prettytable import PrettyTable, TableStyle
from seadex import EntryRecord, SeaDexEntry


class SeaDexLeaderboard:
    def __init__(self) -> None:
        self.entries = self._load_entries()

    def _load_entries(self) -> tuple[EntryRecord, ...]:
        with SeaDexEntry() as se:
            return tuple(se.iterator())

    def by_total_count(self) -> dict[str, int]:
        data: dict[str, int] = defaultdict(lambda: 0)

        for entry in self.entries:
            unique_groups = {t.release_group for t in entry.torrents}
            for group in unique_groups:
                data[group] += 1

        return dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:25])

    def by_best_dual_count(self) -> dict[str, int]:
        data: dict[str, int] = defaultdict(lambda: 0)

        for entry in self.entries:
            unique_groups = {t.release_group for t in entry.torrents if t.is_best and t.is_dual_audio}
            for group in unique_groups:
                data[group] += 1

        return dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:25])

    def by_best_count(self) -> dict[str, int]:
        data: dict[str, int] = defaultdict(lambda: 0)

        for entry in self.entries:
            unique_groups = {t.release_group for t in entry.torrents if t.is_best}
            for group in unique_groups:
                data[group] += 1

        return dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:25])

    def by_alt_count(self) -> dict[str, int]:
        data: dict[str, int] = defaultdict(lambda: 0)

        for entry in self.entries:
            unique_groups = {t.release_group for t in entry.torrents if not t.is_best}
            for group in unique_groups:
                data[group] += 1

        return dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:25])

    def generate_markdown_report(self) -> str:
        header = "# Leaderboards\n\n"
        header += (
            "These rankings are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.\n\n"
            'The definition of an entry (or a "complete" torrent) is quite murky. '
            "SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. "
            "Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. "
            "A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.\n\n"
            "All of this and more means that we need to settle on a method for calculating these rankings. "
            "For our purposes, an entry is defined by SeaDex, which in turn follows AniList's definition. "
            "We iterate through every entry in SeaDex and consider a group only once per entry. "
            "As a result, these leaderboards reflect how many AniList entries a group covers rather than the number of torrents they have.\n\n"
            "```{note}\n"
            "This leaderboard is just for fun! Please don't take these rankings too seriously. "
            "We appreciate all the hard work that every release group puts into making releases. ❤️"
            "\n```\n\n"
        )

        report = []

        for title, data in [
            ("Top 25 - Total entries", self.by_total_count()),
            ("Top 25 - Best dual audio entries", self.by_best_dual_count()),
            ("Top 25 - Best entries", self.by_best_count()),
            ("Top 25 - Alt entries", self.by_alt_count()),
        ]:
            table = PrettyTable()
            table.set_style(TableStyle.MARKDOWN)
            table.align = "l"
            table.field_names = ["Rank", "Group", "Count"]

            for rank, (name, count) in enumerate(data.items(), start=1):
                if rank == 1:
                    table.add_row(["🥇", name, count])
                elif rank == 2:
                    table.add_row(["🥈", name, count])
                elif rank == 3:
                    table.add_row(["🥉", name, count])
                else:
                    table.add_row([rank, name, count])

            report.append(f"## {title}\n")
            report.append(table.get_formatted_string())
            report.append("")

        return header + "\n".join(report)
