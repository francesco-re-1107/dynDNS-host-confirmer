# dynDNS-host-confirmer
This bot automatically confirms free dynDNS host.

## Usage
 1. Install [Python 3](https://www.python.org/downloads/)
 2. Install [selenium](https://pypi.org/project/selenium/) using `pip install selenium`
 3. Install [schedule](https://pypi.org/project/schedule/) using `pip install schedule`
 4. Download the correct WebDriver for your browser [from here](https://selenium-python.readthedocs.io/installation.html#drivers)
 5. Download `bot.py` from this repository and run it with `python bot.py username password`, it will confirm the host every 15 days.

## Warning
This script does **not** update the ip when it changes, instead this script can be used to confirm the host of the free account.

## Tip
Use [DuckDNS](https://www.duckdns.org) instead of dynDNS, which gives you 5 free dynamic domains hosted on AWS that don't require payments or confirmations.
