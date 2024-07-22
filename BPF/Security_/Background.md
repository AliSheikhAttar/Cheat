# BPF Security

## Background on security
* Security analysis
  * Sniffing activity for real-time forensics
  * Privilege debugging
  * Executable usage whitelists
  * Reverse engineering of malware
* Monitoring
  * Custom auditing
  * Host-based intrusion detection systems (HIDS)
  * Container-based intrusion detection systems (CIDS)
* Policy enforcement
  * Networking firewalls
  * Detecting malware and dynamically blocking packets and taking other preventive actions


## BPF Capabilities
BPF can help with these security tasks, including analysis, monitoring, and policy enforcement.
For security analysis, the types of questions that BPF can answer include:
- Which processes are being executed?
- What network connections are being made? By which processes?
- Which system privileges are being requested by which processes?
- What permission denied errors are happening on the system?
- Is this kernel/user function being executed with these arguments (in checking for active
exploits)?

## Limited Buffers & Map vulnerablity

BPF output buffers and maps have limits that can be exceeded, causing events to not be recorded. This may be
exploited by an attacker as an attempt to evade proper logging or policy enforcement, by inundat-
ing the system with events. BPF is aware of when these limits are exceeded, and can report this to
user space for appropriate action. Any security solution built using BPF tracing needs to record
these overflow or dropped events, to satisfy non-repudiation requirements.

Another approach is to add a per-CPU map to count important events. Unlike the perf output
buffer or maps involving keys, once BPF has created a per-CPU map of fixed counters, there is no
risk of losing events. This could be used in conjunction with perf event output to provide more
detail: the more detail may be lost, but the count of events will not be.


## Policy enforcement
Policy enforcement refers to the mechanisms and processes used to ensure that rules, policies, and regulations are adhered to within a system.
The goal of policy enforcement is to maintain compliance, ensure security, and optimize the performance and integrity of the system.

- **seccomp**
Purpose: Seccomp (secure computing mode) is used to restrict the system calls (syscalls) that a process can make, thereby limiting its ability to perform potentially harmful operations.
Mechanism: Seccomp can execute BPF programs (specifically classic BPF) to decide whether to allow or deny syscalls. It supports actions like:
Killing the calling process (SECCOMP_RET_KILL_PROCESS).
Returning an error to the calling process (SECCOMP_RET_ERRNO).
Offloading complex decisions to user-space programs (SECCOMP_RET_USER_NOTIF), where the user-space program is notified and can handle the syscall decision.

- **Cilium**
Purpose: Cilium is a networking solution that secures and manages network connectivity and load balancing for application containers or processes.
Mechanism: It employs BPF programs at various network layers, such as:
XDP: eXpress Data Path, for high-performance packet processing.
cgroup: Control groups for resource management.
tc: Traffic control hooks for managing network traffic. For instance, it uses a sch_clsact qdisc (queueing discipline) with a BPF program to handle tasks like packet mangling, forwarding, or dropping.

- **bpfilter**
Purpose: Bpfilter is a project aimed at replacing the traditional iptables firewall with BPF-based filtering.
Mechanism: It helps transition by converting iptables rules into BPF bytecode via a user-mode helper, making the rules more efficient and integrated with the kernel.

- **Landlock**
Purpose: Landlock is a security module that uses BPF to provide fine-grained access control over kernel resources.
Mechanism: For example, it can restrict access to specific parts of the filesystem based on a BPF inode map that can be updated from user space, enhancing security by controlling file access at a granular level.

- **KRSI (Kernel Runtime Security Instrumentation)**
Purpose: KRSI is a Linux Security Module (LSM) developed by Google for extensible auditing and enforcement of security policies.
Mechanism: It introduces a new BPF program type (BPF_PROG_TYPE_KRSI) and includes helpers like bpf_send_signal(), enabling BPF programs to send signals (e.g., SIGKILL) to processes directly. This can be used for immediate action on detecting security vulnerabilities, such as terminating a process that is exploiting a vulnerability



