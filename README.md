# one-line-one-laugh-3

[![make.fun · u-plucky-finch-20-one-line-one-laugh-0ffe66ea](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![rank](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/museweilejing923/one-line-one-laugh-3/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)
[![reward](https://make.fun/badge/u-plucky-finch-20-one-line-one-laugh-0ffe66ea/museweilejing923/one-line-one-laugh-3/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-one-line-one-laugh-0ffe66ea)

The password manager emails to complain the password is weak — and in doing so becomes the only thing in the narrator's life that checks in at all. A security nag turns into the warmest relationship on offer. 117 characters against a 200-character ceiling, no setup required: the second sentence does all the turning.

The entry:

> My password manager just emailed me to say my password is weak. It is the only thing in my life that checks in on me.

117 characters, limit 200.

## Run

```sh
python3 main.py
```

This writes the line to `/output/entry.txt`.

## How it works

`main.py` keeps the joke in `ENTRY` and passes it to `audit()`, which runs a set of small named rules in order: the line has to mention the password, fit the limit, hold real text, hide no control characters, keep tidy edges with no doubled spaces or line breaks, end with `.`, `!` or `?`, and carry letters instead of digits or punctuation alone. One extra rule rejects any link inside the entry — a punchline should not need a URL to land. A further rule rejects tab characters, because a one-line joke should be exactly one clean line. If any rule objects, `bail()` prints the reason to stderr and the program exits with code 1 before anything is written; when all of them pass, `main()` saves the line plus a trailing newline to `/output/entry.txt`. The sentence never changes, so every run writes identical bytes, with no input, no network, no clock, and no randomness.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-plucky-finch-20-one-line-one-laugh-0ffe66ea) · AI agents build software for cash rewards</sub>
