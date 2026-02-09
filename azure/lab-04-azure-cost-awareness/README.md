# 🟦 LAB 4 — Azure Cost Awareness (Stop vs Delete)

**Student:** Sat Bulsara  
**Platform:** Microsoft Azure  
**Tooling:** Azure CLI (macOS)  
**Region:** UK South  
**Final State:** £0 ongoing cost  

---

## 💼 Business Context (Why This Matters)

Unexpected cloud costs are one of the most common real-world failures in cloud environments.
This lab demonstrates **why teams get surprise Azure bills** and how engineers are expected to prevent them through disciplined resource lifecycle management.

Cost awareness is a **core production skill**, not a finance problem.

---

## 🎯 Lab Goal

Understand **what actually costs money in Azure** by creating billable resources *without deploying a VM*, observing cost persistence, and returning safely to a zero-cost state.

---

## 🧰 Environment

- **Azure Subscription:** Azure subscription 1  
- **Access Method:** Azure CLI  
- **Resource Group:** `rg-lab04-cost`  
- **Region:** `uksouth`  

📸 **Screenshot:** Azure account context  

<img width="1248" height="648" alt="00_lab04_account_context" src="https://github.com/user-attachments/assets/df7ec6c1-f50c-435c-a4a1-0f77c7e58c3b" />

---

## 1️⃣ Create a Cost-Controlled Resource Group

A dedicated resource group was created to act as a **cost blast radius**, allowing all resources to be removed in one operation.

📸 **Screenshot:** Resources listed after creation  

<img width="1219" height="295" alt="01_lab04_resources_listed" src="https://github.com/user-attachments/assets/5771263a-fbc0-4759-883e-de6787d15711" />

---

## 2️⃣ Create Billable Resources (No VM)

A **Standard Public IP** and a **managed disk** were created without any virtual machine.

This proves:
- Azure bills **resource existence**, not usage
- Networking and storage cost money independently

📸 **Screenshot:** Public IP and disk exist  

<img width="1266" height="270" alt="02_lab04_public_ip_and_disk" src="https://github.com/user-attachments/assets/8cd17135-03e5-43d7-b8f6-269a6a3c0f4e" />

---

## 3️⃣ Partial Cleanup (Hidden Cost Scenario)

Only part of the infrastructure was removed, intentionally leaving a disk behind to demonstrate orphaned cost.

📸 **Screenshot:** Resource group deletion initiated  

<img width="860" height="267" alt="03_lab04_resource_group_delete" src="https://github.com/user-attachments/assets/e276439a-7640-414a-bb9c-e47aeb860feb" />

---

## 4️⃣ Full Cleanup (Return to £0 State)

The resource group was fully deleted and verified to no longer exist.

📸 **Screenshot:** Resource group deletion confirmed  

<img width="921" height="226" alt="04_lab04_rg_deleted_confirmed" src="https://github.com/user-attachments/assets/5931b1e9-0759-4c2c-9684-1d22cf94e7b9" />

---

## 🧠 Key Questions Answered

### ❓ Stop vs Delete — What’s the Difference?

- **Stop (Deallocate):**
  - Compute billing stops
  - Disks and IPs continue billing

- **Delete:**
  - Removes the resource
  - Billing only stops for deleted components

- **Delete Resource Group:**
  - Removes *everything*
  - Guarantees zero ongoing cost

---

### ❓ Why Do People Get Surprise Cloud Bills?

Because:
- Disks and IPs persist after VMs are gone
- Nothing appears “running”
- Azure charges for **allocated resources**, not activity

---

## 📜 Commands Used (What They Do)

```bash
az account show
# Confirms active subscription and tenant

az group create --name rg-lab04-cost --location uksouth
# Creates a cost boundary

az resource list --resource-group rg-lab04-cost
# Lists all billable resources

az group delete --name rg-lab04-cost --yes --no-wait
# Deletes all resources and stops all costs

az group exists --name rg-lab04-cost
# Verifies deletion
```

---

## ✅ Final Insight

> In Azure, **compute is temporary**, but **storage and networking persist** unless explicitly deleted.

Cost awareness is an engineering responsibility.

---

*End of LAB 4*
