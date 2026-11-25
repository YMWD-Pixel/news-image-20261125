# World News — 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/YMWD-Pixel/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/YMWD-Pixel/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One image that sums up the world's news of Wednesday, 25 November 2026.

## The image

`entry.png` (1024×1024, 124 KB) is a newspaper front page:

- **Lead — Strait of Hormuz:** two oil tankers hit naval mines and caught fire.
- **01 Ukraine:** drones hit two Russian refineries; a Russian warship was sunk off Libya.
- **02 Saudi Arabia:** Houthi strikes on the Ras Tanura refinery and a Riyadh tower, injuring 11.
- **03 United States:** a US jury convicted Huawei of bank fraud and stealing trade secrets.
- **04 Markets:** Asian stocks plunged (KOSPI −6.2%, Nikkei −2.8%) while the Dow closed above 50,000.
- **05 Space & Pacific:** Shenzhou-24 docked with Tiangong; Australia signed a security treaty with Solomon Islands.
- **06 Climate:** COP31 talks ended without a deal.

The stories were checked against news reports published on 25 November 2026
(Just Security Early Edition, Open Chronicle, Principia, and others).

## The program

`main.ts` (Node 22, standard library only) copies `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It makes no
network calls. The image was drawn locally with Python/PIL
(`draw_image.py`, kept in the repository for reference) before submission.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## License

MIT. See `LICENSE`.
