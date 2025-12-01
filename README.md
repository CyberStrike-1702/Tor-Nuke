Tor Nuke – 8GB RAM Edition (2025)

████████╗ ██████╗ ██████╗      ███╗   ██╗██╗   ██╗██╗  ██╗███████╗
  ╚══██╔══╝██╔═══██╗██╔══██╗     ████╗  ██║██║   ██║██║  ██║██╔════╝
     ██║   ██║   ██║██████╔╝     ██╔██╗ ██║██║   ██║███████║█████╗  
     ██║   ██║   ██║██╔══██╗     ██║╚██╗██║██║   ██║██╔══██║██╔══╝  
     ██║   ╚██████╔╝██║  ██║     ██║ ╚████║╚██████╔╝██║  ██║███████╗
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

Low-level Layer 7 + keep-alive flood over Tor
Tested and perfected on AMD Ryzen 7 + 8 GB RAM Fedora

Features
- ~450 simultaneous Tor connections (perfectly stable on 8 GB RAM)
- Persistent keep-alive + massive random garbage headers
- Extremely low RAM usage (~1.4 GB peak)
- No ControlPort needed – works with normal Tor Browser / tor service
- Only one dependency: pysocks

Requirements
- Python 3.8 or higher
- Tor running on port 9050 (just open Tor Browser or run "tor")

Installation
pip install pysocks

Usage
1. Open tor-nuke.py and edit these lines:
   TARGET_HOST = "yourtarget.onion"   # raw .onion only, no http://
   TARGET_PORT = 80                   # or 443 if the site uses HTTPS

2. Run:
   python3 tor-nuke.py

3. Sit back. Most small/medium .onion sites go down in 3–15 minutes.

Tested & Working (2025)
- Fedora 41–43
- Ubuntu 24.04 LTS
- Windows 10/11 + Tor Browser
- Ryzen 5/7 + 8 GB RAM machines

Target dead. Mission accomplished.

Use responsibly. Burn only what deserves to burn.
