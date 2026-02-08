import json
import sys
import statistics
import subprocess
import re
"""
Lab 01 — Ping & Latency Baseline (ICMP)

Purpose:
- Measure ICMP reachability and latency
- Treat failure as data, not an exception
- Produce both human-readable and JSON output

This script intentionally avoids crashing on network failure.

# LAB 01 — Ping + Latency Baseline (ICMP)
#
# 1. Inputs:
#    - A list of network targets (IP addresses or hostnames)
#    - A ping count (number of attempts per target)
#
# 2. Outputs:
#    - A JSON file (outputs/baseline.json) containing per-target ping statistics
#    - A readable summary printed to stdout
#
# 3. Success:
#    - Targets are reachable with a high success rate
#    - Latency values (min/avg/max) are recorded for successful pings
#
# 4. Failure:
#    - Failed pings are recorded without latency
#    - The script continues running and does not crash on errors
"""


TIME_RE = re.compile(r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms")
PING_COUNT = 5


def ping_once(target: str) -> tuple[bool, float | None]:
    result = subprocess.run(
        ["ping", "-c", "1", target],
        capture_output=True,
        text=True,
    )

    ok = (result.returncode == 0)

    match = TIME_RE.search(result.stdout)
    latency_ms = float(match.group(1)) if match else None

    return ok, latency_ms


def main() -> int:
    latencies: list[float] = []
    successes = 0
    target = sys.argv[1] if len(sys.argv) > 1 else "203.0.113.1"

    for i in range(PING_COUNT):
        ok, latency_ms = ping_once(target)

        if ok and latency_ms is not None:
            successes += 1
            latencies.append(latency_ms)

        print(f"Attempt {i+1}: ok={ok}, latency={latency_ms}")

    print("\nSummary:")
    print("Attempts:", PING_COUNT)
    print("Successes:", successes)
    print("Latencies:", latencies)

    if latencies:
        min_latency = min(latencies)
        avg_latency = statistics.mean(latencies)
        max_latency = max(latencies)
    else:
        min_latency = avg_latency = max_latency = None

    print("\nLatency statistics (ms):")
    print("Min:", min_latency)
    print("Avg:", avg_latency)
    print("Max:", max_latency)

    results = {
        "target": target,
        "attempts": PING_COUNT,
        "successes": successes,
        "success_rate": successes / PING_COUNT if PING_COUNT else 0,
        "latency_ms": {
            "min": min_latency,
            "avg": avg_latency,
            "max": max_latency,
            "samples": latencies,
        },
    }

    with open("outputs/baseline.json", "w") as f:
        json.dump(results, f, indent=2)

    print("\nBaseline written to outputs/baseline.json")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
