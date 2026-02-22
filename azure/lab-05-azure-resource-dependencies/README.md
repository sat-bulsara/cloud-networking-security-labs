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
`00_lab05_subscription_check.png`

Verified correct subscription before deployment.

---

## 1️⃣ Resource Group Created

Created resource group: `rg-lab05-deps`

📸 Screenshot:  
`01_lab05_resource_group_created.png`

---

## 2️⃣ Virtual Network Created

VNet: `vnet-lab05`  
Address space: `10.0.0.0/16`

📸 Screenshot:  
`02_lab05_vnet_created.png`

---

## 3️⃣ Subnet Created

Subnet: `subnet-app`  
Address range: `10.0.1.0/24`

📸 Screenshot:  
`03_lab05_subnet_created.png`

---

## 4️⃣ Network Security Group Created

NSG: `nsg-lab05`

📸 Screenshot:  
`04_lab05_nsg_created.png`

---

## 5️⃣ NSG Associated to Subnet

Dependency created:

Subnet → NSG

📸 Screenshot:  
`05_lab05_nsg_associated.png`

---

## 6️⃣ Public IP Created

Public IP: `pip-lab05`  
SKU: Standard  
Assignment: Static

📸 Screenshot:  
`06_lab05_public_ip_created.png`

---

## 7️⃣ Network Interface Created

NIC: `nic-lab05`  
Attached to:

- `vnet-lab05`  
- `subnet-app`

📸 Screenshot:  
`07_lab05_nic_created.png`

---

## 8️⃣ Public IP Attached to NIC

Dependency created:

NIC → Public IP

📸 Screenshot:  
`08_lab05_public_ip_attached.png`

---

## 9️⃣ Attempted VNet Deletion (Failure Expected)

Azure blocked deletion due to active dependencies.

📸 Screenshot:  
`09_lab05_delete_vnet_failed.png`

---

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

📸 Screenshot:  
`10_lab05_nic_deleted.png`

---

### 🔹 Public IP Deleted

📸 Screenshot:  
`11_lab05_public_ip_deleted.png`

---

### 🔹 NSG Deletion Blocked

NSG still associated to subnet.

📸 Screenshot:  
`12_lab05_nsg_deleted_or_blocked.png`

---

### 🔹 NSG Detached from Subnet

📸 Screenshot:  
`13_lab05_nsg_detached.png`

---

### 🔹 NSG Deleted Successfully

📸 Screenshot:  
`14_lab05_nsg_deleted.png`

---

### 🔹 VNet Deleted Successfully

📸 Screenshot:  
`15_lab05_vnet_deleted.png`

---

## 🏁 Final Verification

Resource group confirmed empty.

📸 Screenshot:  
`16_lab05_rg_empty.png`

---

## ✅ Final Insight

> Deployment builds outward.  
> Teardown collapses inward.

Understanding dependency logic is fundamental to safe cloud engineering.

---

*End of LAB 5*