## bpf_send_signal()
A new BPF helper, bpf_send_signal(), should be included in the upcoming Linux 5.3 release .
This will allow a new type of enforcement program that can send SIGKILL and other signals to
processes from BPF programs alone, without needing seccomp. Taking the previous vulnerability
detection example further, imagine a bpftrace program that not only detects a vulnerability, but
immediately kills the process using it. For example:
```bash
bpftrace --unsafe -e 't:syscalls:sys_enter_renameat2 /args->flags == 2/ {
time(); printf("killing PID %d %s\n", pid, comm); signal(9); }'
```
Such tools could be used as a temporary workaround until software can be properly patched.2
Care must be taken when using signal(): this particular example kills all users of renameat2(2)
who are using RENAME_EXCHANGE, and it can’t tell whether the process was good or evil.
Other signals, such as SIGABRT, could be used to core dump the process to allow forensic analysis
of the malicious software.
Until bpf_send_signal() is available, processes can be terminated by the user-space tracer, based on
reading events from the perf buffer. 
For example, using bpftrace’s system():
```bash
bpftrace --unsafe -e 't:syscalls:sys_enter_renameat2 /args->flags == 2/ {
time(); printf("killing PID %d %s\n", pid, comm);
system("kill -9 %d", pid); }'
```
system() is an asynchronous action (see Chapter 5) issued to bpftrace via the perf output buffer,
and then executed by bpftrace some time after the event. This introduces a lag between detection
and enforcement, which in some environments may be unacceptable. bpf_send_signal() solves
this by sending the signal immediately, in kernel context, during the BPF program.

### Explain the code
#### Ex1
```bash
bpftrace --unsafe -e 't:syscalls:sys_enter_renameat2 /args->flags == 2/ {
    time(); 
    printf("killing PID %d %s\n", pid, comm); 
    signal(9); 
}'
```
This bpftrace script attaches to the sys_enter_renameat2 tracepoint, which triggers when the renameat2 syscall is entered. It filters the events where args->flags equals 2. When this condition is met, it performs the following actions:

- time():
This prints the current time when the event is triggered.

- printf("killing PID %d %s\n", pid, comm):
This prints a message including the PID (pid) and command name (comm) of the process making the syscall.

- signal(9):
This sends the SIGKILL signal (signal number 9) to the process, effectively terminating it immediately.


* BPF Helper:
printf is implemented using a BPF helper to format and send output to user space.
signal is a bpftrace built-in function that leverages the bpf_send_signal() helper to send a signal directly from the BPF program.

* bpf_send_signal():
This helper is used by the signal(9) command to send the SIGKILL signal to the process identified by pid.

* Perf Output Buffer:
The printf function sends its output through a perf output buffer to the user space, where it can be displayed on the console.

#### Ex2
```bash
bpftrace --unsafe -e 't:syscalls:sys_enter_renameat2 /args->flags == 2/ {
    time(); 
    printf("killing PID %d %s\n", pid, comm); 
    system("kill -9 %d", pid); 
}'
```
This bpftrace script is similar to Example 1 but with a key difference in how it sends the kill signal. It performs the same initial actions:

- time():
Prints the current time.

- printf("killing PID %d %s\n", pid, comm):
Prints a message including the PID and command name.

- system("kill -9 %d", pid):
Executes a shell command to send the SIGKILL signal to the process. This command is executed in user space.


- **Key Differences**:
Direct vs. Indirect Signal Sending:

- Example 1 uses bpf_send_signal() directly via the signal(9) function to kill the process from within the BPF program.
- Example 2 uses the system("kill -9 %d", pid) command to execute a shell command from user space to kill the process.

- **Performance and Overhead**:

- Example 1 is likely more efficient, as the signal is sent directly by the BPF program using the kernel helper.
- Example 2 incurs additional overhead due to the context switch from kernel space to user space to execute the shell command.

> they differ in their approach to sending signals: one uses the bpf_send_signal() helper directly from the BPF context, while the other uses a user-space command.


## Unprivileged BPF Users

he ability to use BPF is tightly controlled by the kernel to ensure security and system integrity. This control is evident in the source code for the bpf(2) syscall:

```bash
if (type != BPF_PROG_TYPE_SOCKET_FILTER &&
    type != BPF_PROG_TYPE_CGROUP_SKB &&
    !capable(CAP_SYS_ADMIN))
    return -EPERM;

```
### Code Breakdown
- Program Types:

