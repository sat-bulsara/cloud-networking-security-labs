 # 🧪 Lab 01 — Ping + Latency Baseline (ICMP)

## 🎯 Objective

Measure baseline network reachability and latency using ICMP, and demonstrate how an automation script behaves in both healthy and failure scenarios.

This kind of baseline testing is useful when diagnosing user-reported ‘slow network’ issues or validating connectivity before deeper troubleshooting.

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

<img width="1147" height="246" alt="Screenshot 2026-02-08 at 17 40 29" src="https://github.com/user-attachments/assets/959d3d77-f1d6-4b06-8555-b6ee814fdb6f" />

📸 *Generated JSON output* 

<img width="3580" height="2196" alt="Screenshot 2026-02-08 at 17 45 22" src="https://github.com/user-attachments/assets/91c53328-8ace-4ed3-9f68-d27e328c93b2" />

---

## 💥 Controlled Failure Test

### Description

The target was intentionally changed to a non-responsive documentation IP (`203.0.113.1`) to simulate network failure.

### Evidence

📸 *Controlled failure run*

<img width="1207" height="694" alt="Screenshot 2026-02-08 at 18 29 14" src="https://github.com/user-attachments/assets/fb362916-aeba-4a44-97a7-d58052223848" />

📸 *JSON output showing failure state*

<img width="1332" height="766" alt="Screenshot 2026-02-08 at 18 37 47" src="https://github.com/user-attachments/assets/5ddfd571-375b-4bbc-9cf5-81d64336e35e" />

---

## 🔍 Additional Debug Output

📸 *Terminal output during execution*

<img width="1227" height="307" alt="Screenshot 2026-02-08 at 18 44 01" src="https://github.com/user-attachments/assets/2057e4f9-504f-4705-adc6-55e35b01551b" />

📸 *Summary statistics printed to terminal*

<img width="1382" height="771" alt="Screenshot 2026-02-08 at 18 45 19" src="https://github.com/user-attachments/assets/2e43e9b5-c75e-476f-a9d4-0e60108cd7cf" />

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
