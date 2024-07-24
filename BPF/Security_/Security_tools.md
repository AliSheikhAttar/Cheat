# Toolz

![tools](tools.png)

| Tool          | Source    | Target   | Description                                |
|---------------|-----------|----------|--------------------------------------------|
| execsnoop     | BCC/BT    | Syscalls | List new process execution                 |
| elfsnoop      | Book      | Kernel   | Show ELF file loads                        |
| modsnoop      | Book      | Kernel   | Show kernel module loads                   |
| bashreadline  | BCC/BT    | bash     | List entered bash shell commands           |
| shellsnoop    | Book      | shells   | Mirror shell output                        |
| ttysnoop      | BCC/book  | TTY      | Mirror tty output                          |
| opensnoop     | BCC/BT    | Syscalls | List files opened                          |
| eperm         | Book      | Syscalls | Count failed EPERM and EACCES syscalls     |
| tcpconnect    | BCC/BT    | TCP      | Trace outbound TCP connections (active)    |
| tcpaccept     | BCC/BT    | TCP      | Trace inbound TCP connections (passive)    |
| tcpreset      | Book      | TCP      | Show TCP send resets: port scan detection  |
| capable       | BCC/BT    | Security | Trace kernel security capability checks    |
| setuids       | Book      | Syscalls | Trace the setuid syscalls: privilege escalation |

## execsnoop
it is a BCC and bpftrace tool to trace new processes,
and can be used to identify suspicious process execution. Example output:
```bash
# execsnoop
PCOMM PID   PPID RET ARGS
ls    7777  21086 0 /bin/ls -F
a.out 7778  21086 0 /tmp/a.out
[...]
```
- PCOMM: Process name of the command being executed.
- PID: Process ID of the executing process.
- PPID: Parent Process ID from which the process is spawned.
- RET: Return code from the execve syscall (0 indicates success).
- ARGS: The command-line arguments passed to the process.

This shows a process executing from /tmp named a.out.
execsnoop(8) works by tracing the execve syscall. This is a typical step in the creation of new
processes, which begins by calling fork or clone to create a new process and calls execve to
execute a different program. Note that this is not the only way new software can execute: a buffer
overflow attack can add new instructions to an existing process, and execute malicious software
without needing to call execve

## elfsnoop
traces the execution of ELF binaries by attaching to a key point in the kernel where all ELF executions must pass. This is typically done by instrumenting the kernel functions responsible for loading and executing ELF binaries.
elfsnoop works by tracing the load_elf_binary() function in the Linux kernel.
This function is responsible for loading ELF binaries into memory for execution.
By tracing this function, elfsnoop can capture every ELF binary execution event.


- TIME: Timestamp as HH:MM:SS.
- PID: Process ID.
- INTERPRETER: For scripts, the interpreter that was executed.
- FILE: Executed file.
- MOUNT: Mount point for the executed file.
- INODE: Index node number for the executed file: with the mount point, this forms a
unique identifier.
- RET: Return value from the attempted execution. 0 is success.

### Security Implications of elfsnoop
- Detection of Malicious Activity
elfsnoop can be a critical tool for identifying and mitigating malicious activity on a Linux system. It achieves this by providing detailed information about every ELF binary execution, which includes attributes that are difficult for attackers to spoof. Here’s a deeper look at how elfsnoop aids in security:

**Monitoring Executed Binaries**
- Real-Time Monitoring:

elfsnoop traces every execution of ELF binaries in real-time, allowing system administrators to observe all running processes as they happen.
This real-time insight is crucial for identifying and responding to suspicious activities promptly.

- Detailed Execution Logs:

By logging detailed information such as timestamp, process ID (PID), file path, mount point, inode number, interpreter, and return value, elfsnoop creates a comprehensive record of all executed binaries.
This log can be analyzed to detect unusual patterns or executions that deviate from the norm, which may indicate malicious activity.
Unique Mount Point and Inode Combination

**Mount Point**
The mount point indicates the file system location where the binary is stored.
Even if an attacker creates a malicious binary with the same name and path as a legitimate one, the mount point may differ, providing a clue that something is amiss.

**Inode Number**
An inode number is a unique identifier for a file within a file system.
Combining the mount point and inode number forms a unique identifier for the executed file.
An attacker would find it extremely difficult to match both the mount point and inode number of a legitimate system binary.
Examples of Malicious Activity Detection

**Spoofed System Binaries**

Attackers often replace system binaries (like /bin/ls or /usr/bin/ssh) with their own versions to gain unauthorized access or control.
elfsnoop can detect these replacements by logging the mount point and inode of the executed binary. If these details do not match the known, legitimate binaries, it signals a potential compromise.

