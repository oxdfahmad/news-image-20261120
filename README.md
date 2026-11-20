# The World — 20 November 2026

[![news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/oxdfahmad/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/oxdfahmad/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120)

A newspaper front page summing up Friday 20 November 2026 in ten verified
stories, drawn as one 1024×1024 image. Every story below happened, or was
first reported, on 20 November 2026, checked against live reporting from
Reuters, BBC, The Hindu, Space.com, Marketscreener, Daily Baku, Dolcevia
and Mezha on the day itself. Nothing here is speculation.

## The ten stories

1. **USA–Iran (lead)** — Trump says there is no rush on Iran: the war
   decision is pushed to 2027; he will "see what happens" after Jan 1.
2. **Ukraine (lead)** — Four ballistic missiles hit Kyiv overnight; a
   projectile lands near the Dutch embassy, causing minor damage.
3. **Middle East** — Houthis claim strikes on four Saudi targets; Riyadh
   confirms a landmark building was damaged.
4. **Energy** — A tanker catches fire after hitting a mine east of the
   Strait of Hormuz; oil holds steady.
5. **Weather / India** — Cyclone Akvan: 300,000 people evacuated in
   Odisha ahead of landfall; 423 rescue teams deployed.
6. **Europe** — European leaders say they are ready for talks with Russia
   on ending the war in Ukraine.
7. **Italy** — A nationwide CGIL general strike brings buses and metros
   to a halt across the country.
8. **Gaming** — GTA VI sales pass The Odyssey's $1.8bn global run.
9. **Space** — NASA confirms Voyager 1 has passed one light-day from
   Earth, a first for any spacecraft.
10. **Space / Japan** — Engine trouble ends Hayabusa2's planned asteroid
    landing; JAXA scraps the touchdown.

Also in the ticker: COP31 closes today in Antalya; Taiwan moves to steady
its stock market; a migrant boat sinks off Senegal; Henry Nicholls' unbeaten
113 lifts New Zealand on day one in Wellington; the US Army detonates 68
barrels of unstable lead azide in Iowa.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) places the bundled
`entry.png` at `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`),
checking the PNG magic bytes and the 1 MiB size cap first. The image was
drawn with a small Python/PIL script kept outside this repository; the
entry itself is just the program plus the image.
