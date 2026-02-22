
# 🧪 Lab 06 — Azure Resource Dependencies & Failure Domains

## 💼 Business Context (Why This Matters)

As I continue learning Azure, I’m starting to realise that building resources is only part of the job.

Understanding **how resources depend on each other** is what prevents:

- Accidental outages during changes
- Failed deployments
- Orphaned resources (unexpected cost)
- Security gaps caused by partial deletion
- Poor troubleshooting decisions

This lab is part of my effort to move from “clicking resources into existence” toward understanding how cloud systems are structured.

I am still early in my journey, but this exercise helped me see Azure more as an interconnected system rather than separate components.

---

## 🎯 Objective

Understand how Azure infrastructure components depend on one another and how those dependencies affect:

- Deployment order
- Deletion constraints
- Troubleshooting logic
- Failure domains
- Cost control

---

## 🧱 Core Azure Resource Dependency Map

When building a Virtual Machine in Azure using networking components, the dependency chain looks like this:

Resource Group (RG)
└── Virtual Network (VNet)
    └── Subnet
        └── Network Interface (NIC)
            ├── Network Security Group (NSG)   (attached to NIC or Subnet)
            └── Virtual Machine (VM)
                └── OS Disk / Data Disks

Additional related components:

Public IP (PIP)
└── Attached to NIC (or Load Balancer)

Subnet
└── Route Table (UDR)

Subnet
└── NAT Gateway

---

## 🔄 Reverse Dependency (Deletion Logic)

Azure enforces dependency protection. Resources cannot be deleted if dependent resources still exist.

### ❌ You Cannot Delete:

- Subnet if a NIC is attached
- VNet if subnets exist
- NIC if attached to a VM
- Public IP if attached to a NIC
- Disk if attached to a VM

### ✅ Safe Deletion Order (Reverse Chain)

To safely remove infrastructure:

1. Delete VM
2. Delete NIC
3. Delete Public IP (if attached)
4. Delete Subnet
5. Delete VNet
6. Delete Resource Group

This shows that compute depends on networking — not the other way around.

---

## 🌐 Comparison: Azure vs Traditional Networking

### 🏢 Traditional On-Prem Networking

In a physical environment:

- Server includes physical NIC
- Cable connects directly to switch
- Firewall is a separate appliance
- Infrastructure is location-bound
- Removing a server usually removes its networking implicitly

Dependencies are often hidden inside hardware.

---

### ☁️ Azure Networking

In Azure:

- VM attaches to a NIC
- NIC attaches to a subnet
- Subnet exists inside a VNet
- NSG controls traffic separately
- Public IP exists independently
- Everything is modular and software-defined

Networking is:

- Decoupled from compute
- Explicitly defined
- Independently manageable
- Protected by dependency enforcement

This modular design increases flexibility — but also increases the need for structured thinking.

---

## 🔥 Failure Domain Thinking

If a VM is unreachable, investigation may include:

- VM power state
- NIC attachment
- NSG rules
- Public IP association
- Route tables
- DNS resolution
- Application/service state

This lab helped me understand that troubleshooting should follow dependency order rather than guessing randomly.

---

## 🧠 What I’m Learning

I’m still developing confidence in cloud architecture, but this lab helped me see:

- Infrastructure is layered
- Deletion order reveals system design
- Azure prevents destructive mistakes through dependency enforcement
- Cloud networking is more explicit than traditional networking

The goal isn’t to sound like an architect yet — it’s to build the thinking patterns that lead there.

---

## 🏁 Key Takeaway

Cloud infrastructure is not about clicking “Create VM.”

It is about understanding:

- What depends on what
- What survives deletion
- What blocks removal
- How failures propagate
