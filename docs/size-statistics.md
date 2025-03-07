# Size Statistics

These statistics are NOT 100% accurate, but they likely are as realistic as (reasonably) possible.

The definition of an entry (or a "complete" torrent) is quite murky. SeaDex defines it as an AniList entry, but every private tracker has their own definition (typically, they follow AniDB or TVDB), while Nyaa does not enforce a specific definition. Every release can quite possibly have slightly different torrents across trackers, or a single torrent on Nyaa can include several SeaDex entries. A Nyaa torrent might contain an entire franchise, but only a single file out of it might be relevant.

All of this and more means that we need to settle on a method to calculate these statistics. This was essentially calculated by iterating over every SeaDex entry, and if an entry has both private tracker torrent and public torrent, only the former is considered; otherwise, all torrents are considered. Exact duplicates are also discarded.

## Overview

- Total size: 78.9 TiB
- Best size: 56.8 TiB
- Alt size: 22.1 TiB
- Realistic size: 64.2 TiB

The realistic size stat tries to emulate a scenario where a user will likely download the best dual audio release for an entry, fallback to the best single audio release if that's not present, and again fallback to whatever there is if neither exist.

## Breakdown by Group

| Rank | Group            | Total Size | Best Size           | Total Torrents       |
| :----| :----------------| :----------| :-------------------| :--------------------|
| 1    | -ZR-             | 13.8 TiB   | 11.6 TiB (84.06%)   | 175 (~80.6 GiB each) |
| 2    | sam              | 3.6 TiB    | 3.3 TiB (90.06%)    | 128 (~29.0 GiB each) |
| 3    | NAN0             | 3.4 TiB    | 3.3 TiB (97.78%)    | 49 (~71.0 GiB each)  |
| 4    | hchcsen          | 2.0 TiB    | 1.4 TiB (69.20%)    | 50 (~41.9 GiB each)  |
| 5    | CRUCiBLE         | 2.0 TiB    | 2.0 TiB (100.00%)   | 25 (~82.3 GiB each)  |
| 6    | Moxie            | 2.0 TiB    | 2.0 TiB (100.00%)   | 39 (~52.2 GiB each)  |
| 7    | TTGA             | 1.8 TiB    | 1.6 TiB (88.87%)    | 25 (~75.2 GiB each)  |
| 8    | JySzE            | 1.8 TiB    | 1.8 TiB (100.00%)   | 6 (~308.0 GiB each)  |
| 9    | B00BA            | 1.4 TiB    | 1.4 TiB (100.00%)   | 16 (~86.9 GiB each)  |
| 10   | MTBB             | 1.3 TiB    | 1.1 TiB (83.74%)    | 80 (~16.2 GiB each)  |
| 11   | iKaos            | 1.2 TiB    | 898.5 GiB (70.42%)  | 3 (~425.3 GiB each)  |
| 12   | LazyRemux        | 1.2 TiB    | 1.2 TiB (100.00%)   | 16 (~78.9 GiB each)  |
| 13   | NOGRP            | 1.2 TiB    | 726.5 GiB (60.97%)  | 14 (~85.1 GiB each)  |
| 14   | SubsPlease       | 1.0 TiB    | 202.5 GiB (19.08%)  | 65 (~16.3 GiB each)  |
| 15   | smol             | 890.6 GiB  | 857.6 GiB (96.29%)  | 60 (~14.8 GiB each)  |
| 16   | YURI             | 888.6 GiB  | 447.2 GiB (50.33%)  | 75 (~11.8 GiB each)  |
| 17   | KH               | 773.4 GiB  | 290.9 GiB (37.61%)  | 46 (~16.8 GiB each)  |
| 18   | ZeroBuild        | 753.7 GiB  | 656.9 GiB (87.16%)  | 16 (~47.1 GiB each)  |
| 19   | SoM              | 732.1 GiB  | 732.1 GiB (100.00%) | 2 (~366.1 GiB each)  |
| 20   | Holomux          | 731.4 GiB  | 154.4 GiB (21.11%)  | 27 (~27.1 GiB each)  |
| 21   | LostYears        | 699.6 GiB  | 320.5 GiB (45.81%)  | 55 (~12.7 GiB each)  |
| 22   | Vodes            | 687.5 GiB  | 367.7 GiB (53.49%)  | 17 (~40.4 GiB each)  |
| 23   | Lulu             | 661.5 GiB  | 429.8 GiB (64.98%)  | 27 (~24.5 GiB each)  |
| 24   | Arid             | 646.0 GiB  | 206.7 GiB (31.99%)  | 41 (~15.8 GiB each)  |
| 25   | Drag             | 635.4 GiB  | 164.5 GiB (25.89%)  | 53 (~12.0 GiB each)  |
| 26   | Meakes           | 624.4 GiB  | 624.4 GiB (100.00%) | 8 (~78.0 GiB each)   |
| 27   | Bunny-Apocalypse | 620.2 GiB  | 173.8 GiB (28.02%)  | 30 (~20.7 GiB each)  |
| 28   | LYS1TH3A         | 606.9 GiB  | 587.4 GiB (96.79%)  | 33 (~18.4 GiB each)  |
| 29   | D4C              | 556.0 GiB  | 556.0 GiB (100.00%) | 2 (~278.0 GiB each)  |
| 30   | Reza             | 540.1 GiB  | 193.7 GiB (35.87%)  | 22 (~24.6 GiB each)  |
| 31   | BBT-RMX          | 539.2 GiB  | 374.5 GiB (69.44%)  | 11 (~49.0 GiB each)  |
| 32   | hydes            | 515.4 GiB  | 515.4 GiB (100.00%) | 13 (~39.6 GiB each)  |
| 33   | CTR              | 507.1 GiB  | 135.3 GiB (26.67%)  | 26 (~19.5 GiB each)  |
| 34   | SCY              | 495.6 GiB  | 185.4 GiB (37.42%)  | 28 (~17.7 GiB each)  |
| 35   | Okay-Subs        | 493.6 GiB  | 458.8 GiB (92.96%)  | 25 (~19.7 GiB each)  |
| 36   | koala            | 491.7 GiB  | 491.7 GiB (100.00%) | 13 (~37.8 GiB each)  |
| 37   | IK               | 479.8 GiB  | 256.7 GiB (53.50%)  | 13 (~36.9 GiB each)  |
| 38   | Doc              | 473.9 GiB  | 473.9 GiB (100.00%) | 5 (~94.8 GiB each)   |
| 39   | Kametsu          | 470.3 GiB  | 133.1 GiB (28.31%)  | 31 (~15.2 GiB each)  |
| 40   | CBT              | 460.7 GiB  | 379.9 GiB (82.46%)  | 17 (~27.1 GiB each)  |
| 41   | FraMeSToR        | 456.6 GiB  | 456.6 GiB (100.00%) | 9 (~50.7 GiB each)   |
| 42   | UDF              | 454.9 GiB  | 191.5 GiB (42.10%)  | 20 (~22.7 GiB each)  |
| 43   | OZR              | 426.7 GiB  | 292.7 GiB (68.58%)  | 14 (~30.5 GiB each)  |
| 44   | FLE              | 364.9 GiB  | 345.0 GiB (94.57%)  | 9 (~40.5 GiB each)   |
| 45   | VULCAN           | 360.8 GiB  | 360.8 GiB (100.00%) | 3 (~120.3 GiB each)  |
| 46   | Pog42            | 347.5 GiB  | 188.4 GiB (54.20%)  | 25 (~13.9 GiB each)  |
| 47   | NH               | 342.2 GiB  | 85.5 GiB (24.99%)   | 19 (~18.0 GiB each)  |
| 48   | Flugel           | 328.0 GiB  | 328.0 GiB (100.00%) | 9 (~36.4 GiB each)   |
| 49   | YURASUKA         | 325.3 GiB  | 15.4 GiB (4.72%)    | 31 (~10.5 GiB each)  |
| 50   | BiRJU            | 324.0 GiB  | 324.0 GiB (100.00%) | 4 (~81.0 GiB each)   |
| 51   | inid4c           | 321.5 GiB  | 0 B (0.00%)         | 6 (~53.6 GiB each)   |
| 52   | mofobunny        | 312.6 GiB  | 312.6 GiB (100.00%) | 1 (~312.6 GiB each)  |
| 53   | Aergia           | 304.3 GiB  | 304.3 GiB (100.00%) | 4 (~76.1 GiB each)   |
| 54   | EXP              | 278.9 GiB  | 152.4 GiB (54.67%)  | 18 (~15.5 GiB each)  |
| 55   | Datte13          | 275.7 GiB  | 96.6 GiB (35.06%)   | 11 (~25.1 GiB each)  |
| 56   | Mysteria         | 271.3 GiB  | 175.9 GiB (64.84%)  | 18 (~15.1 GiB each)  |
| 57   | Pizza            | 268.4 GiB  | 197.9 GiB (73.74%)  | 7 (~38.3 GiB each)   |
| 58   | Legion           | 239.4 GiB  | 155.6 GiB (64.98%)  | 8 (~29.9 GiB each)   |
| 59   | HorribleSubs     | 237.0 GiB  | 27.4 GiB (11.55%)   | 13 (~18.2 GiB each)  |
| 60   | fig              | 235.5 GiB  | 235.5 GiB (100.00%) | 6 (~39.2 GiB each)   |
| 61   | Netaro           | 222.5 GiB  | 197.3 GiB (88.65%)  | 7 (~31.8 GiB each)   |
| 62   | ANE              | 220.9 GiB  | 120.3 GiB (54.48%)  | 11 (~20.1 GiB each)  |
| 63   | UQW              | 220.1 GiB  | 27.2 GiB (12.36%)   | 2 (~110.1 GiB each)  |
| 64   | Commie           | 213.6 GiB  | 0 B (0.00%)         | 30 (~7.1 GiB each)   |
| 65   | FFF              | 212.0 GiB  | 0 B (0.00%)         | 10 (~21.2 GiB each)  |
| 66   | Virtuality       | 205.2 GiB  | 166.6 GiB (81.20%)  | 4 (~51.3 GiB each)   |
| 67   | ASC              | 202.8 GiB  | 143.8 GiB (70.92%)  | 12 (~16.9 GiB each)  |
| 68   | Iznjie Biznjie   | 200.3 GiB  | 132.8 GiB (66.27%)  | 10 (~20.0 GiB each)  |
| 69   | Asakura          | 195.8 GiB  | 25.5 GiB (13.03%)   | 11 (~17.8 GiB each)  |
| 70   | FateSucks        | 190.1 GiB  | 190.1 GiB (100.00%) | 4 (~47.5 GiB each)   |
| 71   | o7               | 185.3 GiB  | 56.0 GiB (30.25%)   | 13 (~14.3 GiB each)  |
| 72   | Hark0n           | 179.4 GiB  | 83.0 GiB (46.30%)   | 3 (~59.8 GiB each)   |
| 73   | PMR              | 177.7 GiB  | 177.7 GiB (100.00%) | 3 (~59.2 GiB each)   |
| 74   | AC               | 177.4 GiB  | 0 B (0.00%)         | 6 (~29.6 GiB each)   |
| 75   | CiNEPHiLES       | 176.6 GiB  | 152.3 GiB (86.21%)  | 4 (~44.2 GiB each)   |
| 76   | aRMX             | 171.7 GiB  | 171.7 GiB (100.00%) | 3 (~57.2 GiB each)   |
| 77   | GSK_kun          | 168.8 GiB  | 20.4 GiB (12.08%)   | 12 (~14.1 GiB each)  |
| 78   | CyC              | 166.8 GiB  | 17.5 GiB (10.49%)   | 15 (~11.1 GiB each)  |
| 79   | Gambler          | 159.0 GiB  | 159.0 GiB (100.00%) | 2 (~79.5 GiB each)   |
| 80   | Lisata598        | 155.6 GiB  | 155.6 GiB (100.00%) | 1 (~155.6 GiB each)  |
| 81   | Kinomoto         | 154.3 GiB  | 154.3 GiB (100.00%) | 1 (~154.3 GiB each)  |
| 82   | VALKYRiE         | 154.0 GiB  | 154.0 GiB (100.00%) | 2 (~77.0 GiB each)   |
| 83   | Senjou           | 151.9 GiB  | 14.3 GiB (9.45%)    | 4 (~38.0 GiB each)   |
| 84   | karios           | 149.5 GiB  | 61.9 GiB (41.39%)   | 6 (~24.9 GiB each)   |
| 85   | BMF              | 147.3 GiB  | 147.3 GiB (100.00%) | 1 (~147.3 GiB each)  |
| 86   | Headpatter       | 140.6 GiB  | 140.6 GiB (100.00%) | 1 (~140.6 GiB each)  |
| 87   | eldon            | 139.4 GiB  | 139.4 GiB (100.00%) | 4 (~34.9 GiB each)   |
| 88   | Foxtrot          | 136.8 GiB  | 116.3 GiB (85.03%)  | 4 (~34.2 GiB each)   |
| 89   | MK               | 135.7 GiB  | 70.2 GiB (51.74%)   | 9 (~15.1 GiB each)   |
| 90   | Rasetsu          | 135.2 GiB  | 19.7 GiB (14.56%)   | 8 (~16.9 GiB each)   |
| 91   | ABdex            | 134.8 GiB  | 134.8 GiB (100.00%) | 3 (~44.9 GiB each)   |
| 92   | cappybara        | 134.4 GiB  | 108.8 GiB (80.94%)  | 6 (~22.4 GiB each)   |
| 93   | derp             | 128.7 GiB  | 104.9 GiB (81.51%)  | 6 (~21.4 GiB each)   |
| 94   | ShadyCrab        | 126.7 GiB  | 26.5 GiB (20.89%)   | 5 (~25.3 GiB each)   |
| 95   | P9               | 123.6 GiB  | 123.6 GiB (100.00%) | 8 (~15.4 GiB each)   |
| 96   | Baws             | 121.4 GiB  | 48.6 GiB (40.08%)   | 8 (~15.2 GiB each)   |
| 97   | Dekinai          | 121.1 GiB  | 11.8 GiB (9.76%)    | 5 (~24.2 GiB each)   |
| 98   | Dragon-Releases  | 120.7 GiB  | 0 B (0.00%)         | 5 (~24.1 GiB each)   |
| 99   | Lv.99 Villain    | 118.7 GiB  | 118.7 GiB (100.00%) | 1 (~118.7 GiB each)  |
| 100  | Others           | 12.9 TiB   | 6.7 TiB (51.43%)    | 843 (~15.7 GiB each) |
