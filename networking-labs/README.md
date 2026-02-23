
# 🧪 LAB 0 — What Actually Happens When I Type `google.com`

> A structured Linux networking deep-dive following the lifecycle:
> **Make → Observe → Break → Explain → Fix → Verify**

---

# 🎯 Objective

To trace, capture, and explain — at the Linux OS and network stack level — what happens from the moment a user types:

    google.com

…to the moment a successful HTTPS connection is established.

This lab focuses strictly on:

- OS-level networking
- DNS resolution
- Routing decisions
- ARP behavior
- TCP handshake mechanics
- Packet flow visibility

No cloud abstractions.  
No application-layer debugging.  
Only Linux + Layer 3/4 mechanics.

---

# 🖥 Environment

- OS: Ubuntu (VM)
- Network Mode: (Specify: NAT / Bridged)
- Tools Used:
  - `ip`
  - `arp`
  - `dig`
  - `tcpdump`
  - `ss`
  - `resolvectl`

---

# 🔁 Lab Lifecycle

---

# 1️⃣ MAKE — Establish Baseline

## Commands Executed

    ip addr
    ip route
    resolvectl status
    arp -n

## Screenshot

![Baseline Network State](screenshots/00_lab0_initial_state.png)

## What This Proves

- Host has valid IP address
- Default route exists
- DNS server configured
- ARP table initial state known

---

# 2️⃣ OBSERVE — DNS Resolution

## Command

    dig google.com

## Screenshot

![DNS Resolution](screenshots/01_dns_resolution.png)

## What This Proves

- DNS server responding
- A records returned
- Query latency measured
- No resolution failure

---

# 3️⃣ OBSERVE — Routing Decision

## Command

    ip route get <resolved_google_ip>

## Screenshot

![Routing Decision](screenshots/02_routing_decision.png)

## What This Proves

- Outgoing interface selected
- Source IP chosen
- Gateway used for next hop

---

# 4️⃣ OBSERVE — ARP Resolution

## Command

    arp -n

## Screenshot

![ARP Table State](screenshots/03_arp_table.png)

## What This Proves

- Gateway MAC address learned
- Layer 2 resolution complete

---

# 5️⃣ OBSERVE — TCP Handshake

## Command

    sudo tcpdump -i <interface> host <resolved_google_ip> and port 443

## Screenshot

![TCP Handshake Capture](screenshots/04_tcp_handshake.png)

## What This Proves

- SYN sent
- SYN-ACK received
- ACK returned
- Three-way handshake completed

---

# 🔬 BREAK — Controlled Failure Injection

Choose one:

- Remove default route
- Block outbound DNS via firewall
- Flush ARP cache
- Change DNS server to invalid IP

## Screenshot — Break Applied

![Failure Applied](screenshots/05_failure_applied.png)

## Screenshot — Failure Observed

![Failure Observed](screenshots/06_failure_observed.png)

---

# 🧠 EXPLAIN — Failure Analysis

## Symptom

(Describe what failed — timeout? no route? DNS error?)

## Subsystem

(Network stack / Routing table / DNS resolver / ARP cache)

## Root Cause

(Exact misconfiguration introduced)

## Mechanism of Failure

Explain *why* the packet could not proceed:
- No next-hop
- No name resolution
- No Layer 2 mapping
- Connection reset
- No return traffic

---

# 🔧 FIX — Restore Proper State

Describe the corrective command used.

## Screenshot — Fix Applied

![Fix Applied](screenshots/07_fix_applied.png)

---

# ✅ VERIFY — Confirm Restoration

Re-run:

    dig google.com
    ip route get <ip>
    curl -I https://google.com

## Screenshot — Fix Verified

![Fix Verified](screenshots/08_fix_verified.png)

---

# 🏁 Outcome

After completing this lab, I can:

- Predict packet flow before execution
- Identify failure domains quickly
- Map symptoms to specific subsystems
- Explain DNS, routing, ARP, and TCP interactions
- Diagnose Linux network issues methodically

---

# 📂 Repository Structure

    /lab0-what-happens-when-i-type-google
        ├── README.md
        └── screenshots/
            ├── 00_lab0_initial_state.png
            ├── 01_dns_resolution.png
            ├── 02_routing_decision.png
            ├── 03_arp_table.png
            ├── 04_tcp_handshake.png
            ├── 05_failure_applied.png
            ├── 06_failure_observed.png
            ├── 07_fix_applied.png
            └── 08_fix_verified.png

