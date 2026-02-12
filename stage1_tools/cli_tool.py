"""Command-line example tool for security-focused practice using argparse.

This module defines a simple CLI that accepts a target, port, timeout,
optional output file, and a verbosity flag. It is intended as a template
for building more advanced security tools such as scanners or checkers.
"""

import argparse

def main():
    """Parse command-line arguments and display the chosen configuration.

    This function defines the CLI interface, parses user-provided options,
    and prints the resulting configuration. In a real security tool,
    this is where you would pass the parsed arguments to the core logic
    (e.g., a scanner, checker, or report generator).
    """
    parser = argparse.ArgumentParser(description="Example Security CLI tool")

    parser.add_argument(
        "-t", "--target",
        required=True,
        help="Target IP or hostname"
    )

    parser.add_argument(
        "-p", "--port",
        type=int,
        default=80,
        help="Target port (default: 80)"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Connection timeout in seconds"
    )

    parser.add_argument(
        "-o", "--output",
        required=False,
        help="Output file for results"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    if args.verbose:
        print(f"[+] Target: {args.target}")
        print(f"[+] Port: {args.port}")
        print(f"[+] Timeout: {args.timeout}")
        if args.output:
            print(f"[+] Output file: {args.output}")
    else:
        print(args.target)

if __name__ == "__main__":
    main()