- Unauthorized Script Executions:

Scripts executed with unauthorized interpreters (e.g., a script running with /bin/sh instead of /bin/bash) can be a sign of an attack.
elfsnoop logs the interpreter used for each script, making it easier to spot such deviations.

- Unusual Execution Locations:

Legitimate binaries are typically executed from standard directories like /bin, /usr/bin, etc.
Executions from unusual locations (e.g., /tmp, /var/tmp) can be indicative of malicious activities.
elfsnoop provides the file path and mount point, helping identify such anomalies.

Real-World Use Case
Imagine a scenario where an attacker has gained access to a Linux server and replaced /usr/bin/ssh with a malicious version:

Normal Execution:

Legitimate ssh:
Mount Point: /usr
Inode: 5678
When executed, elfsnoop logs:
```bash
TIME     PID   INTERPRETER   FILE   MOUNT     INODE    RET
14:22:15 1123  /usr/bin/ssh          /usr      5678     0
```
After Compromise:

Malicious ssh:
Mount Point: /tmp
Inode: 1234
When executed, elfsnoop logs:
```bash
TIME     PID   INTERPRETER   FILE                MOUNT     INODE    RET
14:45:30 2345                /usr/bin/ssh        /tmp      1234     0
```
Detection:

The administrator notices the unusual mount point /tmp and a different inode for ssh, indicating a potential security breach.


```bash
#!/usr/local/bin/bpftrace
#include <linux/binfmts.h>
#include <linux/fs.h>
#include <linux/mount.h>
BEGIN
{
printf("Tracing ELF loads. Ctrl-C to end\n");
printf("%-8s %-6s %-18s %-18s %-10s %-10s RET\n",
"TIME", "PID", "INTERPRETER", "FILE", "MOUNT", "INODE");
}
kprobe:load_elf_binary #Sets a kernel probe (kprobe) on the load_elf_binary function, which is responsible for loading ELF binaries.
{
@arg0[tid] = arg0; #Stores the first argument (arg0) of the function call in a BPF map using the thread ID (tid) as the key.

}
kretprobe:load_elf_binary # Sets a return probe (kretprobe) on the load_elf_binary function, which triggers when the function returns.

/@arg0[tid]/ # The conditional (/@arg0[tid]/) ensures this block runs only if there is an entry for the current thread ID in the @arg0 map.
{
$bin = (struct linux_binprm *)@arg0[tid]; # Casts the stored arg0 value to a struct linux_binprm pointer to access the ELF binary's properties.
time("%H:%M:%S ");
printf("%-6d %-18s %-18s %-10s %-10d %3d\n", pid,
str($bin->interp), str($bin->filename),
str($bin->file->f_path.mnt->mnt_root->d_name.name),
$bin->file->f_inode->i_ino, retval);
# Output Columns
# TIME: The current time in "HH:MM
# " format.
# PID: The process ID of the process loading the ELF binary.
# INTERPRETER: The ELF interpreter path.
# FILE: The path of the ELF file being loaded.
# MOUNT: The root name of the mount point.
# INODE: The inode number of the ELF file.
# RET: The return value of the load_elf_binary function.
delete(@arg0[tid]); # Deletes the entry for the current thread ID from the @arg0 map to clean up.
}
```
**Summary**
elfsnoop enhances security by providing a detailed, real-time audit trail of all executed ELF binaries. By leveraging the unique combination of mount points and inode numbers, elfsnoop makes it significantly harder for attackers to disguise their activities. This tool is invaluable for detecting unauthorized modifications, unusual execution patterns, and potential security breaches, thereby helping maintain the integrity and security of a Linux system.

## modsnoop
modsnoop(8)5 is a bpftrace tool to show kernel module loads. For example:
```bash
# modsnoop.bt
Attaching 2 probes...
Tracing kernel module loads. Hit Ctrl-C to end.
12:51:38 module init: msr, by modprobe (PID 32574, user root, UID 0)
[...]
```
This shows that at 10:50:26 the "msr" module was loaded by the modprobe(8) tool, with UID 0.
‍‍‍- Script
```bash
#!/usr/local/bin/bpftrace
#include <linux/module.h>
BEGIN
{
printf("Tracing kernel module loads. Hit Ctrl-C to end.\n");
}
kprobe:do_init_module
{
$mod = (struct module *)arg0;
time("%H:%M:%S ");
printf("module init: %s, by %s (PID %d, user %s, UID %d)\n",
$mod->name, comm, pid, username, uid);
}
```
This works by tracing the do_init_module() kernel function, which can access details from the
module struct.
There is also a module:module_load tracepoint, used by later one-liners

