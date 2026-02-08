# Lab 3 — First Azure Virtual Machine (CLI-First)

## Context
Network Attached Storage (NAS) addresses the challenge of sharing and centralizing data across an organization. 
It is commonly used in both home and business environments to provide scalable, network-based file storage 
without relying on individual device disks.

## 🎯 Goal

Understand **what an Azure Virtual Machine actually is** by manually constructing the supporting Azure infrastructure using the **Azure CLI**, rather than relying on the Azure Portal.

This lab focuses on:
- Azure resource composition
- Networking-first design
- Cost awareness and regional capacity constraints
- Troubleshooting failed deployments
- Treating failure as a valid engineering outcome

---

## 🧰 Environment

- **OS:** macOS (Apple Silicon)
- **Shell:** zsh
- **Tooling:** Azure CLI v2.83.x
- **Interface:** CLI only
- **Region:** UK South

---

## 🔐 Azure Authentication

```bash
az login
az account show
```

📸 Screenshot:  
`Screenshot 2026-02-07 at 16.27.22.png`

---

## 🧱 Resource Group

```bash
az group create --name rg-learning-azure --location uksouth
```

📸 Screenshot:  
`Screenshot 2026-02-07 at 16.29.09.png`

---

## 🌐 Virtual Network & Subnet

```bash
az network vnet create   --resource-group rg-learning-azure   --name vnet-lab-01   --address-prefix 10.0.0.0/16   --subnet-name subnet-lab-01   --subnet-prefix 10.0.1.0/24
```

📸 Screenshot:  
`Screenshot 2026-02-07 at 16.29.33.png`

---

## 🔒 Network Security Group

```bash
az network nsg create   --resource-group rg-learning-azure   --name nsg-lab-01
```

📸 Screenshot:  
`Screenshot 2026-02-07 at 16.33.34.png`

---

## 🌍 Public IP

```bash
az network public-ip create   --resource-group rg-learning-azure   --name pip-vm-lab-01   --sku Standard   --allocation-method Static
```

📸 Screenshot:  
`Screenshot 2026-02-07 at 16.34.33.png`

---

## 🔌 Network Interface

```bash
az network nic create   --resource-group rg-learning-azure   --name nic-vm-lab-01   --vnet-name vnet-lab-01   --subnet subnet-lab-01   --network-security-group nsg-lab-01   --public-ip-address pip-vm-lab-01
```

📸 Screenshots:  
- `Screenshot 2026-02-07 at 16.38.32.png`  
- `Screenshot 2026-02-07 at 16.39.44.png`  
- `Screenshot 2026-02-07 at 16.40.07.png`

---

## 🖥️ VM Creation Attempt (Expected Failure)

```bash
az vm create   --resource-group rg-learning-azure   --name vm-lab-01   --nics nic-vm-lab-01   --image Ubuntu2204   --size Standard_B1s   --admin-username azureuser
```

📸 Screenshots:  
- `Screenshot 2026-02-07 at 16.40.14.png`  
- `Screenshot 2026-02-07 at 16.47.28.png`

---

## ❌ SKU Capacity Error

Error encountered:
```
SkuNotAvailable
```
📸 Screenshot:  
`Screenshot 2026-02-07 at 16.55.38.png`

---

## 🔍 Region Capacity Investigation

```bash
az vm list-sizes -l uksouth
```

📸 Screenshots:  
- `Screenshot 2026-02-07 at 16.58.22.png`  
- `Screenshot 2026-02-07 at 16.59.16.png`

---

## 🧠 Key Learnings

- VMs are **composed**, not single objects
- Networking is built **before** compute
- NIC is the central attachment point
- Failure domains include provider capacity
- Compute is scarce and expensive

---

## 🧹 Cleanup

```bash
az group delete --name rg-learning-azure --yes --no-wait
```

📸 Screenshots:  
- `Screenshot 2026-02-07 at 17.07.51.png`  
- `Screenshot 2026-02-07 at 17.12.07.png`  
- `Screenshot 2026-02-07 at 17.13.39.png`

---

## 🏁 Final Reflection

Failure was the lesson.

This lab reinforced **systems thinking**, cost awareness, and troubleshooting — the real work of a cloud engineer.