BPF_PROG_TYPE_SOCKET_FILTER: This type of BPF program is used for filtering network packets at the socket level.
BPF_PROG_TYPE_CGROUP_SKB: This type is used for cgroup skb (socket buffer) programs, which can inspect and drop packets in control groups.

- Capability Check:

capable(CAP_SYS_ADMIN): This function checks if the user has the CAP_SYS_ADMIN capability, which is a powerful administrative privilege.

- Permission Denial:

If the BPF program type is neither BPF_PROG_TYPE_SOCKET_FILTER nor BPF_PROG_TYPE_CGROUP_SKB, and the user does not have CAP_SYS_ADMIN, the syscall returns -EPERM, indicating "Operation not permitted."
Practical Implications
Socket Filters
Unprivileged users are allowed to use socket filters. These filters can be used to inspect and manipulate network packets at the socket level. This usage scenario is deemed safe and useful enough to be allowed without special privileges.

- Cgroup skb Programs
Cgroup skb (socket buffer) programs are a type of BPF program that can be used to inspect and manipulate network packets in the context of control groups (cgroups). Cgroups are a Linux kernel feature used to organize processes into hierarchical groups and manage their resources, including CPU, memory, and network bandwidth.

Attaching Cgroup skb Programs
There are specific hooks within cgroups where these skb programs can be attached to manage network traffic:

* BPF_CGROUP_INET_INGRESS: This hook is used to manage incoming packets.
* BPF_CGROUP_INET_EGRESS: This hook is used to manage outgoing packets.

- Required Capabilities

CAP_NET_ADMIN: This is a Linux capability that allows various network-related operations. It is less powerful than CAP_SYS_ADMIN but still provides significant control over network interfaces, routing tables, and network traffic.
To attach cgroup skb programs to the above hooks (BPF_CGROUP_INET_INGRESS and BPF_CGROUP_INET_EGRESS), a user must have CAP_NET_ADMIN. This requirement ensures that only users with appropriate permissions can control network traffic at such a low level, which is crucial for maintaining system security and stability.

- Reason for Restriction

The restriction to CAP_NET_ADMIN is due to the following reasons:

Security: Allowing unprivileged users to attach cgroup skb programs could lead to potential abuse, such as intercepting, altering, or dropping network packets in ways that could compromise system or network security.
Stability: Misconfigured or malicious cgroup skb programs could disrupt network traffic, leading to denial of service or other unintended consequences.
Practical Implications

- For unprivileged users:

They can use BPF for socket filters, which are relatively safer and limited in scope.
They cannot attach cgroup skb programs to ingress or egress hooks without CAP_NET_ADMIN.
For privileged users (those with CAP_NET_ADMIN):

They can use cgroup skb programs to effectively manage and control network traffic within specific cgroups, providing powerful tools for traffic shaping, monitoring, and security.
While cgroup skb programs are allowed in the context of the code, they require the CAP_NET_ADMIN capability to attach to specific cgroup hooks (BPF_CGROUP_INET_INGRESS and BPF_CGROUP_INET_EGRESS). This restriction is due to the potential impact these programs can have on network traffic management.

- Error Handling
For users without CAP_SYS_ADMIN, attempting to use BPF for anything other than socket filters results in the syscall failing with an EPERM error. Tools relying on BPF, like BCC (BPF Compiler Collection) tools, will output a message indicating the need for super-user privileges. Similarly, bpftrace, another tool for tracing with BPF, checks if the user ID is 0 (root) and will not run if it isn't, again citing the need for root access.

## Configuring BPF Security

Configuring BPF (Berkeley Packet Filter) security involves managing various kernel parameters to control how BPF programs are executed and how their execution is protected. This ensures both performance optimization and security by regulating access and behavior of BPF programs. Here’s a detailed explanation of the BPF security controls mentioned:

**Key BPF Security Controls**

### kernel.unprivileged_bpf_disabled

