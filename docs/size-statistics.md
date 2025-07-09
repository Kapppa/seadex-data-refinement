# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `105.1 TiB`
- Best size: `76.7 TiB`
- Alt size: `28.3 TiB`
- Realistic size: `81.2 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.4 TiB   | 12.2 TiB (84.30%)   | 184 (~80.4 GiB each)  |
| 2    | CRUCiBLE         | 7.1 TiB    | 7.1 TiB (99.27%)    | 94 (~77.4 GiB each)   |
| 3    | NAN0             | 5.4 TiB    | 5.3 TiB (98.59%)    | 75 (~73.3 GiB each)   |
| 4    | sam              | 3.8 TiB    | 3.4 TiB (88.65%)    | 133 (~29.6 GiB each)  |
| 5    | hchcsen          | 2.4 TiB    | 1.5 TiB (63.97%)    | 62 (~39.8 GiB each)   |
| 6    | TTGA             | 2.4 TiB    | 2.2 TiB (91.85%)    | 33 (~74.4 GiB each)   |
| 7    | B00BA            | 2.3 TiB    | 2.3 TiB (100.00%)   | 25 (~92.6 GiB each)   |
| 8    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 50 (~43.7 GiB each)   |
| 9    | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 10   | SubsPlease       | 1.4 TiB    | 190.4 GiB (13.02%)  | 85 (~17.2 GiB each)   |
| 11   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 12   | NOGRP            | 1.4 TiB    | 849.8 GiB (60.74%)  | 21 (~66.6 GiB each)   |
| 13   | MTBB             | 1.4 TiB    | 1.1 TiB (81.31%)    | 90 (~15.5 GiB each)   |
| 14   | PMR              | 1.3 TiB    | 1.3 TiB (100.00%)   | 16 (~85.2 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | RUDY             | 1.0 TiB    | 1.0 TiB (97.53%)    | 13 (~81.7 GiB each)   |
| 17   | smol             | 1010.8 GiB | 961.3 GiB (95.11%)  | 58 (~17.4 GiB each)   |
| 18   | LYS1TH3A         | 938.0 GiB  | 918.5 GiB (97.92%)  | 37 (~25.4 GiB each)   |
| 19   | KH               | 899.5 GiB  | 307.1 GiB (34.14%)  | 54 (~16.7 GiB each)   |
| 20   | YURI             | 898.8 GiB  | 401.7 GiB (44.70%)  | 76 (~11.8 GiB each)   |
| 21   | Vodes            | 853.4 GiB  | 533.6 GiB (62.53%)  | 19 (~44.9 GiB each)   |
| 22   | LostYears        | 807.3 GiB  | 288.6 GiB (35.75%)  | 49 (~16.5 GiB each)   |
| 23   | Holomux          | 768.0 GiB  | 194.2 GiB (25.29%)  | 30 (~25.6 GiB each)   |
| 24   | Arid             | 762.1 GiB  | 211.8 GiB (27.79%)  | 47 (~16.2 GiB each)   |
| 25   | Bunny-Apocalypse | 760.0 GiB  | 173.8 GiB (22.87%)  | 35 (~21.7 GiB each)   |
| 26   | FraMeSToR        | 745.7 GiB  | 745.7 GiB (100.00%) | 10 (~74.6 GiB each)   |
| 27   | ZeroBuild        | 743.1 GiB  | 646.3 GiB (86.97%)  | 16 (~46.4 GiB each)   |
| 28   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 29   | A&C              | 726.3 GiB  | 699.8 GiB (96.35%)  | 4 (~181.6 GiB each)   |
| 30   | WAP              | 692.7 GiB  | 692.7 GiB (100.00%) | 7 (~99.0 GiB each)    |
| 31   | Okay-Subs        | 684.2 GiB  | 649.4 GiB (94.92%)  | 34 (~20.1 GiB each)   |
| 32   | Lulu             | 678.0 GiB  | 384.6 GiB (56.73%)  | 35 (~19.4 GiB each)   |
| 33   | Drag             | 655.7 GiB  | 146.0 GiB (22.26%)  | 59 (~11.1 GiB each)   |
| 34   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 35   | Flugel           | 584.4 GiB  | 584.4 GiB (100.00%) | 19 (~30.8 GiB each)   |
| 36   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 37   | UDF              | 579.7 GiB  | 203.8 GiB (35.15%)  | 24 (~24.2 GiB each)   |
| 38   | koala            | 554.9 GiB  | 554.9 GiB (100.00%) | 13 (~42.7 GiB each)   |
| 39   | FLE              | 546.2 GiB  | 526.4 GiB (96.37%)  | 15 (~36.4 GiB each)   |
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
| 50   | Others           | 33.1 TiB   | 18.3 TiB (55.33%)   | 1681 (~20.2 GiB each) |
