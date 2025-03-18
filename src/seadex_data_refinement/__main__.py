from __future__ import annotations

from pathlib import Path
from typing import Literal

import seadex
from cyclopts import App, Group

from .core import MediaEntryCollection
from .leaderboard import SeaDexLeaderboard
from .size import SeaDexSizeCalculator

app = App("SeaDex Data Refinement", help_format="markdown")

# Hide default help/version flags
hidden = Group(show=False)
app["--help"].group = hidden
app["--version"].group = hidden


@app.command
def get_entries(
    criteria: Literal[
        "unmuxed",
        "no-comparisons",
        "marked-incomplete",
        "public-non-nyaa",
        "private-tracker-only",
        "public-tracker-only",
        "best-no-dual",
    ],
    /,
    *,
    limit: int | None = None,
    outfile: Path | None = None,
    json: bool = False,
) -> None:
    """
    Retrieve SeaDex entries based on the specified criteria.

    Parameters
    ----------
    criteria : Literal["unmuxed", "no-comparisons", "marked-incomplete", "public-non-nyaa", "private-tracker-only", "public-tracker-only", "best-no-dual"]
        The criteria to use for retrieving SeaDex entries.
        - "unmuxed": Unmuxed entries.
        - "no-comparisons": Entries without any comparisons.
        - "marked-incomplete": Entries explicitly marked as incomplete by editors.
        - "public-non-nyaa": Entries that are publicly available but not distributed on Nyaa.
        - "private-tracker-only": Entries exclusively found on private trackers.
        - "public-tracker-only": Entries exclusively found on public trackers.
        -"best-no-dual": Best entries without a dual audio version.
    limit : int | None, optional
        Maximum number of entries to retrieve.
    outfile : Path | None, optional
        Path to write the output to.
    json : bool, optional
        Whether to output results in JSON format.
    """
    anilist_ids: list[int] = []
    header: str | None = None

    match criteria:
        case "unmuxed":
            header = "# Unmuxed"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    if entry.theoretical_best is not None:
                        anilist_ids.append(entry.anilist_id)

        case "no-comparisons":
            header = "# No comparisons"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    if not any(comp.startswith("https://slow.pics") for comp in entry.comparisons):
                        anilist_ids.append(entry.anilist_id)

        case "marked-incomplete":
            header = "# Marked incomplete"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    if entry.is_incomplete:
                        anilist_ids.append(entry.anilist_id)

        case "public-non-nyaa":
            header = "# Public - non-Nyaa"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    for torrent in entry.torrents:
                        if torrent.tracker.is_public() and torrent.tracker is not seadex.Tracker.NYAA:
                            anilist_ids.append(entry.anilist_id)
                            break

        case "private-tracker-only":
            header = "# Private tracker only"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    for torrent in entry.torrents:
                        if torrent.tracker.is_private():
                            release_group = torrent.release_group.casefold().strip()
                            if not any(
                                t.tracker.is_public()
                                for t in entry.torrents
                                if t.release_group.casefold().strip() == release_group
                            ):
                                anilist_ids.append(entry.anilist_id)
                                break

        case "public-tracker-only":
            header = "# Public tracker only"

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    for torrent in entry.torrents:
                        if torrent.tracker.is_public():
                            release_group = torrent.release_group.casefold().strip()
                            if not any(
                                t.tracker.is_private()
                                for t in entry.torrents
                                if t.release_group.casefold().strip() == release_group
                            ):
                                anilist_ids.append(entry.anilist_id)
                                break

        case "best-no-dual":
            header = "# Best entries without a dual audio version\n\n"
            header += (
                "An entry appears here if its designated 'best' version lacks dual audio, "
                "but at least one alternative release for the same entry "
                "includes a dual audio option.\n\n"
            )

            with seadex.SeaDexEntry() as seadex_entry:
                for entry in seadex_entry.iterator():
                    if any(torrent.is_dual_audio for torrent in entry.torrents if torrent.is_best):
                        # There's already a best dual audio torrent in this entry
                        continue
                    else:  # There's no best dual audio torrent in this entry
                        if any(torrent.is_dual_audio for torrent in entry.torrents if not torrent.is_best):
                            # Check if any alt release has a dual audio torrent
                            # This means there *is* a dub, so we can mark this as
                            # an entry that needs a dual audio mux of the best release.
                            anilist_ids.append(entry.anilist_id)
                            break

        case _:  # Won't ever happen because cyclopts already validates the input.
            raise ValueError(criteria)

    collection = MediaEntryCollection.from_anilist_ids(anilist_ids[:limit])

    if json:
        output = collection.to_json()
    else:
        output = collection.to_markdown_table(header=header)

    if outfile:
        outfile.write_text(output, encoding="utf-8")
    else:
        print(output)


@app.command
def size_stats(outfile: Path | None = None) -> None:
    """
    Generate a markdown report of SeaDex size statistics.

    Parameters
    ----------
    outfile : Path | None, optional
        Path to write the output to.
    """
    output = SeaDexSizeCalculator().generate_markdown_report()

    if outfile:
        outfile.write_text(output, encoding="utf-8")
    else:
        print(output)


@app.command
def leaderboards(outfile: Path | None = None) -> None:
    """
    Generate a markdown leaderboard for SeaDex entries.

    Parameters
    ----------
    outfile : Path | None, optional
        Path to write the output to.
    """
    output = SeaDexLeaderboard().generate_markdown_report()

    if outfile:
        outfile.write_text(output, encoding="utf-8")
    else:
        print(output)


@app.command
def top_200(outfile: Path | None = None) -> None:
    """
    Generate a markdown of top 200 shows not on SeaDex

    Parameters
    ----------
    outfile : Path | None, optional
        Path to write the output to.
    """
    output = MediaEntryCollection.top_200_anilist_not_on_dex()

    if outfile:
        outfile.write_text(output.to_markdown_table(header="# Top 200 missing shows"), encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    app()
