# Scan-Subnet

A simple Python project that scans a network to find hosts that respond to ICMP ping requests.

## Features
- Scans a given network.
- Uses ICMP packets to check hosts.
- Displays scanning progress.
- Lists hosts that respond.
- Displays a JANGOTRA banner in the terminal.

## Requirements
- Python 3

## How to Run

```bash
sudo python3 main.py 192.168.1.0 255.255.255.0
```

Replace the network address and netmask with the network you are authorized to scan.

## Example Output

```text
============================================================
       Scan the Network
============================================================
Scanning 1/254
Scanning 2/254
Scanning 3/254

Online Host1 = 192.168.1.1
Online Host2 = 192.168.1.5
```

*The output above is only an example. Actual results depend on your network.*

## Purpose

This project helps me learn Python, Scapy, ICMP packets, and basic network scanning.

## Disclaimer

This tool only identifies hosts that respond to ICMP Echo Requests. It does not actually block IP addresses. Use it only on networks you own or have permission to test.
