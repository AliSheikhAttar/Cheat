# BPF Security - Short

* BCC:
(BPF Compiler Collection) provides tools and libraries to simplify the writing and running of eBPF programs.
****
- bpftrace: A high-level tracing language that simplifies the process of writing BPF programs for dynamic tracing. It is powerful, user-friendly, and - supports a variety of tracing capabilities.
- Tracepoints: Predefined static instrumentation points in the kernel, designed for low overhead and used primarily for monitoring and debugging specific kernel events.
- Kprobes: Dynamic instrumentation points that can be inserted at any location in the kernel code at runtime, offering greater flexibility but potentially higher overhead compared to tracepoints.


* BPF Helper:
printf is still using a BPF helper to format and send output to user space.
system is a bpftrace built-in function that calls a user-space command.

* bpf_send_signal():
Not used directly in this example. Instead, the kill command is executed from user space to send the signal.

* Perf Output Buffer:
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

* execve:
execve is a system call used in Unix-like operating systems to execute a new program. When a process calls execve, it replaces its current memory space with a new program, effectively transforming into the new process.
The typical flow of creating a new process involves:
fork or clone: These syscalls create a new process by duplicating the calling process.
execve: The newly created process then calls execve to execute a different program.

* Binary Files: Executable and Linking Format (ELF)
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

* Uses of ELF Files
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


* uretprobe
It allows you to trace and collect information when a specific user-space function returns. uretprobe is particularly useful for understanding the behavior of user-space applications and for capturing the return values of functions.

Return Probes:

A return probe is triggered when a specified function exits.
It allows you to capture the state of the program at the point when the function returns, including its return value and other context-specific information.

- Example
‍‍```bash
bpftrace -e 'uretprobe:/path/to/executable:function_name {
    printf("Function returned with value: %d\n", retval);
}'
````

uretprobe:/path/to/executable:function_name:
This specifies the target function to probe. Replace /path/to/executable with the path to the user-space binary and function_name with the name of the function you want to trace.
printf("Function returned with value: %d\n", retval);:
This prints the return value of the specified function. retval is a special variable in BPFtrace that holds the return value of the probed function.