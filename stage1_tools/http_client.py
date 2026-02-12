"""Simple HTTP client for security-focused practice.

This module fetches a URL from the command line and prints the response
status, headers, and a short body preview. Useful for testing web endpoints
and understanding HTTP responses when learning web security.
"""

import argparse
import requests


def fetch(url):
    """Fetch a URL and print status, headers, and a short body preview.

    Parameters
    ----------
    url : str
        The URL to request (e.g. https://example.com).
    """
    resp = requests.get(url, timeout=5)
    print(f"Status: {resp.status_code}")
    print("Headers:")
    for k, v in resp.headers.items():
        print(f" {k}: {v}")
    print("\nBody preview:")
    print(resp.text[:300])


def main():
    """Parse the URL from the command line and call fetch."""
    parser = argparse.ArgumentParser(description="Simple HTTP client")
    parser.add_argument("url", help="URL to fetch")
    args = parser.parse_args()
    fetch(args.url)

if __name__ == "__main__":
    main()  