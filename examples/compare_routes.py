#!/usr/bin/env python3
"""PICUS Shadow Run offline route comparison. Synthetic data only."""
import json
import sys
from pathlib import Path


def all_in_cost(route):
    return float(route["explicit_fee_usd"]) + float(route["gas_usd"]) + float(route["slippage_cost_usd"])


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 examples/compare_routes.py examples/sample-routes.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    routes = data["routes"]
    print("PICUS SHADOW RUN — FINANCIAL ROUTING DEMO (SYNTHETIC)\n")
    print("Intent:", data["intent"])
    print("{:<18} {:>12} {:>12} {:>12} {:>12}".format("Route", "All-in USD", "Output USD", "Quote ms", "Simulation"))
    for r in routes:
        print("{:<18} {:>12.2f} {:>12.2f} {:>12d} {:>12}".format(
            r["name"], all_in_cost(r), float(r["expected_output_usd"]), int(r["quote_age_ms"]), r["simulation"].upper()))
    eligible = [r for r in routes if r["simulation"] == "pass"]
    if not eligible:
        print("\nNo recommendation: every candidate failed simulation.")
        return
    best = min(eligible, key=lambda r: (all_in_cost(r), -float(r["expected_output_usd"])))
    print("\nRecommended synthetic route:", best["name"])
    print("Reminder: sample numbers are invented and no live transaction was executed.")


if __name__ == "__main__":
    main()
