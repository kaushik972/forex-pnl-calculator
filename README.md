# Forex P&L Calculator

A small journal summary for forex trades: total P&L, win rate, average win vs average loss, and P&L by currency pair.

## Why I built this

I have traded stocks and forex on my own for about 7 years, and I keep a journal of every trade. The question I actually care about after a month is not "did I win?" but "is my average win bigger than my average loss, and which pair is doing the work?" — this script answers that from the journal CSV.

## What it does

Reads `trades.csv` (date, pair, side, entry, exit, lots — 12 sample trades, Oct 2026) and prints:

- Total P&L, wins/losses, and win rate
- Average win and average loss
- P&L by currency pair, and the best and worst single trades

P&L is in "points x lots" units from the journal — a simple practice calculation, not a broker statement.

## How to run

```bash
cd forex-pnl-calculator
python forex_pnl.py
```

Point it at your own journal by replacing `trades.csv` (keep the same columns).

## Sample output

```
Forex journal - 12 trades
----------------------------------------------------
Total P&L:   2,422 points x lots
Wins:        9  Losses: 3
Win rate:    75.0%
Average win: 319
Average loss:-151

By pair:
Pair        Trades           P&L
USDJPY           6         2,400
EURUSD           3            14
GBPUSD           3             7

Best trade:  2026-10-02 USDJPY long (900)
Worst trade: 2026-10-17 USDJPY long (-300)
```

(Data is sample data created for practice.)

## Files

- `forex_pnl.py` — the program
- `trades.csv` — sample trades (12 rows, Oct 2026)

## Next steps

- Add a monthly P&L trend, like the sales project has
- Track the longest winning and losing streaks
- Add position-size math so a trade's risk is visible before entry

*Standard library only for now. Built while learning Python.*
