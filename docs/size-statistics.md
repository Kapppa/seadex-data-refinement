# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `97.3 TiB`
- Best size: `70.6 TiB`
- Alt size: `26.7 TiB`
- Realistic size: `75.5 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.7 TiB   | 12.3 TiB (83.84%)   | 189 (~79.8 GiB each)  |
| 2    | NAN0             | 4.5 TiB    | 4.4 TiB (98.31%)    | 65 (~70.2 GiB each)   |
| 3    | CRUCiBLE         | 4.4 TiB    | 4.4 TiB (100.00%)   | 56 (~79.9 GiB each)   |
| 4    | sam              | 3.8 TiB    | 3.4 TiB (90.49%)    | 132 (~29.4 GiB each)  |
| 5    | TTGA             | 2.6 TiB    | 2.3 TiB (92.00%)    | 35 (~74.7 GiB each)   |
| 6    | hchcsen          | 2.3 TiB    | 1.5 TiB (66.21%)    | 56 (~41.3 GiB each)   |
| 7    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 46 (~46.5 GiB each)   |
| 8    | B00BA            | 1.9 TiB    | 1.9 TiB (100.00%)   | 22 (~86.9 GiB each)   |
| 9    | JySzE            | 1.7 TiB    | 1.7 TiB (100.00%)   | 8 (~220.8 GiB each)   |
| 10   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 11   | NOGRP            | 1.3 TiB    | 836.1 GiB (61.25%)  | 19 (~71.8 GiB each)   |
| 12   | SubsPlease       | 1.3 TiB    | 206.8 GiB (15.43%)  | 79 (~17.0 GiB each)   |
| 13   | MTBB             | 1.3 TiB    | 1.1 TiB (83.73%)    | 86 (~15.2 GiB each)   |
| 14   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 15   | PMR              | 1.1 TiB    | 1.1 TiB (100.00%)   | 14 (~81.0 GiB each)   |
| 16   | RUDY             | 994.3 GiB  | 958.2 GiB (96.37%)  | 12 (~82.9 GiB each)   |
| 17   | YURI             | 903.6 GiB  | 463.0 GiB (51.24%)  | 77 (~11.7 GiB each)   |
| 18   | smol             | 903.2 GiB  | 870.2 GiB (96.35%)  | 55 (~16.4 GiB each)   |
| 19   | LYS1TH3A         | 887.5 GiB  | 868.0 GiB (97.80%)  | 37 (~24.0 GiB each)   |
| 20   | LostYears        | 866.5 GiB  | 311.7 GiB (35.98%)  | 52 (~16.7 GiB each)   |
| 21   | KH               | 853.8 GiB  | 322.3 GiB (37.74%)  | 53 (~16.1 GiB each)   |
| 22   | Arid             | 786.9 GiB  | 206.7 GiB (26.26%)  | 47 (~16.7 GiB each)   |
| 23   | Vodes            | 769.7 GiB  | 449.9 GiB (58.45%)  | 18 (~42.8 GiB each)   |
| 24   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 17 (~44.3 GiB each)   |
| 25   | Bunny-Apocalypse | 747.0 GiB  | 173.8 GiB (23.27%)  | 33 (~22.6 GiB each)   |
| 26   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 27   | A&C              | 726.4 GiB  | 699.8 GiB (96.34%)  | 4 (~181.6 GiB each)   |
| 28   | Holomux          | 726.3 GiB  | 152.5 GiB (21.00%)  | 30 (~24.2 GiB each)   |
| 29   | Lulu             | 678.0 GiB  | 401.0 GiB (59.15%)  | 34 (~19.9 GiB each)   |
| 30   | FraMeSToR        | 667.1 GiB  | 667.1 GiB (100.00%) | 9 (~74.1 GiB each)    |
| 31   | Drag             | 655.7 GiB  | 164.5 GiB (25.09%)  | 59 (~11.1 GiB each)   |
| 32   | Meakes           | 637.8 GiB  | 624.4 GiB (97.90%)  | 9 (~70.9 GiB each)    |
| 33   | Okay-Subs        | 635.7 GiB  | 601.0 GiB (94.54%)  | 31 (~20.5 GiB each)   |
| 34   | Flugel           | 587.0 GiB  | 587.0 GiB (100.00%) | 19 (~30.9 GiB each)   |
| 35   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 36   | Reza             | 580.1 GiB  | 193.7 GiB (33.40%)  | 27 (~21.5 GiB each)   |
| 37   | UDF              | 561.4 GiB  | 203.8 GiB (36.29%)  | 23 (~24.4 GiB each)   |
| 38   | koala            | 554.9 GiB  | 554.9 GiB (100.00%) | 13 (~42.7 GiB each)   |
| 39   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 40   | hydes            | 515.4 GiB  | 515.4 GiB (100.00%) | 13 (~39.6 GiB each)   |
| 41   | Almighty         | 507.8 GiB  | 0 B (0.00%)         | 3 (~169.3 GiB each)   |
| 42   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)   |
| 43   | VULCAN           | 499.2 GiB  | 439.1 GiB (87.97%)  | 6 (~83.2 GiB each)    |
| 44   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 5 (~99.3 GiB each)    |
| 45   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 46   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 47   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 32 (~14.7 GiB each)   |
| 48   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 49   | OZR              | 451.8 GiB  | 292.7 GiB (64.78%)  | 15 (~30.1 GiB each)   |
| 50   | Others           | 30.1 TiB   | 16.5 TiB (54.86%)   | 1552 (~19.8 GiB each) |
