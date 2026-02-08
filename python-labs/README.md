# 🧪 Lab 01 — Ping + Latency Baseline (ICMP)

## 🎯 Objective

Measure baseline network reachability and latency using ICMP, and demonstrate how an automation script behaves in both healthy and failure scenarios.

This lab focuses on:
- Establishing what “normal” latency looks like
- Collecting repeatable measurements
- Handling network failure gracefully
- Producing both human-readable and machine-readable output

---

## 🧰 Environment

- **Host OS:** macOS
- **Shell:** zsh
- **Python Version:** Python 3.x
- **Editor:** Visual Studio Code
- **Execution Method:** Terminal

---

## 🛠️ Lab Overview

The lab was completed in four phases:

1. **Make** — Build a Python script to ping a target multiple times  
2. **Observe** — Collect latency measurements and calculate statistics  
3. **Break** — Intentionally test an unreachable target  
4. **Fix / Verify** — Confirm the script handles failure without crashing  

---

## 📦 Script Capabilities

The script performs the following:

- Pings a target IP address a fixed number of times
- Records total attempts, successes, and latency samples
- Calculates min / avg / max latency
- Writes structured output to a JSON file
- Continues running even when all pings fail

---

## ▶️ Healthy Baseline Run

### Description

The script was executed against a reachable public IP address (`1.1.1.1`) to establish a baseline.

### Evidence

📸 *Successful baseline run*

![Baseline Success](screenshots/Screenshot%202026-02-08%20at%2017.40.29.png)

📸 *Generated JSON output*

![Baseline JSON](screenshots/Screenshot%202026-02-08%20at%2017.45.22.jpeg)

---

## 💥 Controlled Failure Test

### Description

The target was intentionally changed to a non-responsive documentation IP (`203.0.113.1`) to simulate network failure.

### Evidence

📸 *Controlled failure run*

![Failure Run](screenshots/Screenshot%202026-02-08%20at%2018.29.14.png)

📸 *JSON output showing failure state*

![Failure JSON](screenshots/Screenshot%202026-02-08%20at%2018.37.47.png)

---

## 🔍 Additional Debug Output

📸 *Terminal output during execution*

![Terminal Output](screenshots/Screenshot%202026-02-08%20at%2018.44.01.png)

📸 *Summary statistics printed to terminal*

![Summary Output](screenshots/Screenshot%202026-02-08%20at%2018.45.19.png)

---

## 🧠 What I Misunderstood at First

Initially, I expected the script to throw errors when connectivity failed.  
Instead, I learned that **robust tooling treats failure as data**, not as an exception.

This shifted my understanding from:
- “Did it work or fail?”
to:
- “What signal did the system give me?”

---

## 🧠 Key Takeaways

- ICMP is useful for reachability and latency, but not application health
- A lack of errors does not mean a lack of failure
- Layer 3 failures can be observed without crashing applications
- JSON output enables offline analysis and historical comparison

---

## 🔄 Cleanup / Reset

No persistent system changes were made.  
The JSON output file can be safely deleted or regenerated.

---

## 🏁 Final Reflection

This lab reinforced that **observability and failure-handling matter more than success paths**.

The script did not just test the network — it tested how *I* reason about systems under failure.
