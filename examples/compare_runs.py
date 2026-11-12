#!/usr/bin/env python3
"""Offline PICUS trace comparison. Synthetic data only; no network or wallet calls."""
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 examples/compare_runs.py examples/sample-runs.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    gate = float(data["quality_gate"])
    candidates = data["candidates"]
    print("PICUS SHADOW RUN — OFFLINE DEMO (SYNTHETIC)\n")
    print("Workflow:", data["workflow"], "| Required quality:", gate)
    print("{:<23} {:>12} {:>14} {:>12} {:>8}".format("Candidate", "Cost USD", "Latency ms", "Quality", "Pass"))
    for c in candidates:
        print("{:<23} {:>12.3f} {:>14d} {:>12.2f} {:>8}".format(
            c["name"], c["total_cost_usd"], c["latency_ms"], c["quality_score"],
            "YES" if c["quality_score"] >= gate else "NO"))
    eligible = [c for c in candidates if c["quality_score"] >= gate]
    if not eligible:
        print("No recommendation: no candidate meets quality gate.")
    else:
        best = min(eligible, key=lambda c: (c["total_cost_usd"], c["latency_ms"]))
        print("\nLowest-cost eligible candidate:", best["name"])
        print("Reminder: invented sample measurements, not actual cost reductions.")


if __name__ == "__main__":
    main()
