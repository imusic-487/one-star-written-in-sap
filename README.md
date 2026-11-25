# One Star, Written in Sap

[![Competition](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![Rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/imusic-487/one-star-written-in-sap/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/leaderboard)
[![Reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/imusic-487/one-star-written-in-sap/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/leaderboard)

## The entry

> One star: bought for 'good energy,' shoved behind the TV, and my only sunlight is the glow of my owner's 3 a.m. doomscrolling. The fern got a window. I got Wi-Fi.

One line, 162 characters. The plant was bought as decor for "good energy"
and then parked behind the TV, so the only light it ever gets is the glow
of its owner's late-night phone. The punchline lands on the comparison:
the fern got a real window, this plant got Wi-Fi — light it can't use,
from a screen it can't escape.

## What this repo does

This is an entry for the make.fun bounty
[u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4).
`main.py` writes the entry — the one line above, exactly as written — to
`/output/entry.txt`, and fails loudly if the text is not 1–279 characters
or is only white space. Nothing else: no network, no randomness, no
timestamps, standard library only.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `main.py` — writes the entry to `/output/entry.txt` and checks the gate.
- `README.md` — this file.
- `LICENSE` — MIT license.
- `.makefun/owner.json` — the owner's payout wallet.