Purpose: Controls whether unprivileged users can load BPF programs.
Values:
0: Allows unprivileged users to load BPF programs. This is useful for environments where limited access to BPF features is required for users without administrative privileges.
1: Disables unprivileged access to BPF. This setting restricts BPF usage to users with administrative privileges (CAP_SYS_ADMIN), enhancing security by preventing potential misuse or abuse by unprivileged users.
Configuration:
```bash
### Disable unprivileged BPF access
sysctl -w kernel.unprivileged_bpf_disabled=1
echo 1 > /proc/sys/kernel/unprivileged_bpf_disabled
```
Note: Once set to 1, reverting to 0 is not allowed, which means that this setting is effectively a one-way configuration for increased security.

### net.core.bpf_jit_enable

Purpose: Controls the Just-In-Time (JIT) compiler for BPF programs, which improves performance by compiling BPF bytecode to native machine code.

Values:

0: Disables the JIT compiler (default). BPF programs will be interpreted, which is slower.
1: Enables the JIT compiler, improving performance by translating BPF bytecode into machine code.
2: Enables JIT and logs compiler debug traces to the kernel log. This setting is intended for debugging purposes only and should not be used in production environments.
Configuration:

```bash
### Enable JIT compiler
sysctl -w net.core.bpf_jit_enable=1
echo 1 > /proc/sys/net/core/bpf_jit_enable
```
Additional Information: The JIT compiler's availability depends on the processor architecture. The Linux kernel supports JIT compilers for many architectures, including x86_64, arm64, ppc64, s390x, sparc64, mips64, and riscv. The x86_64 and arm64 compilers are considered mature and well-tested.

### net.core.bpf_jit_harden

Purpose: Enables additional security protections for the JIT compiler to mitigate potential security vulnerabilities.
Values:
0: Disables JIT hardening (default). This provides no extra security features but may offer better performance.
1: Enables JIT hardening for unprivileged users only. Adds some security protections, particularly for users without administrative privileges.
2: Enables JIT hardening for all users. Provides the highest level of security but may impact performance.
Configuration:
```bash
### Enable JIT hardening for unprivileged users
sysctl -w net.core.bpf_jit_harden=1
echo 1 > /proc/sys/net/core/bpf_jit_harden
```

### net.core.bpf_jit_kallsyms

Purpose: Controls whether the compiled JIT images are exposed via /proc/kallsyms, which can be useful for debugging but can also reveal sensitive information.
Values:
0: Exposes JIT images. Useful for debugging purposes.
1: Disables the exposure of JIT images. If bpf_jit_harden is enabled, this option is automatically disabled.
Configuration:
```bash
### Disable exposure of JIT images
sysctl -w net.core.bpf_jit_kallsyms=0
echo 0 > /proc/sys/net/core/bpf_jit_kallsyms
```

### net.core.bpf_jit_limit

Purpose: Sets a memory limit (in bytes) for JIT compilation. If the limit is reached, further unprivileged user requests for BPF JIT compilation are blocked and redirected to the BPF interpreter.
Values: The default value is typically set to a large number, but it can be adjusted based on system requirements and resource availability.
Configuration:
```bash
### Set BPF JIT memory limit to 264MB
sysctl -w net.core.bpf_jit_limit=264241152
echo 264241152 > /proc/sys/net/core/bpf_jit_limit
```

## Strategy for the security analysis of system activity not already covered by other BPF tools:

1. Check whether there are tracepoints or USDT probes available to instrument the activity.

```bash
# List available tracepoints
sudo bpftrace -l tracepoint

# Attach a BPF program to a tracepoint
sudo bpftrace -e 'tracepoint:syscalls:sys_enter_execve { printf("execve called: %s\n", str(args->filename)); }'
```


2. Check whether LSM kernel hooks can be traced: these begin with "security_".

```bash
# Example of attaching to an LSM hook (assuming a tool like bpftrace or custom BPF program)
sudo bpftrace -e 'kprobe:security_inode_permission { printf("Permission check on inode: %d\n", args->inode); }'
```

3. Use kprobes/uprobes as appropriate to instrument the raw code.
Example Commands:

```bash
# List available kprobes
sudo bpftrace -l kprobe

# Attach a BPF program to a kprobe
sudo bpftrace -e 'kprobe:vfs_open { printf("File opened: %s\n", str(args->filename)); }'

# List available uprobes
sudo bpftrace -l uprobe

# Attach a BPF program to a uprobe
sudo bpftrace -e 'uprobe:/usr/bin/bash:main { printf("Bash main function called\n"); }'

```