"""Simple log analyzer for security-focused practice.

Reads a log file (e.g. web server access log), counts requests per IP,
and prints IPs that exceed a minimum hit threshold. Useful for spotting
brute-force attempts or noisy scanners.
"""

import argparse
from collections import Counter
from pathlib import Path


def analyze_log(path, min_hits):
    """Analyze a log file and print IPs with at least min_hits requests.

    Expects log lines where the first token is an IP address (e.g. Apache
    combined log format).

    Parameters
    ----------
    path : str
        Path to the log file.
    min_hits : int
        Minimum number of requests per IP to include in the output.
    """
    counter = Counter()
    p = Path(path)

    with p.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            parts = line.split()
            if not parts:
                continue
            ip = parts[0]
            counter[ip] += 1
    
    for ip, count in counter.most_common():
        if count >= min_hits:
            print(f"{ip}: {count} requests")

def main():
    """Parse CLI arguments and run the log analyzer."""
    parser = argparse.ArgumentParser(description="simple log analyzer")
    parser.add_argument("logfile", help="Path to log file")
    parser.add_argument("--min-hits", type=int, default=20, help="Minimun requests for IP to show")
    args = parser.parse_args()

    analyze_log(args.logfile, args.min_hits)

if __name__ == "__main__":
    main()