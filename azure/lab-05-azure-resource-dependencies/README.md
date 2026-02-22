# 🟦 LAB 5 — Azure Resource Dependencies & Blast Radius

**Student:** [Your Name]  
**Platform:** Microsoft Azure  
**Access Method:** Azure Portal  
**Resource Group:** rg-lab05-deps  
**Final State:** Clean (No Resources Remaining)

---

## 🎯 Goal

Understand how Azure resources depend on one another and how Azure prevents deletion when dependencies exist.

---

## 💼 Why This Matters (Business Context)

In production environments, accidental deletion of networking resources can cause service outages.

Understanding Azure resource dependencies helps prevent:

- Accidental downtime  
- Broken application connectivity  
- Security misconfigurations  
- Unexpected production impact  

This lab reinforced that infrastructure changes must follow dependency order to avoid disrupting running systems.

---

## 🧠 Lab Summary

During LAB 5, I built a layered Azure networking structure consisting of a Virtual Network, Subnet, Network Security Group (NSG), Network Interface (NIC), and Public IP.

I intentionally attempted to delete the Virtual Network before removing its dependencies. Azure correctly blocked the deletion due to active child resources and associations.

I then removed resources in reverse dependency order:

- Deleted NIC  
- Deleted Public IP  
- Detached NSG from Subnet  
- Deleted NSG  
- Deleted VNet  

This demonstrated Azure’s dependency enforcement model and showed how infrastructure must be dismantled from the leaf nodes inward.

The final state confirmed a clean, empty resource group.

---

## 🧰 Environment Verification

📸 Screenshot:  
<img width="1926" height="966" alt="00_lab05_subscription_check" src="https://github.com/user-attachments/assets/1f23798e-9831-441b-a805-2aad7cc75e6a" />

Verified correct subscription before deployment.

---

## 1️⃣ Resource Group Created

Created resource group: `rg-lab05-deps`

📸 Screenshot:  
<img width="1643" height="326" alt="01_lab05_resource_group_created" src="https://github.com/user-attachments/assets/a1138235-353a-4ec5-8ed4-c0156ad435ce" />

---

## 2️⃣ Virtual Network Created

VNet: `vnet-lab05`  
Address space: `10.0.0.0/16`

📸 Screenshot:  
<img width="3976" height="2246" alt="02_lab05_vnet_created" src="https://github.com/user-attachments/assets/52e1e6b2-de97-4d01-a5f4-1ca68612caa4" />
<img width="4064" height="2334" alt="02 1_lab05_vnet_created" src="https://github.com/user-attachments/assets/48515624-cc8f-48c5-9190-9bb1cead251b" />

---

## 3️⃣ Subnet Created

Subnet: `subnet-app`  
Address range: `10.0.1.0/24`

📸 Screenshot:  
<img width="3976" height="2246" alt="03_lab05_subnet_created" src="https://github.com/user-attachments/assets/967000d7-7579-4070-8eb4-38d8cef83602" />

---

## 4️⃣ Network Security Group Created

NSG: `nsg-lab05`

📸 Screenshot:  
<img width="1621" height="470" alt="04_lab05_nsg_created" src="https://github.com/user-attachments/assets/f83863e6-232a-4a97-8be7-cecb3d3942e0" />

---

## 5️⃣ NSG Associated to Subnet

Dependency created:

Subnet → NSG

📸 Screenshot:  
<img width="1680" height="262" alt="05_lab05_nsg_associated" src="https://github.com/user-attachments/assets/b9c127c7-c245-4300-bff7-548ecbc8de44" />

---

## 6️⃣ Public IP Created

Public IP: `pip-lab05`  
SKU: Standard  
Assignment: Static

📸 Screenshot:  
<img width="1622" height="485" alt="06_lab05_public_ip_created" src="https://github.com/user-attachments/assets/e4cd83e8-b2ce-4b78-94a5-f44fef3bf1fb" />

---

## 7️⃣ Network Interface Created

NIC: `nic-lab05`  
Attached to:

- `vnet-lab05`  
- `subnet-app`

📸 Screenshot:  
<img width="962" height="881" alt="07_lab05_nic_created" src="https://github.com/user-attachments/assets/87690f2e-4194-47fd-8f41-7b9ea9da20b7" />

---


## 9️⃣ Attempted VNet Deletion (Failure Expected)

Azure blocked deletion due to active dependencies.

📸 Screenshot:  

<img width="1040" height="189" alt="09B_lab05_delete_vnet_failed" src="https://github.com/user-attachments/assets/fa327a6f-57b2-4cb3-95b6-87d5050d5ba1" />
<img width="1615" height="618" alt="09A_lab05_dependency_graph" src="https://github.com/user-attachments/assets/3b6294e3-2154-43db-bbc0-f19298662d1a" />


## 🗺️ Dependency Map (Simplified)

Resource Group
└── Virtual Network (vnet-lab05)
└── Subnet (subnet-app)
├── Network Security Group (nsg-lab05)
└── Network Interface (nic-lab05)
└── Public IP (pip-lab05)

### Deletion Order (Reverse Dependency)

1. NIC  
2. Public IP  
3. NSG (after detaching)  
4. VNet  
5. Resource Group  

---

## 🔥 Reverse Dependency Teardown

### 🔹 NIC Deleted

---

### 🔹 Public IP Deleted

📸 Screenshot:  
<img width="861" height="928" alt="11_lab05_public_ip_deleted" src="https://github.com/user-attachments/assets/7f677805-8e84-4fa3-a60c-29305b98e315" />

---

### 🔹 NSG Deletion Blocked

NSG still associated to subnet.

📸 Screenshot:  
<img width="1706" height="674" alt="12_lab05_nsg_deleted_or_blocked" src="https://github.com/user-attachments/assets/76c39fb9-9a28-4877-aab3-1e1a0caf81a5" />

---

### 🔹 NSG Detached from Subnet

📸 Screenshot:  
<img width="854" height="167" alt="13_lab05_nsg_detached" src="https://github.com/user-attachments/assets/85e8d9e7-6b7e-4be3-9e71-fb99602de41e" />

---

### 🔹 NSG Deleted Successfully

📸 Screenshot:  
<img width="866" height="355" alt="14_lab05_nsg_deleted" src="https://github.com/user-attachments/assets/b415d425-e5a4-4ab5-a872-f0016e82fade" />

---

### 🔹 VNet Deleted Successfully

📸 Screenshot:  
<img width="1171" height="513" alt="15_lab05_vnet_deleted" src="https://github.com/user-attachments/assets/ac3bbbf4-5d8a-4ef3-ab17-22aa8310ea06" />

---

## 🏁 Final Verification

Resource group confirmed empty.

📸 Screenshot:  
<img width="1896" height="793" alt="16_lab05_rg_empty" src="https://github.com/user-attachments/assets/05ab16c5-79f7-4990-ae1b-fd402268d5d0" />

---

## ✅ Final Insight

> Deployment builds outward.  
> Teardown collapses inward.

Understanding dependency logic is fundamental to safe cloud engineering.

---

*End of LAB 5*
