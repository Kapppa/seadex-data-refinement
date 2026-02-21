# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `127.8 TiB`
- Best size: `97.1 TiB`
- Alt size: `30.8 TiB`
- Realistic size: `100.3 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.3 TiB   | 13.5 TiB (94.43%)   | 191 (~76.5 GiB each)  |
| 2    | CRUCiBLE         | 10.7 TiB   | 10.7 TiB (100.00%)  | 145 (~75.4 GiB each)  |
| 3    | NAN0             | 7.9 TiB    | 7.9 TiB (99.05%)    | 106 (~76.7 GiB each)  |
| 4    | sam              | 3.9 TiB    | 3.6 TiB (92.76%)    | 132 (~30.3 GiB each)  |
| 5    | Headpatter       | 3.4 TiB    | 3.0 TiB (86.19%)    | 100 (~35.3 GiB each)  |
| 6    | Moxie            | 3.4 TiB    | 3.4 TiB (100.00%)   | 87 (~40.4 GiB each)   |
| 7    | PMR              | 2.9 TiB    | 2.9 TiB (100.00%)   | 36 (~81.3 GiB each)   |
| 8    | hchcsen          | 2.8 TiB    | 1.8 TiB (65.12%)    | 75 (~38.2 GiB each)   |
| 9    | TTGA             | 2.6 TiB    | 2.5 TiB (95.07%)    | 36 (~73.5 GiB each)   |
| 10   | B00BA            | 2.3 TiB    | 2.3 TiB (100.00%)   | 26 (~91.1 GiB each)   |
| 11   | SoM              | 1.8 TiB    | 1.8 TiB (100.00%)   | 3 (~614.9 GiB each)   |
| 12   | MTBB             | 1.6 TiB    | 1.3 TiB (84.20%)    | 103 (~15.7 GiB each)  |
| 13   | JySzE            | 1.5 TiB    | 1.5 TiB (100.00%)   | 8 (~192.8 GiB each)   |
| 14   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 20 (~72.3 GiB each)   |
| 15   | LaCroiX          | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~75.5 GiB each)   |
| 16   | SubsPlease       | 1.3 TiB    | 177.6 GiB (12.93%)  | 80 (~17.2 GiB each)   |
| 17   | smol             | 1.0 TiB    | 976.7 GiB (95.18%)  | 58 (~17.7 GiB each)   |
| 18   | NOGRP            | 973.2 GiB  | 771.9 GiB (79.32%)  | 31 (~31.4 GiB each)   |
| 19   | FLE              | 951.3 GiB  | 913.2 GiB (95.99%)  | 24 (~39.6 GiB each)   |
| 20   | KH               | 938.7 GiB  | 219.7 GiB (23.41%)  | 58 (~16.2 GiB each)   |
| 21   | LYS1TH3A         | 935.0 GiB  | 909.6 GiB (97.29%)  | 36 (~26.0 GiB each)   |
| 22   | koala            | 920.5 GiB  | 920.5 GiB (100.00%) | 18 (~51.1 GiB each)   |
| 23   | YURASUKA         | 874.3 GiB  | 217.4 GiB (24.86%)  | 77 (~11.4 GiB each)   |
| 24   | YURI             | 867.7 GiB  | 384.1 GiB (44.26%)  | 70 (~12.4 GiB each)   |
| 25   | RUDY             | 846.8 GiB  | 828.3 GiB (97.80%)  | 11 (~77.0 GiB each)   |
| 26   | Vodes            | 827.1 GiB  | 533.6 GiB (64.51%)  | 18 (~46.0 GiB each)   |
| 27   | FraMeSToR        | 822.9 GiB  | 822.9 GiB (100.00%) | 12 (~68.6 GiB each)   |
| 28   | Holomux          | 819.7 GiB  | 163.2 GiB (19.91%)  | 30 (~27.3 GiB each)   |
| 29   | sittingmongoose  | 782.5 GiB  | 782.5 GiB (100.00%) | 1 (~782.5 GiB each)   |
| 30   | A&C              | 779.4 GiB  | 753.0 GiB (96.60%)  | 5 (~155.9 GiB each)   |
| 31   | Okay-Subs        | 778.8 GiB  | 761.8 GiB (97.81%)  | 38 (~20.5 GiB each)   |
| 32   | UQW              | 765.4 GiB  | 36.3 GiB (4.74%)    | 8 (~95.7 GiB each)    |
| 33   | ZeroBuild        | 730.4 GiB  | 681.4 GiB (93.30%)  | 16 (~45.6 GiB each)   |
| 34   | Bunny-Apocalypse | 728.3 GiB  | 161.0 GiB (22.10%)  | 35 (~20.8 GiB each)   |
| 35   | LostYears        | 727.1 GiB  | 207.6 GiB (28.55%)  | 43 (~16.9 GiB each)   |
| 36   | Lulu             | 678.0 GiB  | 352.6 GiB (52.00%)  | 35 (~19.4 GiB each)   |
| 37   | Reza             | 665.1 GiB  | 318.7 GiB (47.92%)  | 27 (~24.6 GiB each)   |
| 38   | Arid             | 648.0 GiB  | 210.6 GiB (32.50%)  | 46 (~14.1 GiB each)   |
| 39   | Drag             | 641.2 GiB  | 146.0 GiB (22.76%)  | 59 (~10.9 GiB each)   |
| 40   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 41   | Erai-raws        | 630.9 GiB  | 101.9 GiB (16.16%)  | 37 (~17.1 GiB each)   |
| 42   | D4C              | 556.0 GiB  | 556.0 GiB (100.00%) | 2 (~278.0 GiB each)   |
| 43   | Almighty         | 555.9 GiB  | 0 B (0.00%)         | 5 (~111.2 GiB each)   |
| 44   | BBT-RMX          | 548.0 GiB  | 374.5 GiB (68.33%)  | 12 (~45.7 GiB each)   |
| 45   | GetItTwisted     | 541.8 GiB  | 302.3 GiB (55.79%)  | 33 (~16.4 GiB each)   |
| 46   | WAP              | 540.8 GiB  | 540.8 GiB (100.00%) | 6 (~90.1 GiB each)    |
| 47   | SEV              | 533.0 GiB  | 0 B (0.00%)         | 11 (~48.5 GiB each)   |
| 48   | UDF              | 530.9 GiB  | 249.3 GiB (46.96%)  | 27 (~19.7 GiB each)   |
| 49   | Mehul            | 525.4 GiB  | 525.4 GiB (100.00%) | 15 (~35.0 GiB each)   |
| 50   | Others           | 40.8 TiB   | 23.0 TiB (56.26%)   | 1859 (~22.5 GiB each) |
