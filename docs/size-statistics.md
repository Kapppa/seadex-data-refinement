# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `115.8 TiB`
- Best size: `86.6 TiB`
- Alt size: `29.1 TiB`
- Realistic size: `90.2 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.5 TiB   | 12.5 TiB (85.69%)   | 185 (~80.5 GiB each)  |
| 2    | CRUCiBLE         | 10.2 TiB   | 10.2 TiB (100.00%)  | 135 (~77.1 GiB each)  |
| 3    | NAN0             | 6.6 TiB    | 6.5 TiB (98.85%)    | 88 (~76.5 GiB each)   |
| 4    | sam              | 3.8 TiB    | 3.5 TiB (92.17%)    | 131 (~29.7 GiB each)  |
| 5    | TTGA             | 2.7 TiB    | 2.5 TiB (92.70%)    | 37 (~74.1 GiB each)   |
| 6    | B00BA            | 2.5 TiB    | 2.5 TiB (100.00%)   | 27 (~94.1 GiB each)   |
| 7    | PMR              | 2.5 TiB    | 2.5 TiB (100.00%)   | 32 (~78.8 GiB each)   |
| 8    | Moxie            | 2.4 TiB    | 2.4 TiB (100.00%)   | 61 (~41.1 GiB each)   |
| 9    | hchcsen          | 2.4 TiB    | 1.5 TiB (64.49%)    | 61 (~40.2 GiB each)   |
| 10   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 11   | MTBB             | 1.5 TiB    | 1.2 TiB (83.20%)    | 94 (~15.8 GiB each)   |
| 12   | Headpatter       | 1.4 TiB    | 1.2 TiB (85.37%)    | 54 (~26.2 GiB each)   |
| 13   | SubsPlease       | 1.4 TiB    | 206.6 GiB (14.70%)  | 82 (~17.1 GiB each)   |
| 14   | LazyRemux        | 1.3 TiB    | 1.3 TiB (100.00%)   | 19 (~71.7 GiB each)   |
| 15   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 16   | NOGRP            | 1.0 TiB    | 862.0 GiB (81.33%)  | 30 (~35.3 GiB each)   |
| 17   | smol             | 1010.8 GiB | 961.3 GiB (95.11%)  | 58 (~17.4 GiB each)   |
| 18   | KH               | 947.9 GiB  | 219.7 GiB (23.18%)  | 56 (~16.9 GiB each)   |
| 19   | LYS1TH3A         | 938.0 GiB  | 909.6 GiB (96.98%)  | 37 (~25.4 GiB each)   |
| 20   | FraMeSToR        | 903.8 GiB  | 903.8 GiB (100.00%) | 13 (~69.5 GiB each)   |
| 21   | koala            | 871.3 GiB  | 871.3 GiB (100.00%) | 17 (~51.3 GiB each)   |
| 22   | YURI             | 868.7 GiB  | 385.1 GiB (44.33%)  | 71 (~12.2 GiB each)   |
| 23   | RUDY             | 846.8 GiB  | 828.3 GiB (97.80%)  | 11 (~77.0 GiB each)   |
| 24   | Vodes            | 827.1 GiB  | 533.6 GiB (64.51%)  | 18 (~46.0 GiB each)   |
| 25   | LostYears        | 810.6 GiB  | 288.6 GiB (35.60%)  | 49 (~16.5 GiB each)   |
| 26   | Bunny-Apocalypse | 809.5 GiB  | 173.8 GiB (21.47%)  | 38 (~21.3 GiB each)   |
| 27   | Holomux          | 804.4 GiB  | 163.2 GiB (20.29%)  | 29 (~27.7 GiB each)   |
| 28   | A&C              | 779.4 GiB  | 753.0 GiB (96.60%)  | 5 (~155.9 GiB each)   |
| 29   | WAP              | 776.1 GiB  | 776.1 GiB (100.00%) | 8 (~97.0 GiB each)    |
| 30   | Okay-Subs        | 752.8 GiB  | 735.7 GiB (97.73%)  | 37 (~20.3 GiB each)   |
| 31   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 32   | ZeroBuild        | 726.3 GiB  | 646.3 GiB (89.00%)  | 15 (~48.4 GiB each)   |
| 33   | Reza             | 723.4 GiB  | 377.0 GiB (52.12%)  | 28 (~25.8 GiB each)   |
| 34   | LaCroiX          | 691.7 GiB  | 691.7 GiB (100.00%) | 11 (~62.9 GiB each)   |
| 35   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 36   | FLE              | 672.5 GiB  | 634.4 GiB (94.33%)  | 18 (~37.4 GiB each)   |
| 37   | Arid             | 642.0 GiB  | 211.8 GiB (32.99%)  | 45 (~14.3 GiB each)   |
| 38   | Drag             | 639.7 GiB  | 146.0 GiB (22.81%)  | 58 (~11.0 GiB each)   |
| 39   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 40   | UDF              | 625.2 GiB  | 249.3 GiB (39.88%)  | 28 (~22.3 GiB each)   |
| 41   | SEV              | 613.8 GiB  | 0 B (0.00%)         | 13 (~47.2 GiB each)   |
| 42   | YURASUKA         | 590.8 GiB  | 107.7 GiB (18.23%)  | 54 (~10.9 GiB each)   |
| 43   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 44   | Flugel           | 559.0 GiB  | 559.0 GiB (100.00%) | 18 (~31.1 GiB each)   |
| 45   | Almighty         | 544.3 GiB  | 0 B (0.00%)         | 4 (~136.1 GiB each)   |
| 46   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 47   | Pizza            | 519.0 GiB  | 366.8 GiB (70.68%)  | 9 (~57.7 GiB each)    |
| 48   | Mehul            | 514.3 GiB  | 514.3 GiB (100.00%) | 14 (~36.7 GiB each)   |
| 49   | SCY              | 503.5 GiB  | 185.4 GiB (36.83%)  | 29 (~17.4 GiB each)   |
| 50   | Others           | 35.8 TiB   | 20.0 TiB (55.83%)   | 1719 (~21.3 GiB each) |