## bashreadline
bashreadline is a BCC and bpftrace tool to trace interactively entered commands in the bash
shell, system-wide. For example, running the BCC version:
```bash
# bashreadline
bashreadline
TIME PID COMMAND
11:43:51 21086 ls
11:44:07 21086 echo hello book readers
11:44:22 21086 eccho hi
11:44:33 21086 /tmp/ls
[...]
```
This output shows commands that were entered while tracing, including shell built-ins (echo)
and commands that failed (eccho). This works by tracing the readline() function from the bash shell, 
so any entered command will be shown. Note that while this can trace commands across all
shells running on the system, it cannot trace commands by other shell programs, and an attacker
may install their own shell (e.g., a nanoshell) that is not traced.

bpftrace script
```bash
#!/usr/local/bin/bpftrace
BEGIN
{
printf("Tracing bash commands... Hit Ctrl-C to end.\n");
printf("%-9s %-6s %s\n", "TIME", "PID", "COMMAND");
}
uretprobe:/bin/bash:readline
{
time("%H:%M:%S
");
printf("%-6d %s\n", pid, str(retval));
}
```
This traces the readline() function in /bin/bash using a uretprobe.
Some Linux distributions build bash differently 
such that readline() is used from the libreadline library instead;


## shellsnoop
Shellsnoop is an eBPF-based tool designed for monitoring and logging shell commands executed on a system. 
It operates by attaching eBPF programs to specific system calls, such as execve, which are used to execute programs.

**Key Features of Shellsnoop**
- Monitors Executed Commands: Captures details of shell commands at the point of execution, providing insight into the commands run on a system.
- System-Wide Scope: Capable of monitoring commands from any shell or executable, not limited to a specific shell like bash.
- Efficient Operation: Utilizes eBPF technology to run lightweight programs in kernel space, ensuring minimal performance overhead.
- Detailed Logging: Logs information such as the command executed, user ID, process ID, and other relevant metadata, useful for auditing and security monitoring.
- Security and Compliance: Helps in auditing user activities, detecting unauthorized or suspicious behavior, and ensuring compliance with security policies.

**Use Cases**
- Security Monitoring: Tracks executed commands to detect potential security breaches or unauthorized actions.
- Auditing: Provides a log of executed commands for post-incident analysis and compliance verification.
- Intrusion Detection: Identifies unusual or malicious command executions to help in preventing security incidents.

Example Usage:

```bash
sudo shellsnoop
```


```bash
#!/usr/local/bin/bpftrace   Purpose: Specifies the path to the BPFtrace interpreter, which will execute this script.
BEGIN # This block runs at the start of the script execution.
/$1 == 0/ # checks if no PID argument is provided (i.e., if $1 is zero or not set).
{
printf("USAGE: shellsnoop.bt PID\n"); # prints usage information to indicate how to use the script.
exit(); # exits the script if no PID is provided.
}
tracepoint:sched:sched_process_fork # This tracepoint triggers on the fork system call, which is used to create new processes.
/args->parent_pid == $1 || @descendent[args->parent_pid]/
# args->parent_pid == $1: Checks if the parent PID of the new process matches the PID provided to the script.
# @descendent[args->parent_pid]: Checks if the parent PID is already marked as a descendant.
{
@descendent[args->child_pid] = 1;
#Marks the child PID as a descendant by adding it to the @descendent associative array. This array tracks the PIDs of all descendant processes.
# Trace Writes to STDOUT and STDERR
# bpftrace
}
tracepoint:syscalls:sys_enter_write # This tracepoint triggers on the write system call, which is used to write data to file descriptors.
/(pid == $1 || @descendent[pid]) && (args->fd == 1 || args->fd == 2)/ 
# Checks if the current process PID matches the provided PID or is a descendant.
# Checks if the file descriptor is either 1 (STDOUT) or 2 (STDERR).
{
printf("%s", str(args->buf, args->count));
# Prints the data being written to STDOUT or STDERR. str(args->buf, args->count) converts the buffer being written into a string, truncated to BPFTRACE_STRLEN (64 bytes by default).
```

**Summary of code**
Initialization: The script begins by checking if a PID is provided. If not, it prints usage information and exits.
Fork Monitoring: It tracks when processes fork (create child processes) and marks these child processes as descendants of the original PID.
Output Logging: It monitors write system calls from the specified process and its descendants, capturing and printing data written to STDOUT and STDERR.
