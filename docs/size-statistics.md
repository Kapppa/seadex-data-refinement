# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `106.4 TiB`
- Best size: `77.9 TiB`
- Alt size: `28.4 TiB`
- Realistic size: `82.3 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.6 TiB   | 12.3 TiB (84.14%)   | 187 (~80.2 GiB each)  |
| 2    | CRUCiBLE         | 7.5 TiB    | 7.4 TiB (99.31%)    | 99 (~77.3 GiB each)   |
| 3    | NAN0             | 5.6 TiB    | 5.5 TiB (98.65%)    | 78 (~73.4 GiB each)   |
| 4    | sam              | 3.7 TiB    | 3.4 TiB (91.41%)    | 129 (~29.6 GiB each)  |
| 5    | TTGA             | 2.5 TiB    | 2.3 TiB (92.12%)    | 34 (~74.6 GiB each)   |
| 6    | hchcsen          | 2.4 TiB    | 1.5 TiB (63.97%)    | 62 (~39.8 GiB each)   |
| 7    | B00BA            | 2.3 TiB    | 2.3 TiB (100.00%)   | 25 (~92.6 GiB each)   |
| 8    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 50 (~43.7 GiB each)   |
| 9    | PMR              | 1.6 TiB    | 1.6 TiB (100.00%)   | 20 (~82.1 GiB each)   |
| 10   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 11   | SubsPlease       | 1.4 TiB    | 190.4 GiB (12.85%)  | 86 (~17.2 GiB each)   |
| 12   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 13   | MTBB             | 1.4 TiB    | 1.1 TiB (81.85%)    | 93 (~15.5 GiB each)   |
| 14   | NOGRP            | 1.4 TiB    | 849.8 GiB (60.74%)  | 21 (~66.6 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | RUDY             | 1.0 TiB    | 1.0 TiB (97.55%)    | 14 (~76.2 GiB each)   |
| 17   | smol             | 1010.8 GiB | 961.3 GiB (95.11%)  | 58 (~17.4 GiB each)   |
| 18   | LYS1TH3A         | 938.0 GiB  | 918.5 GiB (97.92%)  | 37 (~25.4 GiB each)   |
| 19   | KH               | 917.3 GiB  | 307.1 GiB (33.48%)  | 55 (~16.7 GiB each)   |
| 20   | YURI             | 898.8 GiB  | 401.7 GiB (44.70%)  | 76 (~11.8 GiB each)   |
| 21   | Vodes            | 853.4 GiB  | 533.6 GiB (62.53%)  | 19 (~44.9 GiB each)   |
| 22   | LostYears        | 807.3 GiB  | 288.6 GiB (35.75%)  | 49 (~16.5 GiB each)   |
| 23   | Bunny-Apocalypse | 777.1 GiB  | 173.8 GiB (22.37%)  | 36 (~21.6 GiB each)   |
| 24   | Holomux          | 768.0 GiB  | 194.2 GiB (25.29%)  | 30 (~25.6 GiB each)   |
| 25   | FraMeSToR        | 745.7 GiB  | 745.7 GiB (100.00%) | 10 (~74.6 GiB each)   |
| 26   | ZeroBuild        | 743.1 GiB  | 646.3 GiB (86.97%)  | 16 (~46.4 GiB each)   |
| 27   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 28   | A&C              | 726.3 GiB  | 699.8 GiB (96.35%)  | 4 (~181.6 GiB each)   |
| 29   | WAP              | 692.7 GiB  | 692.7 GiB (100.00%) | 7 (~99.0 GiB each)    |
| 30   | Okay-Subs        | 684.2 GiB  | 649.4 GiB (94.92%)  | 34 (~20.1 GiB each)   |
| 31   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 32   | Arid             | 656.4 GiB  | 211.8 GiB (32.26%)  | 46 (~14.3 GiB each)   |
| 33   | Drag             | 655.7 GiB  | 146.0 GiB (22.26%)  | 59 (~11.1 GiB each)   |
| 34   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 35   | koala            | 594.9 GiB  | 594.9 GiB (100.00%) | 13 (~45.8 GiB each)   |
| 36   | Flugel           | 584.4 GiB  | 584.4 GiB (100.00%) | 19 (~30.8 GiB each)   |
| 37   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 38   | UDF              | 579.7 GiB  | 203.8 GiB (35.15%)  | 24 (~24.2 GiB each)   |
| 39   | FLE              | 552.9 GiB  | 533.1 GiB (96.42%)  | 16 (~34.6 GiB each)   |
| 40   | Reza             | 540.1 GiB  | 193.7 GiB (35.87%)  | 27 (~20.0 GiB each)   |
| 41   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 42   | SEV              | 538.2 GiB  | 0 B (0.00%)         | 11 (~48.9 GiB each)   |
| 43   | CTR              | 507.1 GiB  | 113.6 GiB (22.40%)  | 26 (~19.5 GiB each)   |
| 44   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 5 (~99.3 GiB each)    |
| 45   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 46   | Almighty         | 478.9 GiB  | 0 B (0.00%)         | 2 (~239.5 GiB each)   |
| 47   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 48   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 49   | LaCroiX          | 457.7 GiB  | 457.7 GiB (100.00%) | 6 (~76.3 GiB each)    |
| 50   | Others           | 33.3 TiB   | 18.3 TiB (55.00%)   | 1698 (~20.1 GiB each) |
