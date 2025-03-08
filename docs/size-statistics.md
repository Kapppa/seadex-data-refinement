# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent, only the former is considered; otherwise, all torrents are considered. Exact duplicates are also discarded.

## Overview

- Total size: `87.6 TiB`
- Best size: `63.6 TiB`
- Alt size: `24.0 TiB`
- Realistic size: `67.3 TiB`

The realistic size stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, fallback to the best single audio release if that's not present, and again fallback to whatever there is if neither exist.

## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Torrents        |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 13.8 TiB   | 11.6 TiB (84.06%)   | 175 (~80.6 GiB each)  |
| 2    | sam              | 3.7 TiB    | 3.4 TiB (90.32%)    | 130 (~29.3 GiB each)  |
| 3    | NAN0             | 3.6 TiB    | 3.5 TiB (97.88%)    | 54 (~67.5 GiB each)   |
| 4    | CRUCiBLE         | 2.8 TiB    | 2.8 TiB (100.00%)   | 35 (~82.9 GiB each)   |
| 5    | TTGA             | 2.2 TiB    | 2.0 TiB (90.60%)    | 31 (~71.8 GiB each)   |
| 6    | hchcsen          | 2.2 TiB    | 1.5 TiB (70.44%)    | 52 (~42.5 GiB each)   |
| 7    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 45 (~47.6 GiB each)   |
| 8    | JySzE            | 2.0 TiB    | 2.0 TiB (100.00%)   | 7 (~297.4 GiB each)   |
| 9    | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 20 (~72.2 GiB each)   |
| 10   | B00BA            | 1.4 TiB    | 1.4 TiB (100.00%)   | 16 (~86.9 GiB each)   |
| 11   | MTBB             | 1.3 TiB    | 1.1 TiB (83.73%)    | 82 (~15.9 GiB each)   |
| 12   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 3 (~425.3 GiB each)   |
| 13   | NOGRP            | 1.2 TiB    | 805.4 GiB (63.40%)  | 15 (~84.7 GiB each)   |
| 14   | SubsPlease       | 1.1 TiB    | 202.5 GiB (18.65%)  | 67 (~16.2 GiB each)   |
| 15   | YURI             | 895.6 GiB  | 454.2 GiB (50.71%)  | 76 (~11.8 GiB each)   |
| 16   | smol             | 890.6 GiB  | 857.6 GiB (96.29%)  | 60 (~14.8 GiB each)   |
| 17   | LYS1TH3A         | 887.5 GiB  | 868.0 GiB (97.80%)  | 36 (~24.7 GiB each)   |
| 18   | KH               | 793.5 GiB  | 290.9 GiB (36.66%)  | 47 (~16.9 GiB each)   |
| 19   | Arid             | 785.1 GiB  | 225.6 GiB (28.73%)  | 44 (~17.8 GiB each)   |
| 20   | LostYears        | 775.4 GiB  | 328.1 GiB (42.32%)  | 71 (~10.9 GiB each)   |
| 21   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 16 (~47.1 GiB each)   |
| 22   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 23   | Holomux          | 731.4 GiB  | 154.4 GiB (21.11%)  | 27 (~27.1 GiB each)   |
| 24   | Vodes            | 687.5 GiB  | 367.7 GiB (53.49%)  | 17 (~40.4 GiB each)   |
| 25   | Lulu             | 678.0 GiB  | 446.4 GiB (65.83%)  | 28 (~24.2 GiB each)   |
| 26   | PMR              | 666.6 GiB  | 666.6 GiB (100.00%) | 9 (~74.1 GiB each)    |
| 27   | Drag             | 655.7 GiB  | 164.5 GiB (25.09%)  | 55 (~11.9 GiB each)   |
| 28   | Meakes           | 624.4 GiB  | 624.4 GiB (100.00%) | 8 (~78.0 GiB each)    |
| 29   | Bunny-Apocalypse | 620.2 GiB  | 173.8 GiB (28.02%)  | 30 (~20.7 GiB each)   |
| 30   | Okay-Subs        | 594.4 GiB  | 559.7 GiB (94.16%)  | 26 (~22.9 GiB each)   |
| 31   | Flugel           | 587.0 GiB  | 587.0 GiB (100.00%) | 17 (~34.5 GiB each)   |
| 32   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 33   | UDF              | 569.1 GiB  | 211.4 GiB (37.15%)  | 22 (~25.9 GiB each)   |
| 34   | Reza             | 540.1 GiB  | 193.7 GiB (35.87%)  | 22 (~24.6 GiB each)   |
| 35   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 36   | koala            | 534.3 GiB  | 534.3 GiB (100.00%) | 15 (~35.6 GiB each)   |
| 37   | hydes            | 515.4 GiB  | 515.4 GiB (100.00%) | 13 (~39.6 GiB each)   |
| 38   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)   |
| 39   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 4 (~124.2 GiB each)   |
| 40   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 41   | Almighty         | 491.4 GiB  | 0 B (0.00%)         | 12 (~41.0 GiB each)   |
| 42   | IK               | 479.8 GiB  | 256.7 GiB (53.50%)  | 13 (~36.9 GiB each)   |
| 43   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 44   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 31 (~15.2 GiB each)   |
| 45   | RUDY             | 462.9 GiB  | 426.8 GiB (92.20%)  | 5 (~92.6 GiB each)    |
| 46   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 17 (~27.1 GiB each)   |
| 47   | FraMeSToR        | 456.6 GiB  | 456.6 GiB (100.00%) | 9 (~50.7 GiB each)    |
| 48   | OZR              | 451.8 GiB  | 292.7 GiB (64.78%)  | 15 (~30.1 GiB each)   |
| 49   | A&C              | 401.6 GiB  | 375.0 GiB (93.37%)  | 2 (~200.8 GiB each)   |
| 50   | Others           | 26.9 TiB   | 15.2 TiB (56.62%)   | 1427 (~19.3 GiB each) |
