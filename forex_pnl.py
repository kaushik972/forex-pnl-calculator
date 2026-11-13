"""
Forex P&L Calculator
--------------------
Practice project. I have traded stocks and forex on my own for about
7 years, and I keep a journal of every trade. This script reads that
journal and summarises it: total P&L, win rate, best and worst trade,
and P&L by currency pair.

P&L here is in "points x lots" units from the journal (entry vs exit,
x lots, signed by side) — a simple practice calculation, not a broker
statement. Reads trades.csv (date, pair, side, entry, exit, lots).

Built by Shivam Kaushik while learning Python.
Standard library only (csv).
"""

import csv

TRADES_FILE = "trades.csv"


def load_trades(filename):
    rows = []
    with open(filename, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            entry, exit_ = float(row["entry"]), float(row["exit"])
            lots = float(row["lots"])
            direction = 1 if row["side"] == "long" else -1
            rows.append({
                "date": row["date"], "pair": row["pair"], "side": row["side"],
                "pnl": direction * (exit_ - entry) * lots * 10000,
            })
    return rows


def main():
    rows = load_trades(TRADES_FILE)
    wins = [r for r in rows if r["pnl"] > 0]
    losses = [r for r in rows if r["pnl"] < 0]
    total = sum(r["pnl"] for r in rows)

    print(f"Forex journal - {len(rows)} trades")
    print("-" * 52)
    print(f"Total P&L:   {total:,.0f} points x lots")
    print(f"Wins:        {len(wins)}  Losses: {len(losses)}")
    print(f"Win rate:    {len(wins) / len(rows):.1%}")
    print(f"Average win: {sum(r['pnl'] for r in wins) / len(wins):,.0f}")
    print(f"Average loss:{sum(r['pnl'] for r in losses) / len(losses):,.0f}")

    by_pair = {}
    for r in rows:
        p = by_pair.setdefault(r["pair"], {"trades": 0, "pnl": 0.0})
        p["trades"] += 1
        p["pnl"] += r["pnl"]

    print("\nBy pair:")
    print(f"{'Pair':<10}{'Trades':>8}{'P&L':>14}")
    for name, p in sorted(by_pair.items(), key=lambda i: i[1]["pnl"], reverse=True):
        print(f"{name:<10}{p['trades']:>8,}{p['pnl']:>14,.0f}")

    best = max(rows, key=lambda r: r["pnl"])
    worst = min(rows, key=lambda r: r["pnl"])
    print(f"\nBest trade:  {best['date']} {best['pair']} {best['side']} ({best['pnl']:,.0f})")
    print(f"Worst trade: {worst['date']} {worst['pair']} {worst['side']} ({worst['pnl']:,.0f})")


if __name__ == "__main__":
    main()
