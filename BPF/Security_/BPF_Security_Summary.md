# BPF Security - Short

## BCC:
(BPF Compiler Collection) provides tools and libraries to simplify the writing and running of eBPF programs.
****
- bpftrace: A high-level tracing language that simplifies the process of writing BPF programs for dynamic tracing. It is powerful, user-friendly, and - supports a variety of tracing capabilities.
- Tracepoints: Predefined static instrumentation points in the kernel, designed for low overhead and used primarily for monitoring and debugging specific kernel events.
- Kprobes: Dynamic instrumentation points that can be inserted at any location in the kernel code at runtime, offering greater flexibility but potentially higher overhead compared to tracepoints.


## BPF Helper:
printf is still using a BPF helper to format and send output to user space.
system is a bpftrace built-in function that calls a user-space command.

## bpf_send_signal():
Not used directly in this example. Instead, the kill command is executed from user space to send the signal.

## Perf Output Buffer:
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

## Tracepoints:
>*Definition*: Tracepoints are static instrumentation points within the Linux kernel that provide information about kernel events.
>*Usage*: They can be used to gather data on specific events without significantly impacting system performance.
>*How to Use*: Use BPF programs to attach to these tracepoints and collect data. Tools like bpftrace can help in creating scripts to trace these points.

* USDT Probes (Userland Statically Defined Tracing):
>*Definition*: USDT probes are similar to tracepoints but are used in user-space applications.
>*Usage*: They allow you to insert instrumentation points into your applications at compile time.
>*How to Use*: BPF tools can be used to attach to USDT probes to monitor application-level events.

## LSM:
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

* execve:
execve is a system call used in Unix-like operating systems to execute a new program. When a process calls execve, it replaces its current memory space with a new program, effectively transforming into the new process.
The typical flow of creating a new process involves:
fork or clone: These syscalls create a new process by duplicating the calling process.
execve: The newly created process then calls execve to execute a different program.

## Binary Files: Executable and Linking Format (ELF)
What is ELF?
The Executable and Linking Format (ELF) is a standard file format for executables, object code, shared libraries, and core dumps in Unix-like operating systems, such as Linux. The ELF format is flexible and extensible, making it suitable for a variety of applications.

Components of an ELF File
- Header: Contains metadata about the file, including the type (e.g., executable, shared library), architecture, entry point address, and the program header table offset.
- Program Header Table: Describes the segments of the file that are necessary for program execution.
- Section Header Table: Contains information about the sections of the file, which are used for linking and relocation.
- Sections:
  - .text: Contains the executable code.
  - .data: Contains initialized data.
  - .bss: Contains uninitialized data.
  - .rodata: Contains read-only data.
  - .symtab: Symbol table, used for linking.
  - .strtab: String table, used for storing symbol names.
  - .debug: Contains debugging information.

### Uses of ELF Files
  * Executables: Programs that can be directly executed by the operating system.
  * Shared Libraries: Libraries that can be dynamically loaded at runtime.
  * Object Files: Intermediate files used in the process of compiling a program.
  * Core Dumps: Files that contain the memory image of a process at a specific point in time, often used for debugging.
- Where are ELF Files Found?
  - System Binaries: /bin, /sbin, /usr/bin, /usr/sbin
  - Libraries: /lib, /usr/lib, /lib64, /usr/lib64
  - Compiled Applications: Anywhere in the filesystem where user applications are installed, often in /usr/local/bin or user-specific directories.

* readline() kernel function
Example Usage in Bash:
When you open a Bash shell and type a command, the following happens:

Invocation: The shell waits for user input, invoking readline() to capture the input.
Editing: As you type, you can use keyboard shortcuts to move the cursor, edit the text, and recall history, all handled by the readline() function.
Completion: Pressing Tab triggers auto-completion, another feature provided by readline().
Execution: Once you press Enter, readline() returns the completed line of text to the shell, which then parses and executes the command.


## uretprobe
It allows you to trace and collect information when a specific user-space function returns. uretprobe is particularly useful for understanding the behavior of user-space applications and for capturing the return values of functions.

Return Probes:

A return probe is triggered when a specified function exits.
It allows you to capture the state of the program at the point when the function returns, including its return value and other context-specific information.

