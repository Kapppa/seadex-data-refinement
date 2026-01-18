# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `123.5 TiB`
- Best size: `93.2 TiB`
- Alt size: `30.4 TiB`
- Realistic size: `96.1 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 15.1 TiB   | 13.2 TiB (87.24%)   | 187 (~82.8 GiB each)  |
| 2    | CRUCiBLE         | 10.8 TiB   | 10.8 TiB (100.00%)  | 146 (~75.4 GiB each)  |
| 3    | NAN0             | 7.6 TiB    | 7.5 TiB (99.00%)    | 101 (~76.7 GiB each)  |
| 4    | sam              | 3.9 TiB    | 3.6 TiB (92.07%)    | 135 (~29.8 GiB each)  |
| 5    | Headpatter       | 2.8 TiB    | 2.4 TiB (87.79%)    | 87 (~32.4 GiB each)   |
| 6    | PMR              | 2.6 TiB    | 2.6 TiB (100.00%)   | 34 (~78.7 GiB each)   |
| 7    | TTGA             | 2.6 TiB    | 2.4 TiB (92.43%)    | 36 (~73.3 GiB each)   |
| 8    | Moxie            | 2.6 TiB    | 2.6 TiB (100.00%)   | 68 (~38.8 GiB each)   |
| 9    | hchcsen          | 2.4 TiB    | 1.6 TiB (65.00%)    | 64 (~39.1 GiB each)   |
| 10   | B00BA            | 2.3 TiB    | 2.3 TiB (100.00%)   | 26 (~91.1 GiB each)   |
| 11   | SoM              | 1.8 TiB    | 1.8 TiB (100.00%)   | 3 (~614.9 GiB each)   |
| 12   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 13   | MTBB             | 1.5 TiB    | 1.2 TiB (83.44%)    | 99 (~15.4 GiB each)   |
| 14   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 20 (~72.3 GiB each)   |
| 15   | SubsPlease       | 1.3 TiB    | 190.6 GiB (14.06%)  | 79 (~17.2 GiB each)   |
| 16   | LaCroiX          | 1.3 TiB    | 1.3 TiB (100.00%)   | 19 (~71.2 GiB each)   |
| 17   | NOGRP            | 1.0 TiB    | 850.8 GiB (80.87%)  | 32 (~32.9 GiB each)   |
| 18   | smol             | 1.0 TiB    | 976.7 GiB (95.18%)  | 58 (~17.7 GiB each)   |
| 19   | FLE              | 936.1 GiB  | 897.9 GiB (95.93%)  | 23 (~40.7 GiB each)   |
| 20   | LYS1TH3A         | 935.0 GiB  | 909.6 GiB (97.29%)  | 36 (~26.0 GiB each)   |
| 21   | koala            | 900.1 GiB  | 900.1 GiB (100.00%) | 17 (~52.9 GiB each)   |
| 22   | KH               | 895.0 GiB  | 219.7 GiB (24.55%)  | 55 (~16.3 GiB each)   |
| 23   | YURI             | 868.7 GiB  | 385.1 GiB (44.33%)  | 71 (~12.2 GiB each)   |
| 24   | RUDY             | 846.8 GiB  | 828.3 GiB (97.80%)  | 11 (~77.0 GiB each)   |
| 25   | Vodes            | 827.1 GiB  | 533.6 GiB (64.51%)  | 18 (~46.0 GiB each)   |
| 26   | FraMeSToR        | 822.9 GiB  | 822.9 GiB (100.00%) | 12 (~68.6 GiB each)   |
| 27   | Holomux          | 804.4 GiB  | 163.2 GiB (20.29%)  | 29 (~27.7 GiB each)   |
| 28   | YURASUKA         | 792.7 GiB  | 178.6 GiB (22.53%)  | 71 (~11.2 GiB each)   |
| 29   | sittingmongoose  | 782.5 GiB  | 782.5 GiB (100.00%) | 1 (~782.5 GiB each)   |
| 30   | A&C              | 779.4 GiB  | 753.0 GiB (96.60%)  | 5 (~155.9 GiB each)   |
| 31   | Okay-Subs        | 778.8 GiB  | 761.8 GiB (97.81%)  | 38 (~20.5 GiB each)   |
| 32   | ZeroBuild        | 761.4 GiB  | 681.4 GiB (89.50%)  | 17 (~44.8 GiB each)   |
| 33   | Bunny-Apocalypse | 753.1 GiB  | 173.8 GiB (23.08%)  | 37 (~20.4 GiB each)   |
| 34   | LostYears        | 727.1 GiB  | 207.6 GiB (28.55%)  | 43 (~16.9 GiB each)   |
| 35   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 36   | Reza             | 665.1 GiB  | 318.7 GiB (47.92%)  | 27 (~24.6 GiB each)   |
| 37   | Arid             | 648.0 GiB  | 210.6 GiB (32.50%)  | 46 (~14.1 GiB each)   |
| 38   | Drag             | 639.7 GiB  | 146.0 GiB (22.81%)  | 58 (~11.0 GiB each)   |
| 39   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 40   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 41   | SEV              | 568.2 GiB  | 0 B (0.00%)         | 12 (~47.3 GiB each)   |
| 42   | Almighty         | 544.3 GiB  | 0 B (0.00%)         | 4 (~136.1 GiB each)   |
| 43   | Erai-raws        | 541.2 GiB  | 69.0 GiB (12.75%)   | 32 (~16.9 GiB each)   |
| 44   | WAP              | 540.8 GiB  | 540.8 GiB (100.00%) | 6 (~90.1 GiB each)    |
| 45   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 46   | UDF              | 530.9 GiB  | 249.3 GiB (46.96%)  | 27 (~19.7 GiB each)   |
| 47   | Mehul            | 525.4 GiB  | 525.4 GiB (100.00%) | 15 (~35.0 GiB each)   |
| 48   | Pizza            | 519.0 GiB  | 366.8 GiB (70.68%)  | 9 (~57.7 GiB each)    |
| 49   | CTR              | 500.5 GiB  | 113.6 GiB (22.70%)  | 25 (~20.0 GiB each)   |
| 50   | Others           | 38.6 TiB   | 21.6 TiB (55.92%)   | 1785 (~22.2 GiB each) |
