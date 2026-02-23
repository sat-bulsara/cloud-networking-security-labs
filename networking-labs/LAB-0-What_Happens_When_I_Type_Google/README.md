
# 🧪 LAB 0 — What Actually Happens When I Type `google.com`

> A structured Linux networking deep-dive following the lifecycle:
> **Make → Observe → Break → Explain → Fix → Verify**

---

# 🎯 Objective

To trace and explain — at the Linux OS and network stack level — what happens from the moment a user types:

    google.com

…to the moment a successful HTTPS connection is established.

This lab focuses strictly on:

- OS-level networking
- DNS resolution
- Routing decisions
- ARP behavior
- TCP handshake mechanics
- Firewall behavior (Layer 4 control)

No cloud abstractions.  
No application-layer debugging.  
Only Linux + Layer 3/4 mechanics.

---

# 🖥 Environment

- OS: Ubuntu 24.04 (VM)
- Network Mode: DHCP (NAT)
- Tools Used:
  - `ip`
  - `arp`
  - `nslookup` / `dig`
  - `tcpdump`
  - `curl`
  - `ufw`

---

# 🔁 Lab Lifecycle

---

# 1️⃣ BASELINE — Routing State Before Break

## Command

    ip route

## Screenshot

<img width="751" height="162" alt="10_lab0_route_break_before" src="https://github.com/user-attachments/assets/e12b16af-4691-4067-8e36-96ac63dbd878" />

## What This Proves

- Default route exists via 10.211.55.1
- Interface `enp0s5` has Layer 3 reachability
- System can forward traffic beyond local subnet

---

# 2️⃣ BREAK — Remove Default Route

## Command

    sudo ip route del default

## Failure Observed

    ping -c 3 1.1.1.1
    → Network is unreachable

## Screenshot

<img width="858" height="639" alt="11_lab0_route_break_failure" src="https://github.com/user-attachments/assets/7a41aa84-4927-423d-ab3a-1648b1a1c974" />

## Symptom

No external connectivity.

## Subsystem

Kernel routing table.

## Root Cause

Default route removed → no next-hop for non-local destinations.

## Mechanism

Packet lookup fails at routing decision stage.
No matching route → kernel drops packet immediately.

---

# 3️⃣ FIX — Restore Network

Network restored via DHCP renewal / NetworkManager restart.

## Screenshot

<img width="728" height="446" alt="12_lab0_route_fix_verified" src="https://github.com/user-attachments/assets/66c39f10-04c6-45e2-b29e-4b1107525544" />

## Verification

- Default route restored
- ICMP to 1.1.1.1 successful
- 0% packet loss observed

---

# 4️⃣ BREAK — Block HTTPS (Layer 4 Firewall Test)

## Command

    sudo ufw deny out 443/tcp

## Screenshot

<img width="988" height="276" alt="13_lab0_443_block_rule" src="https://github.com/user-attachments/assets/41a441ac-23a6-4c1c-b389-0559abff61e2" />

## What This Changes

- Outbound TCP 443 traffic explicitly denied
- DNS still works
- Routing still works
- TCP handshake should fail

---

# 5️⃣ FIX — Remove Firewall Rule

## Command

    sudo ufw delete 1

## Screenshot

<img width="1156" height="498" alt="15_lab0_443_unblock_verified" src="https://github.com/user-attachments/assets/17cfc8e7-d448-4263-af4a-24ddf98f9c9c" />

## Verification

    curl -I https://google.com

- HTTP response received
- TCP 3-way handshake succeeds
- Application headers returned

---

# 🧠 Failure Analysis Summary

### Routing Failure

Symptom:
Network unreachable.

Subsystem:
Kernel routing table.

Root Cause:
Default route removed.

Why It Failed:
No next-hop available for non-local traffic.

Verification:
Default route restored → ICMP succeeds.

---

### Firewall Failure

Symptom:
HTTPS requests fail.

Subsystem:
Netfilter (ufw).

Root Cause:
Explicit deny rule for outbound 443/tcp.

Why It Failed:
TCP SYN blocked before handshake completes.

Verification:
Rule removed → HTTPS response received.

---

# 🏁 Outcome

After completing this lab, I can:

- Predict packet flow before execution
- Identify where routing decisions occur
- Explain why removing a default route kills connectivity
- Explain how firewall rules interrupt TCP establishment
- Distinguish Layer 3 failure from Layer 4 failure
- Restore functionality methodically with verification

---

# 📂 Repository Structure

    /lab0-what-happens-when-i-type-google
        ├── README.md
        └── screenshots/
            ├── 10_lab0_route_break_before.png
            ├── 11_lab0_route_break_failure.png
            ├── 12_lab0_route_fix_verified.png
            ├── 13_lab0_443_block_rule.png
            └── 15_lab0_443_unblock_verified.png
