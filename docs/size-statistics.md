# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `118.6 TiB`
- Best size: `89.2 TiB`
- Alt size: `29.4 TiB`
- Realistic size: `92.5 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.5 TiB   | 12.4 TiB (85.62%)   | 184 (~80.5 GiB each)  |
| 2    | CRUCiBLE         | 10.5 TiB   | 10.5 TiB (100.00%)  | 142 (~75.8 GiB each)  |
| 3    | NAN0             | 7.3 TiB    | 7.2 TiB (98.96%)    | 98 (~75.8 GiB each)   |
| 4    | sam              | 3.9 TiB    | 3.6 TiB (91.97%)    | 133 (~29.9 GiB each)  |
| 5    | TTGA             | 2.7 TiB    | 2.5 TiB (92.70%)    | 37 (~74.1 GiB each)   |
| 6    | PMR              | 2.6 TiB    | 2.6 TiB (100.00%)   | 34 (~78.7 GiB each)   |
| 7    | B00BA            | 2.5 TiB    | 2.5 TiB (100.00%)   | 27 (~94.1 GiB each)   |
| 8    | hchcsen          | 2.5 TiB    | 1.6 TiB (64.78%)    | 64 (~39.6 GiB each)   |
| 9    | Moxie            | 2.4 TiB    | 2.4 TiB (100.00%)   | 61 (~41.1 GiB each)   |
| 10   | Headpatter       | 1.9 TiB    | 1.7 TiB (87.59%)    | 66 (~29.9 GiB each)   |
| 11   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 12   | MTBB             | 1.5 TiB    | 1.2 TiB (83.03%)    | 94 (~15.9 GiB each)   |
| 13   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 20 (~72.3 GiB each)   |
| 14   | SubsPlease       | 1.4 TiB    | 206.6 GiB (14.55%)  | 83 (~17.1 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | NOGRP            | 1.1 TiB    | 862.0 GiB (79.62%)  | 33 (~32.8 GiB each)   |
| 17   | smol             | 1.0 TiB    | 976.7 GiB (95.18%)  | 58 (~17.7 GiB each)   |
| 18   | LaCroiX          | 990.6 GiB  | 990.6 GiB (100.00%) | 14 (~70.8 GiB each)   |
| 19   | LYS1TH3A         | 938.0 GiB  | 909.6 GiB (96.98%)  | 37 (~25.4 GiB each)   |
| 20   | FLE              | 934.0 GiB  | 895.9 GiB (95.92%)  | 22 (~42.5 GiB each)   |
| 21   | FraMeSToR        | 903.8 GiB  | 903.8 GiB (100.00%) | 13 (~69.5 GiB each)   |
| 22   | KH               | 895.0 GiB  | 219.7 GiB (24.55%)  | 55 (~16.3 GiB each)   |
| 23   | koala            | 871.3 GiB  | 871.3 GiB (100.00%) | 17 (~51.3 GiB each)   |
| 24   | YURI             | 868.7 GiB  | 385.1 GiB (44.33%)  | 71 (~12.2 GiB each)   |
| 25   | RUDY             | 846.8 GiB  | 828.3 GiB (97.80%)  | 11 (~77.0 GiB each)   |
| 26   | Vodes            | 827.1 GiB  | 533.6 GiB (64.51%)  | 18 (~46.0 GiB each)   |
| 27   | Bunny-Apocalypse | 809.5 GiB  | 173.8 GiB (21.47%)  | 38 (~21.3 GiB each)   |
| 28   | Holomux          | 804.4 GiB  | 163.2 GiB (20.29%)  | 29 (~27.7 GiB each)   |
| 29   | A&C              | 779.4 GiB  | 753.0 GiB (96.60%)  | 5 (~155.9 GiB each)   |
| 30   | LostYears        | 763.4 GiB  | 288.6 GiB (37.80%)  | 45 (~17.0 GiB each)   |
| 31   | Okay-Subs        | 752.8 GiB  | 735.7 GiB (97.73%)  | 37 (~20.3 GiB each)   |
| 32   | ZeroBuild        | 741.0 GiB  | 661.0 GiB (89.21%)  | 16 (~46.3 GiB each)   |
| 33   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 34   | WAP              | 699.2 GiB  | 699.2 GiB (100.00%) | 7 (~99.9 GiB each)    |
| 35   | YURASUKA         | 695.2 GiB  | 154.3 GiB (22.20%)  | 61 (~11.4 GiB each)   |
| 36   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 37   | Reza             | 665.1 GiB  | 318.7 GiB (47.92%)  | 27 (~24.6 GiB each)   |
| 38   | Arid             | 642.0 GiB  | 211.8 GiB (32.99%)  | 45 (~14.3 GiB each)   |
| 39   | Drag             | 639.7 GiB  | 146.0 GiB (22.81%)  | 58 (~11.0 GiB each)   |
| 40   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 41   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 42   | SEV              | 568.2 GiB  | 0 B (0.00%)         | 12 (~47.3 GiB each)   |
| 43   | Almighty         | 544.3 GiB  | 0 B (0.00%)         | 4 (~136.1 GiB each)   |
| 44   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 45   | UDF              | 530.9 GiB  | 249.3 GiB (46.96%)  | 27 (~19.7 GiB each)   |
| 46   | Pizza            | 519.0 GiB  | 366.8 GiB (70.68%)  | 9 (~57.7 GiB each)    |
| 47   | Mehul            | 514.3 GiB  | 514.3 GiB (100.00%) | 14 (~36.7 GiB each)   |
| 48   | CTR              | 500.7 GiB  | 113.6 GiB (22.69%)  | 25 (~20.0 GiB each)   |
| 49   | SCY              | 497.2 GiB  | 179.1 GiB (36.02%)  | 28 (~17.8 GiB each)   |
| 50   | Others           | 36.4 TiB   | 20.6 TiB (56.67%)   | 1738 (~21.4 GiB each) |
