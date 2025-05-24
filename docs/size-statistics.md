# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `101.4 TiB`
- Best size: `74.3 TiB`
- Alt size: `27.1 TiB`
- Realistic size: `78.5 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.7 TiB   | 12.3 TiB (83.72%)   | 189 (~79.7 GiB each)  |
| 2    | CRUCiBLE         | 5.7 TiB    | 5.7 TiB (100.00%)   | 73 (~80.3 GiB each)   |
| 3    | NAN0             | 5.0 TiB    | 4.9 TiB (98.48%)    | 70 (~72.7 GiB each)   |
| 4    | sam              | 3.9 TiB    | 3.4 TiB (88.71%)    | 133 (~29.7 GiB each)  |
| 5    | TTGA             | 2.5 TiB    | 2.3 TiB (94.85%)    | 34 (~74.6 GiB each)   |
| 6    | hchcsen          | 2.4 TiB    | 1.6 TiB (64.72%)    | 61 (~40.2 GiB each)   |
| 7    | Moxie            | 2.2 TiB    | 2.2 TiB (100.00%)   | 50 (~44.7 GiB each)   |
| 8    | B00BA            | 2.0 TiB    | 2.0 TiB (100.00%)   | 23 (~90.4 GiB each)   |
| 9    | JySzE            | 1.7 TiB    | 1.7 TiB (100.00%)   | 8 (~220.8 GiB each)   |
| 10   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 11   | MTBB             | 1.4 TiB    | 1.1 TiB (81.97%)    | 89 (~15.7 GiB each)   |
| 12   | PMR              | 1.4 TiB    | 1.4 TiB (100.00%)   | 15 (~92.2 GiB each)   |
| 13   | NOGRP            | 1.3 TiB    | 849.8 GiB (61.64%)  | 20 (~68.9 GiB each)   |
| 14   | SubsPlease       | 1.3 TiB    | 206.8 GiB (15.06%)  | 82 (~16.7 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | RUDY             | 1.1 TiB    | 1.0 TiB (97.62%)    | 13 (~84.5 GiB each)   |
| 17   | smol             | 980.9 GiB  | 947.9 GiB (96.64%)  | 57 (~17.2 GiB each)   |
| 18   | LYS1TH3A         | 938.0 GiB  | 918.5 GiB (97.92%)  | 37 (~25.4 GiB each)   |
| 19   | YURI             | 903.6 GiB  | 445.7 GiB (49.33%)  | 77 (~11.7 GiB each)   |
| 20   | KH               | 879.4 GiB  | 322.3 GiB (36.65%)  | 54 (~16.3 GiB each)   |
| 21   | LostYears        | 865.1 GiB  | 311.7 GiB (36.03%)  | 51 (~17.0 GiB each)   |
| 22   | Vodes            | 853.4 GiB  | 533.6 GiB (62.53%)  | 19 (~44.9 GiB each)   |
| 23   | Arid             | 788.5 GiB  | 206.7 GiB (26.21%)  | 48 (~16.4 GiB each)   |
| 24   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 17 (~44.3 GiB each)   |
| 25   | Bunny-Apocalypse | 748.1 GiB  | 173.8 GiB (23.23%)  | 34 (~22.0 GiB each)   |
| 26   | FraMeSToR        | 745.7 GiB  | 745.7 GiB (100.00%) | 10 (~74.6 GiB each)   |
| 27   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 28   | A&C              | 726.4 GiB  | 699.8 GiB (96.34%)  | 4 (~181.6 GiB each)   |
| 29   | Holomux          | 726.3 GiB  | 152.5 GiB (21.00%)  | 30 (~24.2 GiB each)   |
| 30   | Lulu             | 678.0 GiB  | 401.0 GiB (59.15%)  | 34 (~19.9 GiB each)   |
| 31   | Okay-Subs        | 663.2 GiB  | 628.5 GiB (94.76%)  | 32 (~20.7 GiB each)   |
| 32   | Drag             | 655.7 GiB  | 164.5 GiB (25.09%)  | 59 (~11.1 GiB each)   |
| 33   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 34   | Flugel           | 587.0 GiB  | 587.0 GiB (100.00%) | 19 (~30.9 GiB each)   |
| 35   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 36   | UDF              | 561.4 GiB  | 203.8 GiB (36.29%)  | 23 (~24.4 GiB each)   |
| 37   | koala            | 554.9 GiB  | 554.9 GiB (100.00%) | 13 (~42.7 GiB each)   |
| 38   | Reza             | 540.1 GiB  | 193.7 GiB (35.87%)  | 27 (~20.0 GiB each)   |
| 39   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 40   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)   |
| 41   | Almighty         | 500.9 GiB  | 0 B (0.00%)         | 3 (~167.0 GiB each)   |
| 42   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 5 (~99.3 GiB each)    |
| 43   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 44   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 45   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 32 (~14.7 GiB each)   |
| 46   | FLE              | 463.5 GiB  | 443.7 GiB (95.73%)  | 11 (~42.1 GiB each)   |
| 47   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 48   | OZR              | 451.8 GiB  | 292.7 GiB (64.78%)  | 15 (~30.1 GiB each)   |
| 49   | VULCAN           | 439.1 GiB  | 439.1 GiB (100.00%) | 5 (~87.8 GiB each)    |
| 50   | Others           | 31.3 TiB   | 17.5 TiB (55.83%)   | 1590 (~20.2 GiB each) |
