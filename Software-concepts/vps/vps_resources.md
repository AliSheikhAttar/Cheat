Yes, in a typical Virtual Private Server (VPS) setup, when a provider specifies that a VPS has 2GB of RAM and 2 core processors, it usually means those resources are **dedicated** to that specific VPS. Let me break it down for you:

### What "Dedicated" Means
- **RAM (Memory)**: The 2GB of RAM is reserved exclusively for your VPS. This ensures that no other VPS on the same physical machine can use that portion of memory. You have consistent access to the full 2GB at all times.
- **CPU (Processors)**: The 2 core processors are also allocated specifically to your VPS. These cores are set aside for your use, meaning other VPS instances on the same physical server cannot borrow or interfere with them.

### How It Works on the Physical Machine
On the physical server hosting multiple VPS instances, the total available resources (RAM, CPU cores, etc.) are divided among the VPSs. When your VPS is assigned 2GB of RAM and 2 cores:
- Those resources are "carved out" and reserved just for your VPS.
- Even if other VPSs on the same machine are under heavy load, your 2GB of RAM and 2 cores remain unaffected because they are dedicated to you.

### Why This Matters
- **Stable Performance**: Since the resources are dedicated, your VPS won’t slow down due to other users’ activities on the same physical machine.
- **Predictability**: You know exactly how much RAM and CPU power you have, making it easier to run your applications reliably.

### A Quick Caveat
While this is true for most standard VPS setups, some hosting providers might **oversell** resources. This means they could allocate more resources across all VPSs than the physical machine actually has, leading to shared or reduced performance during peak times. However, reputable providers ensure that the 2GB of RAM and 2 cores you’re promised are truly dedicated to your VPS.

### In Summary
Yes, on a physical machine, a VPS allocated with 2GB of RAM and 2 core processors typically has those resources dedicated solely to it. This setup ensures your VPS operates in an isolated and predictable environment, giving you full control over the specified resources. If you’re unsure, it’s always a good idea to confirm with your hosting provider that these resources are guaranteed as dedicated!