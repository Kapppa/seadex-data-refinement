from __future__ import annotations

import itertools
import time
from collections.abc import Iterable
from typing import Self

import httpx
from prettytable import PrettyTable, TableStyle
from pydantic import BaseModel, ConfigDict

SEADEX_ANILIST_IDS_URL = "https://releases.moe/api/listIDs"

ANILIST_API_URL = "https://graphql.anilist.co"

ANILIST_QUERY = """\
query Media($idIn: [Int]) {
  Page {
    media(id_in: $idIn) {
      id
      title {
        romaji
        english
      }
      startDate {
        year
      }
      averageScore
      popularity
    }
  }
}
"""

ANILIST_TOP_50_QUERY = """\
query Media($idNotIn: [Int], $page: Int) {
  Page(perPage: 50, page: $page) {
    media(status_not_in:[NOT_YET_RELEASED,CANCELLED],type:ANIME,sort:[POPULARITY_DESC], id_not_in: $idNotIn {
      id
      title {
        romaji
        english
      }
      startDate {
        year
      }
      averageScore
      popularity    
    }
  }
}
"""


class MediaEntry(BaseModel):
    """Represents a single media entry with metadata."""

    model_config = ConfigDict(frozen=True)

    id: int
    title: str
    year: int | None
    score: int | None
    popularity: int | None
    seadex_url: str
    anilist_url: str


class MediaEntryCollection(BaseModel):
    """Represents a collection of media entries."""

    model_config = ConfigDict(frozen=True)

    entries: tuple[MediaEntry, ...]

    @classmethod
    def from_anilist_ids(cls, anilist_ids: Iterable[int]) -> Self:
        """Fetches and creates an MediaEntryCollection from AniList IDs."""
        results = []

        with httpx.Client() as client:
            for batch in itertools.batched(anilist_ids, 50):
                resp = (
                    client.post(
                        ANILIST_API_URL,
                        json={
                            "query": ANILIST_QUERY,
                            "variables": {"idIn": batch},
                        },
                    )
                    .raise_for_status()
                    .json()["data"]["Page"]["media"]
                )

                for media in resp:
                    results.append(
                        MediaEntry(
                            id=media["id"],
                            title=media["title"]["english"] or media["title"]["romaji"],
                            year=media["startDate"]["year"],
                            score=media["averageScore"],
                            popularity=media["popularity"],
                            seadex_url=f"https://releases.moe/{media['id']}/",
                            anilist_url=f"https://anilist.co/anime/{media['id']}",
                        ),
                    )

                time.sleep(1)

        results.sort(
            reverse=True,
            key=lambda x: x.popularity if x.popularity is not None else -1,
        )

        return cls(entries=tuple(results))
    

    @classmethod
    def top_200_anilist_not_on_dex(cls) -> Self:
        """Fetches and creates an MediaEntryCollection of the Top 200 not on SeaDex."""
        results = []

        with httpx.Client() as client:
            ids = client.get(SEADEX_ANILIST_IDS_URL).raise_for_status().text
            for page in range(4):
                resp = (
                    client.post(
                        ANILIST_API_URL,
                        json={
                            "query": ANILIST_QUERY,
                            "variables": {"page": page+1, "idNotIN": ids},
                        },
                    )
                    .raise_for_status()
                    .json()["data"]["Page"]["media"]
                )

                for media in resp:
                    results.append(
                        MediaEntry(
                            id=media["id"],
                            title=media["title"]["english"] or media["title"]["romaji"],
                            year=media["startDate"]["year"],
                            score=media["averageScore"],
                            popularity=media["popularity"],
                            seadex_url=f"https://releases.moe/{media['id']}/",
                            anilist_url=f"https://anilist.co/anime/{media['id']}",
                        ),
                    )

                time.sleep(1)

        results.sort(
            reverse=True,
            key=lambda x: x.popularity if x.popularity is not None else -1,
        )

        return cls(entries=tuple(results))

    def to_markdown_table(self, *, header: str | None = None) -> str:
        """Converts the MediaEntryCollection to a Markdown table string."""
        table = PrettyTable()
        table.set_style(TableStyle.MARKDOWN)
        table.align = "l"
        table.field_names = ["Idx", "Title", "Year", "Score", "Links"]
        for idx, entry in enumerate(self.entries, start=1):
            table.add_row(
                [
                    idx,
                    entry.title,
                    entry.year,
                    entry.score,
                    f"[SeaDex]({entry.seadex_url}), [AniList]({entry.anilist_url})",
                ],
            )

        return f"{header}\n{table.get_formatted_string()}" if header else table.get_formatted_string()

    def to_json(self) -> str:
        """Converts the MediaEntryCollection to a JSON string."""
        return self.model_dump_json(indent=2)
