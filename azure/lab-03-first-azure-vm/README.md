# 🧪 Lab 03 — First Azure Virtual Machine (CLI-First)

## 🎯 Goal

Understand **what an Azure Virtual Machine actually is** by manually constructing the supporting Azure infrastructure using the **Azure CLI**, rather than relying on the Azure Portal.

This lab demonstrates:
- How Azure resources are composed
- Why networking is built before compute
- The role of the Network Interface (NIC)
- Cost awareness and regional capacity limits
- Treating failure as a valid engineering outcome

> This lab prioritises *understanding* over a successful VM deployment.

---

## 🧰 Environment

- **Host OS:** macOS (Apple Silicon)
- **Shell:** zsh
- **Tooling:** Azure CLI v2.83.0
- **Interface:** CLI only (no Portal)
- **Region:** UK South
- **Cost control:** Manual creation + explicit cleanup

---

## 🔐 Azure Authentication & Context

```bash
az login
az account show
```

📸 Screenshot: `01-az-login.png`

---

## 🧱 1️⃣ Resource Group — Lifecycle Boundary

```bash
az group create \
  --name rg-learning-azure \
  --location uksouth
```

📸 Screenshot: `02-resource-group-created.png`

---

## 🌐 2️⃣ Virtual Network & Subnet — Building the Road

```bash
az network vnet create \
  --resource-group rg-learning-azure \
  --name vnet-lab-01 \
  --address-prefix 10.0.0.0/16 \
  --subnet-name subnet-lab-01 \
  --subnet-prefix 10.0.1.0/24
```

📸 Screenshot: `03-vnet-subnet-created.png`

---

## 🔒 3️⃣ Network Security Group — Traffic Control

```bash
az network nsg create \
  --resource-group rg-learning-azure \
  --name nsg-lab-01
```

📸 Screenshot: `04-nsg-created.png`

---

## 🌍 4️⃣ Public IP — Azure Edge Resource

```bash
az network public-ip create \
  --resource-group rg-learning-azure \
  --name pip-vm-lab-01 \
  --sku Standard \
  --allocation-method Static
```

📸 Screenshot: `05-public-ip-created.png`

---

## 🔌 5️⃣ Network Interface (NIC) — The Anchor Point

```bash
az network nic create \
  --resource-group rg-learning-azure \
  --name nic-vm-lab-01 \
  --vnet-name vnet-lab-01 \
  --subnet subnet-lab-01 \
  --network-security-group nsg-lab-01 \
  --public-ip-address pip-vm-lab-01
```

📸 Screenshot: `06-nic-created.png`

---

## 🖥️ 6️⃣ Virtual Machine Attempt — Expected Failure

```bash
az vm create \
  --resource-group rg-learning-azure \
  --name vm-lab-01 \
  --nics nic-vm-lab-01 \
  --image Ubuntu2204 \
  --size Standard_B1s \
  --admin-username azureuser
```

📸 Screenshot: `07-vm-sku-not-available.png`

---

## 🔍 7️⃣ Troubleshooting — Capacity Investigation

```bash
az vm list-sizes -l uksouth
```

📸 Screenshot: `08-vm-sizes-list.png`

---

## 🔄 Cleanup

```bash
az group delete \
  --name rg-learning-azure \
  --yes \
  --no-wait
```

📸 Screenshot: `09-resource-group-deleted.png`

