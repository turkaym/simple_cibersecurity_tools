Security Tools

A **learning project** for practicing **cybersecurity with Python**. This repository holds small, documented scripts used to build foundations in security tooling: command-line interfaces, log analysis, safe use of system commands, and HTTP clients.

## Purpose

- **Learn by doing**: Use Python to build the kind of tools used in offensive security (recon, scanning) and defensive security (log analysis, automation).
- **Stage 1 focus**: Get comfortable with **argparse**, **file/log handling**, **subprocess**, and **HTTP requests** as building blocks for later stages (e.g. networking, web security, automation).

All scripts include docstrings and are intended for **authorized practice only** (your own systems or lab environments).

## Project structure

| Path | Purpose |
|------|--------|
| `scanner.py` | CLI template for a security scanner (target, port, timeout, output, verbose). |
| `stage1_tools/cli_tool.py` | Example CLI with argparse (target, port, timeout, output, verbose). |
| `stage1_tools/log_analyzer.py` | Analyzes a log file and lists IPs above a minimum request count. |
| `stage1_tools/run_comman.py` | Runs a system command safely (no shell) and prints exit code, stdout, stderr. |
| `stage1_tools/http_client.py` | Fetches a URL and prints status, headers, and a short body preview. |
| `stage1_tools/access.log` | Sample log file for testing the log analyzer. |

## Requirements

- **Python 3**
- **requests** (only for `http_client.py`):

  ```bash
  pip install requests
  ```

## How to run

From the project root:

```bash
# CLI tool (example)
python stage1_tools/cli_tool.py -t 127.0.0.1 -p 8080 -v

# Log analyzer (use your log file or the sample)
python stage1_tools/log_analyzer.py stage1_tools/access.log --min-hits 1

# Run a system command
python stage1_tools/run_comman.py ping google.com

# HTTP client
python stage1_tools/http_client.py https://httpbin.org/get

# Scanner template
python scanner.py -t 192.168.1.1 -p 80 -v
```

## Ethical use

Only use these tools on systems you own or have explicit permission to test. Unauthorized scanning or access is illegal.
