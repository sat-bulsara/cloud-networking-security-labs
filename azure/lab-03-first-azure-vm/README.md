# Lab 3 — First Azure Virtual Machine (CLI-First)


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
<img width="849" height="525" alt="Screenshot 2026-02-07 at 16 29 09" src="https://github.com/user-attachments/assets/87715844-667a-4bf0-85a0-d54c5b922166" />

---

## 🌐 Virtual Network & Subnet

```bash
az network vnet create   --resource-group rg-learning-azure   --name vnet-lab-01   --address-prefix 10.0.0.0/16   --subnet-name subnet-lab-01   --subnet-prefix 10.0.1.0/24
```

📸 Screenshot:  
<img width="859" height="530" alt="Screenshot 2026-02-07 at 16 29 33" src="https://github.com/user-attachments/assets/8babb75d-82bf-4a35-87ff-7b3d6aa8995d" />

---

## 🔒 Network Security Group

```bash
az network nsg create   --resource-group rg-learning-azure   --name nsg-lab-01
```

📸 Screenshot:  
<img width="865" height="520" alt="Screenshot 2026-02-07 at 16 33 34" src="https://github.com/user-attachments/assets/13b088f4-2664-4b62-920a-d2d936749c3c" />

---

## 🌍 Public IP

```bash
az network public-ip create   --resource-group rg-learning-azure   --name pip-vm-lab-01   --sku Standard   --allocation-method Static
```

📸 Screenshot:  
<img width="862" height="534" alt="Screenshot 2026-02-07 at 16 34 33" src="https://github.com/user-attachments/assets/de172688-41dd-495e-8685-2cef3d8dff6e" />

---

## 🔌 Network Interface

```bash
az network nic create   --resource-group rg-learning-azure   --name nic-vm-lab-01   --vnet-name vnet-lab-01   --subnet subnet-lab-01   --network-security-group nsg-lab-01   --public-ip-address pip-vm-lab-01
```

📸 Screenshots:  
<img width="862" height="520" alt="Screenshot 2026-02-07 at 16 38 32" src="https://github.com/user-attachments/assets/141a21c0-d1d5-4cb7-acb0-6de137ddc229" />
<img width="861" height="530" alt="Screenshot 2026-02-07 at 16 39 44" src="https://github.com/user-attachments/assets/4e1babdb-6322-4508-aec3-e3382789a956" />
<img width="867" height="522" alt="Screenshot 2026-02-07 at 16 40 07" src="https://github.com/user-attachments/assets/24980f90-dda3-483f-b1d6-8f2c6fcc14c3" />

---

## 🖥️ VM Creation Attempt (Expected Failure)

```bash
az vm create   --resource-group rg-learning-azure   --name vm-lab-01   --nics nic-vm-lab-01   --image Ubuntu2204   --size Standard_B1s   --admin-username azureuser
```

📸 Screenshots:  
<img width="866" height="539" alt="Screenshot 2026-02-07 at 16 40 14" src="https://github.com/user-attachments/assets/8cdd9323-de1b-4b97-a830-f039ee3784f1" />
<img width="853" height="525" alt="Screenshot 2026-02-07 at 16 47 28" src="https://github.com/user-attachments/assets/0daeaef6-0625-45bb-aa2e-e168f95b5c3c" />

---

## ❌ SKU Capacity Error

Error encountered:
```
SkuNotAvailable
```
📸 Screenshot:  
<img width="871" height="524" alt="Screenshot 2026-02-07 at 16 55 38" src="https://github.com/user-attachments/assets/0400651a-6478-4ad7-9123-2e63ccb139a5" />

---

## 🔍 Region Capacity Investigation

```bash
az vm list-sizes -l uksouth
```

📸 Screenshots:  
<img width="860" height="526" alt="Screenshot 2026-02-07 at 16 58 22" src="https://github.com/user-attachments/assets/b58d4f41-08f5-431f-bcd7-842e9abb61e8" />
<img width="856" height="520" alt="Screenshot 2026-02-07 at 16 59 16" src="https://github.com/user-attachments/assets/7ff0fdc5-c3d4-480b-ab14-f3fb9edab2d8" />

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
<img width="853" height="521" alt="Screenshot 2026-02-07 at 17 07 51" src="https://github.com/user-attachments/assets/300dab7d-765f-4e60-9184-053a411f32a6" />
<img width="859" height="522" alt="Screenshot 2026-02-07 at 17 12 07" src="https://github.com/user-attachments/assets/c2c0d8b0-7578-43c2-beec-b822f43ac6db" />
<img width="859" height="525" alt="Screenshot 2026-02-07 at 17 13 39" src="https://github.com/user-attachments/assets/ef39643a-0dbb-45e3-86ef-4fdb4d63899f" />

---

## 🏁 Final Reflection

Failure was the lesson.

This lab reinforced **systems thinking**, cost awareness, and troubleshooting — the real work of a cloud engineer.