- Example
‍‍```bash
bpftrace -e 'uretprobe:/path/to/executable:function_name {
    printf("Function returned with value: %d\n", retval);
}'
``

uretprobe:/path/to/executable:function_name:
This specifies the target function to probe. Replace /path/to/executable with the path to the user-space binary and function_name with the name of the function you want to trace.
printf("Function returned with value: %d\n", retval);:
This prints the return value of the specified function. retval is a special variable in BPFtrace that holds the return value of the probed function.


## Socket buffer

is sk_buff in the Linux kernel, a fundamental data structure used to manage network packets in the Linux networking stack. It is defined in the Linux kernel's networking code and serves as a container for network packets as they traverse through various layers of the network stack.

### Key Components of sk_buff

* Packet Data: The actual data of the network packet is stored in the buffer.
* Metadata: Information about the packet, such as protocol headers (IP, TCP, etc.), buffer lengths, and offsets, is included.
* Pointers: Pointers to various protocol headers (e.g., Ethernet, IP, TCP) within the packet data to facilitate easy access and manipulation.

### Structure
Here's a simplified explanation of the structure and fields of sk_buff:

Data Pointers:

- head: Pointer to the start of the buffer.
- data: Pointer to the start of the packet data.
- tail: Pointer to the end of the packet data.
- end: Pointer to the end of the buffer.

- Header Pointers:

  - network_header: Offset to the network layer header (e.g., IP header).
  - transport_header: Offset to the transport layer header (e.g., TCP/UDP header).
- Length Fields:

  - len: Total length of the packet data.
  - data_len: Length of the data payload.
  - mac_len: Length of the MAC header.

### Protocol Information:

Information about the protocol stack, such as protocol family (e.g., IPv4, IPv6), transport protocol (e.g., TCP, UDP), etc.
Usage
Socket buffers are used extensively in the Linux kernel for networking operations. 

* Here’s a typical flow:

Packet Reception: When a network packet arrives, it is placed into a socket buffer by the network interface card (NIC) driver.

Protocol Processing: The packet is processed by various network stack layers (e.g., Ethernet, IP, TCP). The socket buffer structure allows easy access to the relevant headers and payload.

Packet Transmission: When a packet is to be sent out, it is assembled into a socket buffer and handed off to the NIC driver for transmission.

* Example in the Script

In the provided script, sk_buff is used to access the network and transport layer headers of the packet to extract and display information about TCP reset packets.

```cpp
$skb = (struct sk_buff *)arg1;
$tcp = (struct tcphdr *)($skb->head + $skb->transport_header);
$ip = (struct iphdr *)($skb->head + $skb->network_header);
```

- $skb: The socket buffer pointer, which is cast from the first argument of the tcp_v4_send_reset function.
- $tcp: The TCP header pointer, calculated using the base address of the buffer (head) and the offset to the transport header (transport_header).
- $ip: The IP header pointer, calculated using the base address of the buffer (head) and the offset to the network header (network_header).


* Socket buffers are crucial for:

Buffer Management: Efficiently managing memory for network packets.
Protocol Independence: Allowing the network stack to process packets independently of the underlying hardware.
Flexibility: Enabling easy manipulation and inspection of network packets as they traverse the stack.


## conversion of port number

The calculation of the port number in the script involves converting the port number from network byte order (big-endian) to host byte order (which can be either little-endian or big-endian depending on the architecture). This process ensures that the port numbers are displayed correctly on the host machine.

Understanding Byte Order
Network Byte Order: Big-endian format, where the most significant byte (MSB) is stored at the lowest memory address.
Host Byte Order: Can be either little-endian or big-endian depending on the architecture. Most x86 architectures use little-endian, where the least significant byte (LSB) is stored at the lowest memory address.
Structure of Port Number
A port number in TCP is a 16-bit value. In network byte order (big-endian), the higher-order byte (most significant byte) is stored first, followed by the lower-order byte (least significant byte).

Conversion Process
Here’s the code for converting the port number from network byte order to host byte order:

```cpp
$dport = ($tcp->dest >> 8) | (($tcp->dest << 8) & 0xff00);
$sport = ($tcp->source >> 8) | (($tcp->source << 8) & 0xff00);
```
Let’s break down this conversion step by step:

Right Shift by 8 Bits:

1. ($tcp->source >> 8): This shifts the source port number 8 bits to the right. As a result, the lower-order byte is discarded, and the higher-order byte moves to the lower-order byte's position.
Left Shift by 8 Bits and Mask with 0xff00:

2. (($tcp->source << 8) & 0xff00): This shifts the source port number 8 bits to the left. As a result, the higher-order byte is discarded, and the lower-order byte moves to the higher-order byte's position. The & 0xff00 mask ensures that only the higher-order byte is considered.
Bitwise OR Operation:

3. ($tcp->source >> 8) | (($tcp->source << 8) & 0xff00): This combines the results of the previous two operations using a bitwise OR. The result is the port number in host byte order.

* Example
Assume the source port number in network byte order is 0x1234 (hexadecimal):

- Network Byte Order (Big-Endian): 0x12 0x34
- Host Byte Order (Little-Endian): 0x34 0x12
 
* Conversion Steps
1. Right Shift by 8 Bits:
0x1234 >> 8 results in 0x0012 (higher-order byte).

2. Left Shift by 8 Bits and Mask with 0xff00:
(0x1234 << 8) & 0xff00 results in 0x3400.

3. Bitwise OR Operation:
0x0012 | 0x3400 results in 0x3412.

Thus, 0x1234 in network byte order (big-endian) is converted to 0x3412 in host byte order (little-endian).

This conversion ensures that the port numbers are displayed correctly on the host system regardless of the byte order used by the network.


