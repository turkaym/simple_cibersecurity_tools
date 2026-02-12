"""Run a system command safely from Python (Stage 1 security tooling practice).

This module runs a single command and its arguments via subprocess without
using the shell, then prints exit code, stdout, and stderr. Use only for
commands you trust (e.g. ping, netstat) on systems you are allowed to test.
"""

import argparse
import subprocess


def run_command(cmd_list):
    """Execute a command (as a list of strings) and print exit code, stdout, and stderr.

    Parameters
    ----------
    cmd_list : list of str
        The command and its arguments, e.g. ["ping", "google.com"].
    """
    result = subprocess.run(
        cmd_list,
        capture_output=True,
        text=True
    )
    print(f"Exit code: {result.returncode}")
    print("STDOUT:")
    print(result.stdout)    
    print("STDERR:")
    print(result.stderr)

def main():
    """Parse command and optional arguments from the CLI, then run the command."""
    parser = argparse.ArgumentParser(description="Run a system command safely")
    parser.add_argument("command", help="Command to run (e.g. ping)")
    parser.add_argument("args", nargs="*", help="Arguments for the command")
    parsed = parser.parse_args()

    cmd = [parsed.command] + parsed.args
    run_command(cmd)

if __name__ == "__main__":
    main()