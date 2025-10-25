# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `117.3 TiB`
- Best size: `88.0 TiB`
- Alt size: `29.3 TiB`
- Realistic size: `91.5 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.4 TiB   | 12.3 TiB (85.54%)   | 183 (~80.5 GiB each)  |
| 2    | CRUCiBLE         | 10.5 TiB   | 10.5 TiB (100.00%)  | 139 (~77.0 GiB each)  |
| 3    | NAN0             | 6.9 TiB    | 6.9 TiB (98.91%)    | 93 (~76.4 GiB each)   |
| 4    | sam              | 3.8 TiB    | 3.5 TiB (92.17%)    | 131 (~29.7 GiB each)  |
| 5    | TTGA             | 2.7 TiB    | 2.5 TiB (92.70%)    | 37 (~74.1 GiB each)   |
| 6    | PMR              | 2.5 TiB    | 2.5 TiB (100.00%)   | 34 (~76.4 GiB each)   |
| 7    | B00BA            | 2.5 TiB    | 2.5 TiB (100.00%)   | 27 (~94.1 GiB each)   |
| 8    | hchcsen          | 2.5 TiB    | 1.6 TiB (65.35%)    | 63 (~39.9 GiB each)   |
| 9    | Moxie            | 2.4 TiB    | 2.4 TiB (100.00%)   | 61 (~41.1 GiB each)   |
| 10   | Headpatter       | 1.7 TiB    | 1.5 TiB (88.10%)    | 59 (~29.5 GiB each)   |
| 11   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 12   | MTBB             | 1.5 TiB    | 1.2 TiB (83.20%)    | 94 (~15.8 GiB each)   |
| 13   | SubsPlease       | 1.4 TiB    | 206.6 GiB (14.53%)  | 83 (~17.1 GiB each)   |
| 14   | LazyRemux        | 1.3 TiB    | 1.3 TiB (100.00%)   | 19 (~71.7 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | NOGRP            | 1.1 TiB    | 862.0 GiB (79.62%)  | 33 (~32.8 GiB each)   |
| 17   | smol             | 1010.8 GiB | 961.3 GiB (95.11%)  | 58 (~17.4 GiB each)   |
| 18   | KH               | 947.9 GiB  | 219.7 GiB (23.18%)  | 56 (~16.9 GiB each)   |
| 19   | LYS1TH3A         | 938.0 GiB  | 909.6 GiB (96.98%)  | 37 (~25.4 GiB each)   |
| 20   | FraMeSToR        | 903.8 GiB  | 903.8 GiB (100.00%) | 13 (~69.5 GiB each)   |
| 21   | koala            | 871.3 GiB  | 871.3 GiB (100.00%) | 17 (~51.3 GiB each)   |
| 22   | YURI             | 868.7 GiB  | 385.1 GiB (44.33%)  | 71 (~12.2 GiB each)   |
| 23   | RUDY             | 846.8 GiB  | 828.3 GiB (97.80%)  | 11 (~77.0 GiB each)   |
| 24   | Vodes            | 827.1 GiB  | 533.6 GiB (64.51%)  | 18 (~46.0 GiB each)   |
| 25   | Bunny-Apocalypse | 809.5 GiB  | 173.8 GiB (21.47%)  | 38 (~21.3 GiB each)   |
| 26   | Holomux          | 804.4 GiB  | 163.2 GiB (20.29%)  | 29 (~27.7 GiB each)   |
| 27   | LostYears        | 780.1 GiB  | 288.6 GiB (36.99%)  | 46 (~17.0 GiB each)   |
| 28   | A&C              | 779.4 GiB  | 753.0 GiB (96.60%)  | 5 (~155.9 GiB each)   |
| 29   | WAP              | 776.1 GiB  | 776.1 GiB (100.00%) | 8 (~97.0 GiB each)    |
| 30   | Okay-Subs        | 752.8 GiB  | 735.7 GiB (97.73%)  | 37 (~20.3 GiB each)   |
| 31   | ZeroBuild        | 741.0 GiB  | 661.0 GiB (89.21%)  | 16 (~46.3 GiB each)   |
| 32   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 33   | Reza             | 723.4 GiB  | 377.0 GiB (52.12%)  | 28 (~25.8 GiB each)   |
| 34   | LaCroiX          | 691.7 GiB  | 691.7 GiB (100.00%) | 11 (~62.9 GiB each)   |
| 35   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 36   | FLE              | 672.5 GiB  | 634.4 GiB (94.33%)  | 18 (~37.4 GiB each)   |
| 37   | Arid             | 642.0 GiB  | 211.8 GiB (32.99%)  | 45 (~14.3 GiB each)   |
| 38   | Drag             | 639.7 GiB  | 146.0 GiB (22.81%)  | 58 (~11.0 GiB each)   |
| 39   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 40   | UDF              | 625.2 GiB  | 249.3 GiB (39.88%)  | 28 (~22.3 GiB each)   |
| 41   | SEV              | 613.8 GiB  | 0 B (0.00%)         | 13 (~47.2 GiB each)   |
| 42   | YURASUKA         | 604.7 GiB  | 107.7 GiB (17.81%)  | 55 (~11.0 GiB each)   |
| 43   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 44   | Almighty         | 544.3 GiB  | 0 B (0.00%)         | 4 (~136.1 GiB each)   |
| 45   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 46   | Pizza            | 519.0 GiB  | 366.8 GiB (70.68%)  | 9 (~57.7 GiB each)    |
| 47   | Mehul            | 514.3 GiB  | 514.3 GiB (100.00%) | 14 (~36.7 GiB each)   |
| 48   | SCY              | 503.5 GiB  | 185.4 GiB (36.83%)  | 29 (~17.4 GiB each)   |
| 49   | CTR              | 500.7 GiB  | 113.6 GiB (22.69%)  | 25 (~20.0 GiB each)   |
| 50   | Others           | 36.3 TiB   | 20.8 TiB (57.16%)   | 1724 (~21.6 GiB each) |
