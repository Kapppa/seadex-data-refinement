# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent from the same group, only the former is considered; otherwise, all torrents are considered. The `total_entries` metric counts how many times a group appears across entries, with each group counted up to twice per entry—once for best torrents and once for alt torrents. This avoids skewing results from entries with multiple torrents (e.g., a single entry with 12 torrents counts as one for `total_entries`). Exact duplicates are also discarded.

## Overview

- Total size: `93.7 TiB`
- Best size: `68.3 TiB`
- Alt size: `25.4 TiB`
- Realistic size: `72.8 TiB`

The `Realistic size` stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, falling back to the best single audio release if that's not present, and again falling back to whatever is available if neither exists.


## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Entries         |
| :----| :----------------| :----------| :-------------------| :---------------------|
| 1    | -ZR-             | 14.5 TiB   | 12.1 TiB (83.50%)   | 187 (~79.6 GiB each)  |
| 2    | NAN0             | 4.2 TiB    | 4.1 TiB (98.21%)    | 62 (~69.6 GiB each)   |
| 3    | CRUCiBLE         | 4.1 TiB    | 4.1 TiB (100.00%)   | 52 (~81.0 GiB each)   |
| 4    | sam              | 3.7 TiB    | 3.4 TiB (90.32%)    | 131 (~29.1 GiB each)  |
| 5    | TTGA             | 2.5 TiB    | 2.3 TiB (91.77%)    | 34 (~74.8 GiB each)   |
| 6    | hchcsen          | 2.2 TiB    | 1.5 TiB (69.25%)    | 55 (~40.2 GiB each)   |
| 7    | Moxie            | 2.1 TiB    | 2.1 TiB (100.00%)   | 47 (~45.5 GiB each)   |
| 8    | JySzE            | 1.7 TiB    | 1.7 TiB (100.00%)   | 8 (~220.8 GiB each)   |
| 9    | B00BA            | 1.6 TiB    | 1.6 TiB (100.00%)   | 19 (~87.7 GiB each)   |
| 10   | LazyRemux        | 1.4 TiB    | 1.4 TiB (100.00%)   | 19 (~76.0 GiB each)   |
| 11   | MTBB             | 1.3 TiB    | 1.1 TiB (83.73%)    | 86 (~15.2 GiB each)   |
| 12   | NOGRP            | 1.3 TiB    | 836.1 GiB (64.26%)  | 16 (~81.3 GiB each)   |
| 13   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 4 (~319.0 GiB each)   |
| 14   | SubsPlease       | 1.2 TiB    | 177.7 GiB (14.11%)  | 75 (~16.8 GiB each)   |
| 15   | PMR              | 1.1 TiB    | 1.1 TiB (100.00%)   | 14 (~80.0 GiB each)   |
| 16   | YURI             | 903.6 GiB  | 463.0 GiB (51.24%)  | 77 (~11.7 GiB each)   |
| 17   | smol             | 903.2 GiB  | 870.2 GiB (96.35%)  | 55 (~16.4 GiB each)   |
| 18   | LYS1TH3A         | 887.5 GiB  | 868.0 GiB (97.80%)  | 37 (~24.0 GiB each)   |
| 19   | LostYears        | 880.4 GiB  | 328.1 GiB (37.27%)  | 53 (~16.6 GiB each)   |
| 20   | KH               | 830.9 GiB  | 299.3 GiB (36.02%)  | 52 (~16.0 GiB each)   |
| 21   | Vodes            | 769.7 GiB  | 449.9 GiB (58.45%)  | 18 (~42.8 GiB each)   |
| 22   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 17 (~44.3 GiB each)   |
| 23   | Holomux          | 751.2 GiB  | 152.5 GiB (20.31%)  | 31 (~24.2 GiB each)   |
| 24   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)   |
| 25   | A&C              | 726.4 GiB  | 699.8 GiB (96.34%)  | 4 (~181.6 GiB each)   |
| 26   | Arid             | 718.6 GiB  | 225.6 GiB (31.39%)  | 46 (~15.6 GiB each)   |
| 27   | Bunny-Apocalypse | 692.4 GiB  | 173.8 GiB (25.10%)  | 32 (~21.6 GiB each)   |
| 28   | Lulu             | 678.0 GiB  | 401.0 GiB (59.15%)  | 34 (~19.9 GiB each)   |
| 29   | Drag             | 655.7 GiB  | 164.5 GiB (25.09%)  | 60 (~10.9 GiB each)   |
| 30   | RUDY             | 637.5 GiB  | 601.4 GiB (94.34%)  | 12 (~53.1 GiB each)   |
| 31   | Okay-Subs        | 635.7 GiB  | 601.0 GiB (94.54%)  | 31 (~20.5 GiB each)   |
| 32   | Meakes           | 624.4 GiB  | 624.4 GiB (100.00%) | 8 (~78.0 GiB each)    |
| 33   | Flugel           | 587.0 GiB  | 587.0 GiB (100.00%) | 19 (~30.9 GiB each)   |
| 34   | D4C              | 583.2 GiB  | 583.2 GiB (100.00%) | 3 (~194.4 GiB each)   |
| 35   | Reza             | 580.1 GiB  | 193.7 GiB (33.40%)  | 27 (~21.5 GiB each)   |
| 36   | UDF              | 561.4 GiB  | 203.8 GiB (36.29%)  | 23 (~24.4 GiB each)   |
| 37   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)   |
| 38   | koala            | 534.3 GiB  | 534.3 GiB (100.00%) | 12 (~44.5 GiB each)   |
| 39   | hydes            | 515.4 GiB  | 515.4 GiB (100.00%) | 13 (~39.6 GiB each)   |
| 40   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)   |
| 41   | VULCAN           | 499.2 GiB  | 439.1 GiB (87.97%)  | 6 (~83.2 GiB each)    |
| 42   | UltraRemux       | 496.7 GiB  | 496.7 GiB (100.00%) | 5 (~99.3 GiB each)    |
| 43   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)   |
| 44   | Almighty         | 491.4 GiB  | 0 B (0.00%)         | 2 (~245.7 GiB each)   |
| 45   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)    |
| 46   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 32 (~14.7 GiB each)   |
| 47   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 19 (~24.2 GiB each)   |
| 48   | FraMeSToR        | 456.6 GiB  | 456.6 GiB (100.00%) | 8 (~57.1 GiB each)    |
| 49   | OZR              | 451.8 GiB  | 292.7 GiB (64.78%)  | 15 (~30.1 GiB each)   |
| 50   | Others           | 28.5 TiB   | 15.9 TiB (55.73%)   | 1508 (~19.4 GiB each) |
