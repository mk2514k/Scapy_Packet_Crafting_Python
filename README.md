# Scapy Packet Crafting

A Python script that manually builds and sends ICMP, TCP SYN, and UDP packets using Scapy, with live capture in Wireshark.

---

## What the Script Does

Sends three packets to `127.0.0.1` (your own machine — no network needed):

1. An **ICMP Echo Request** — the same thing a ping sends
2. A **TCP SYN** packet to port 80 — the opening move of a TCP connection
3. A **UDP datagram** to port 9999 — connectionless, no handshake

Each packet is built by stacking Scapy layers using the `/` operator — IP header on the bottom, protocol header on top.

---

## What to Expect

Terminal output when the script runs:

```
ICMP Echo Request sent to 127.0.0.1
TCP SYN packet sent to 127.0.0.1 on port 80
UDP packet sent to 127.0.0.1 on port 9999
```

In Wireshark you'll see all three packets appear on the loopback interface. A `[RST, ACK]` will also show up after the TCP SYN — that's normal, it just means nothing is listening on port 80.

Use these filters to isolate each one:

| Filter | What it shows |
|---|---|
| `icmp` | ICMP Echo Request |
| `tcp.flags.syn == 1` | TCP SYN packet |
| `udp` | UDP datagram |

---

## How to Run It

> Scapy requires root privileges to send raw packets.

Open Wireshark and start capturing on the **Loopback: lo** interface first, then run:

```bash
sudo /usr/bin/python3 ScapyPacketCrafting.py
```

If you get `ModuleNotFoundError: No module named 'scapy'` when using sudo:

```bash
sudo pip install scapy --break-system-packages
```

---

## Files

| File | Description |
|---|---|
| `ScapyPacketCrafting.py` | Main script — builds and sends the three packets |
| `screenshots/` | allPackets, ICMP, TCP, UDP |
| `packetCapture.pcapng` | Wireshark document |
