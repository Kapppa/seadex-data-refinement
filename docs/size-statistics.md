# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `91.4 TiB`
- Best size: `66.5 TiB`
- Alt size: `24.9 TiB`
- Realistic size: `70.2 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.4 TiB   | 12.0 TiB (83.74%)   | 181 (~81.3 GiB each)  |
| 2    | NAN0             | 4.2 TiB    | 4.0 TiB (95.04%)    | 61 (~70.4 GiB each)   |
| 3    | sam              | 3.7 TiB    | 3.4 TiB (90.32%)    | 131 (~29.1 GiB each)  |
| 4    | CRUCiBLE         | 3.4 TiB    | 3.4 TiB (100.00%)   | 45 (~78.2 GiB each)   |
| 5    | TTGA             | 2.3 TiB    | 2.1 TiB (91.22%)    | 32 (~74.5 GiB each)   |
| 6    | hchcsen          | 2.2 TiB    | 1.5 TiB (69.25%)    | 55 (~40.2 GiB each)   |
| 7    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 47 (~45.5 GiB each)   |
| 8    | JySzE            | 1.8 TiB    | 1.8 TiB (100.00%)   | 7 (~265.9 GiB each)   |
| 9    | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 10   | B00BA            | 1.4 TiB    | 1.4 TiB (100.00%)   | 16 (~86.9 GiB each)   |
| 11   | MTBB             | 1.3 TiB    | 1.1 TiB (83.73%)    | 86 (~15.2 GiB each)   |
| 12   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 13   | NOGRP            | 1.2 TiB    | 805.4 GiB (63.40%)  | 15 (~84.7 GiB each)   |
| 14   | SubsPlease       | 1.1 TiB    | 177.7 GiB (15.24%)  | 70 (~16.7 GiB each)   |
| 15   | PMR              | 1.0 TiB    | 1.0 TiB (100.00%)   | 12 (~89.6 GiB each)   |
| 16   | YURI             | 903.6 GiB  | 463.0 GiB (51.24%)  | 77 (~11.7 GiB each)   |
| 17   | smol             | 899.2 GiB  | 866.2 GiB (96.33%)  | 55 (~16.3 GiB each)   |
| 18   | LostYears        | 898.0 GiB  | 345.7 GiB (38.50%)  | 54 (~16.6 GiB each)   |
| 19   | LYS1TH3A         | 887.5 GiB  | 868.0 GiB (97.80%)  | 37 (~24.0 GiB each)   |
| 20   | KH               | 793.5 GiB  | 290.9 GiB (36.66%)  | 48 (~16.5 GiB each)   |
| 21   | Arid             | 785.1 GiB  | 225.6 GiB (28.73%)  | 46 (~17.1 GiB each)   |
| 22   | Vodes            | 769.7 GiB  | 449.9 GiB (58.45%)  | 18 (~42.8 GiB each)   |
| 23   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 17 (~44.3 GiB each)   |
| 24   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 25   | Holomux          | 731.4 GiB  | 154.4 GiB (21.11%)  | 29 (~25.2 GiB each)   |
| 26   | A&C              | 728.3 GiB  | 701.7 GiB (96.35%)  | 4 (~182.1 GiB each)   |
| 27   | Lulu             | 678.0 GiB  | 446.4 GiB (65.83%)  | 34 (~19.9 GiB each)   |
| 28   | Bunny-Apocalypse | 674.5 GiB  | 173.8 GiB (25.77%)  | 31 (~21.8 GiB each)   |
| 29   | Drag             | 655.7 GiB  | 164.5 GiB (25.09%)  | 60 (~10.9 GiB each)   |
| 30   | Meakes           | 624.4 GiB  | 624.4 GiB (100.00%) | 8 (~78.0 GiB each)    |
| 31   | Okay-Subs        | 594.4 GiB  | 559.7 GiB (94.16%)  | 29 (~20.5 GiB each)   |
| 32   | Flugel           | 587.0 GiB  | 587.0 GiB (100.00%) | 19 (~30.9 GiB each)   |
| 33   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 34   | UDF              | 569.1 GiB  | 211.4 GiB (37.15%)  | 24 (~23.7 GiB each)   |
| 35   | RUDY             | 550.9 GiB  | 514.8 GiB (93.45%)  | 10 (~55.1 GiB each)   |
| 36   | Reza             | 540.1 GiB  | 193.7 GiB (35.87%)  | 26 (~20.8 GiB each)   |
| 37   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 38   | koala            | 534.3 GiB  | 534.3 GiB (100.00%) | 12 (~44.5 GiB each)   |
| 39   | hydes            | 515.4 GiB  | 515.4 GiB (100.00%) | 13 (~39.6 GiB each)   |
| 40   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)   |
| 41   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 4 (~124.2 GiB each)   |
| 42   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 43   | Almighty         | 491.4 GiB  | 0 B (0.00%)         | 2 (~245.7 GiB each)   |
| 44   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 45   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 32 (~14.7 GiB each)   |
| 46   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 47   | FraMeSToR        | 456.6 GiB  | 456.6 GiB (100.00%) | 8 (~57.1 GiB each)    |
| 48   | OZR              | 451.8 GiB  | 292.7 GiB (64.78%)  | 15 (~30.1 GiB each)   |
| 49   | IK               | 400.9 GiB  | 177.9 GiB (44.36%)  | 22 (~18.2 GiB each)   |
| 50   | Others           | 27.8 TiB   | 15.8 TiB (56.92%)   | 1464 (~19.5 GiB each) |
