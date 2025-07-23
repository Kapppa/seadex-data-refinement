# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `107.1 TiB`
- Best size: `78.8 TiB`
- Alt size: `28.3 TiB`
- Realistic size: `82.9 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.4 TiB   | 12.3 TiB (85.32%)   | 184 (~80.4 GiB each)  |
| 2    | CRUCiBLE         | 7.6 TiB    | 7.6 TiB (100.00%)   | 101 (~77.2 GiB each)  |
| 3    | NAN0             | 5.6 TiB    | 5.5 TiB (98.65%)    | 78 (~73.4 GiB each)   |
| 4    | sam              | 3.7 TiB    | 3.4 TiB (91.41%)    | 129 (~29.6 GiB each)  |
| 5    | TTGA             | 2.5 TiB    | 2.3 TiB (92.12%)    | 34 (~74.6 GiB each)   |
| 6    | hchcsen          | 2.4 TiB    | 1.5 TiB (64.53%)    | 62 (~39.5 GiB each)   |
| 7    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 51 (~43.2 GiB each)   |
| 8    | B00BA            | 2.1 TiB    | 2.1 TiB (100.00%)   | 23 (~92.9 GiB each)   |
| 9    | PMR              | 1.7 TiB    | 1.7 TiB (100.00%)   | 21 (~84.7 GiB each)   |
| 10   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 11   | MTBB             | 1.4 TiB    | 1.2 TiB (82.17%)    | 95 (~15.4 GiB each)   |
| 12   | SubsPlease       | 1.4 TiB    | 206.6 GiB (14.28%)  | 84 (~17.2 GiB each)   |
| 13   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 14   | NOGRP            | 1.4 TiB    | 849.8 GiB (60.74%)  | 21 (~66.6 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | RUDY             | 1.0 TiB    | 1.0 TiB (97.55%)    | 14 (~76.2 GiB each)   |
| 17   | smol             | 1010.8 GiB | 961.3 GiB (95.11%)  | 58 (~17.4 GiB each)   |
| 18   | LYS1TH3A         | 938.0 GiB  | 918.5 GiB (97.92%)  | 37 (~25.4 GiB each)   |
| 19   | KH               | 917.3 GiB  | 239.8 GiB (26.14%)  | 55 (~16.7 GiB each)   |
| 20   | YURI             | 898.8 GiB  | 393.1 GiB (43.74%)  | 76 (~11.8 GiB each)   |
| 21   | Vodes            | 853.4 GiB  | 533.6 GiB (62.53%)  | 19 (~44.9 GiB each)   |
| 22   | koala            | 844.1 GiB  | 844.1 GiB (100.00%) | 16 (~52.8 GiB each)   |
| 23   | LostYears        | 807.3 GiB  | 288.6 GiB (35.75%)  | 49 (~16.5 GiB each)   |
| 24   | Bunny-Apocalypse | 776.7 GiB  | 173.8 GiB (22.38%)  | 36 (~21.6 GiB each)   |
| 25   | Holomux          | 768.0 GiB  | 194.2 GiB (25.29%)  | 30 (~25.6 GiB each)   |
| 26   | FraMeSToR        | 745.7 GiB  | 745.7 GiB (100.00%) | 10 (~74.6 GiB each)   |
| 27   | ZeroBuild        | 743.1 GiB  | 646.3 GiB (86.97%)  | 16 (~46.4 GiB each)   |
| 28   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 29   | A&C              | 726.3 GiB  | 699.8 GiB (96.35%)  | 4 (~181.6 GiB each)   |
| 30   | Reza             | 723.4 GiB  | 377.0 GiB (52.12%)  | 28 (~25.8 GiB each)   |
| 31   | Okay-Subs        | 703.1 GiB  | 686.1 GiB (97.57%)  | 34 (~20.7 GiB each)   |
| 32   | WAP              | 692.7 GiB  | 692.7 GiB (100.00%) | 7 (~99.0 GiB each)    |
| 33   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 34   | Arid             | 656.4 GiB  | 211.8 GiB (32.26%)  | 46 (~14.3 GiB each)   |
| 35   | Drag             | 655.7 GiB  | 146.0 GiB (22.26%)  | 59 (~11.1 GiB each)   |
| 36   | FLE              | 654.2 GiB  | 634.4 GiB (96.97%)  | 17 (~38.5 GiB each)   |
| 37   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 38   | Headpatter       | 601.0 GiB  | 393.9 GiB (65.55%)  | 29 (~20.7 GiB each)   |
| 39   | Flugel           | 584.4 GiB  | 584.4 GiB (100.00%) | 19 (~30.8 GiB each)   |
| 40   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 41   | UDF              | 579.7 GiB  | 203.8 GiB (35.15%)  | 24 (~24.2 GiB each)   |
| 42   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 43   | SEV              | 538.2 GiB  | 0 B (0.00%)         | 11 (~48.9 GiB each)   |
| 44   | CTR              | 507.1 GiB  | 113.6 GiB (22.40%)  | 26 (~19.5 GiB each)   |
| 45   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 5 (~99.3 GiB each)    |
| 46   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 47   | Almighty         | 478.9 GiB  | 0 B (0.00%)         | 2 (~239.5 GiB each)   |
| 48   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 49   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 50   | Others           | 33.5 TiB   | 18.6 TiB (55.49%)   | 1693 (~20.3 GiB each) |
