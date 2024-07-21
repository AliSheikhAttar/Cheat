# BPF Security - Short

- bpftrace: A high-level tracing language that simplifies the process of writing BPF programs for dynamic tracing. It is powerful, user-friendly, and - supports a variety of tracing capabilities.
- Tracepoints: Predefined static instrumentation points in the kernel, designed for low overhead and used primarily for monitoring and debugging specific kernel events.
- Kprobes: Dynamic instrumentation points that can be inserted at any location in the kernel code at runtime, offering greater flexibility but potentially higher overhead compared to tracepoints.


* BPF Helper:
printf is still using a BPF helper to format and send output to user space.
system is a bpftrace built-in function that calls a user-space command.

* bpf_send_signal():
Not used directly in this example. Instead, the kill command is executed from user space to send the signal.

- Perf Output Buffer:
The printf function uses the perf output buffer to send its output to user space.
The system function triggers a user-space command, which is executed outside of the BPF program context, contrasting with the direct use of bpf_send_signal() in Example 1.


* Cgroup skb Programs: Used to manage network packets in cgroups.
* Required Capability: CAP_NET_ADMIN is necessary to attach these programs to specific cgroup hooks.
* Reason for Restriction: Ensures security and stability by preventing unprivileged users from having low-level control over network traffic
* Current State (Linux 5.2): Unprivileged users can only use BPF for socket filters.
* Permissions Required: CAP_SYS_ADMIN for most BPF program types, CAP_NET_ADMIN for attaching cgroup skb programs.
* Error Handling: Unprivileged attempts result in EPERM errors.
* Documentation: All BPF tools are in section 8 of the man pages.
* Future Potential: Expanding BPF support for unprivileged users, especially in containerized environments


- kernel.unprivileged_bpf_disabled --->  Controls access for unprivileged users.
- net.core.bpf_jit_enable ---> Manages JIT compiler usage for performance improvements.
- net.core.bpf_jit_harden ---> Provides additional security protections for JIT.
- net.core.bpf_jit_kallsyms ---> Controls visibility of JIT images for debugging.
- net.core.bpf_jit_limit ---> Sets a memory limit for JIT compilation.

* Tracepoints:
>*Definition*: Tracepoints are static instrumentation points within the Linux kernel that provide information about kernel events.
>*Usage*: They can be used to gather data on specific events without significantly impacting system performance.
>*How to Use*: Use BPF programs to attach to these tracepoints and collect data. Tools like bpftrace can help in creating scripts to trace these points.

* USDT Probes (Userland Statically Defined Tracing):
>*Definition*: USDT probes are similar to tracepoints but are used in user-space applications.
>*Usage*: They allow you to insert instrumentation points into your applications at compile time.
>*How to Use*: BPF tools can be used to attach to USDT probes to monitor application-level events.

**LSM**:
Linux Security Modules (LSM) is a framework within the Linux kernel that provides a mechanism for various security policies and access controls. LSM allows the integration of different security models into the kernel, enabling additional security checks and restrictions beyond the standard Linux access control mechanisms.

- Key Features of LSM:
  - Pluggable Framework: Allows multiple security modules to be loaded into the kernel, each implementing different security policies.
  - Common Interface: Provides a common interface for security modules to hook into the kernel, making it easier to develop and integrate new security features.
  - Enhancing Security: Used to enhance the security of the system by providing additional checks on various operations like file access, process management, and network operations.
- Examples of LSM:
  - SELinux (Security-Enhanced Linux): Implements mandatory access control policies to limit what processes can do, adding an additional layer of security.
  - AppArmor: Uses path-based access control to restrict program capabilities based on file paths.
  - Smack (Simplified Mandatory Access Control Kernel): Provides a simple mandatory access control system.

- Usage of LSM Hooks:
LSM hooks are specific points in the kernel where security checks are performed. These hooks are prefixed with "security_". BPF programs can attach to these hooks to monitor and enforce security policies.

Example:
```bash
# Attach a BPF program to an LSM hook
sudo bpftrace -e 'kprobe:security_inode_permission { printf("Permission check on inode: %d\n", args->inode); }'
```

* Tracepoints and USDT Probes: Start by looking for tracepoints or USDT probes, which provide built-in instrumentation points with minimal performance overhead.
* LSM Kernel Hooks: If tracepoints or USDT probes are not available, check for LSM hooks that begin with "security_" to trace security-relevant events.
* Kprobes/Uprobes: As a last resort, use kprobes for kernel functions and uprobes for user-space functions to instrument raw code directly.