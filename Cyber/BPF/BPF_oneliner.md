# BPF one-Liner

BPF (Berkeley Packet Filter) one-liners are concise commands used to perform specific tracing and monitoring tasks on Unix-like systems. These one-liners can be written using either BCC (BPF Compiler Collection) or bpftrace, each with its own syntax and capabilities. Here's a detailed breakdown of the one-liners provided:

## BCC One-Liners
### Count Security Audit Events for a Specific PID
```bash
funccount -p 1234 'security_*'
```
- Purpose: Counts the occurrences of security audit events for the process with PID 1234.
- Explanation:
funccount: A BCC tool that counts function calls.
  - -p 1234: Filters the events to only those occurring in the process with PID 1234.
  - 'security_*': A wildcard pattern that matches all security-related functions.

### Trace PAM Session Starts
```bash
trace 'pam:pam_start "%s: %s", arg1, arg2'
```
- Purpose: Traces the start of Pluggable Authentication Module (PAM) sessions.
- Explanation:
  - trace: A BCC tool for tracing function calls and their arguments.
  - 'pam:pam_start "%s: %s", arg1, arg2': Specifies the function to trace (pam_start in the PAM library) and the format of the output, printing two arguments arg1 and arg2.
  
### Trace Kernel Module Loads
```bash
trace 't:module:module_load "load: %s", args->name'
```
- Purpose: Traces the loading of kernel modules.
- Explanation:
  - trace: Again, a BCC tool for tracing.
  - 't:module:module_load "load: %s", args->name': Specifies the tracepoint for module loading and prints the name of the module being loaded (args->name).

## bpftrace One-Liners

### Count Security Audit Events for a Specific PID
```bash
bpftrace -e 'k:security_* /pid == 1234 { @[func] = count(); }'
```
- Purpose: Counts the occurrences of security audit events for the process with PID 1234.
- Explanation:
  - bpftrace -e: Executes a one-liner script.
  - 'k:security_* /pid == 1234 { @[func] = count(); }':
  - k:security_*: Matches all kernel functions that start with security_.
  - /pid == 1234: Conditional statement to filter events for PID 1234.
  - { @[func] = count(); }: Aggregates the count of events per function name.

### Trace PAM Session Starts
```bash
bpftrace -e 'u:/lib/x86_64-linux-gnu/libpam.so.0:pam_start { printf("%s: %s\n", str(arg0), str(arg1)); }'
```
- Purpose: Traces the start of Pluggable Authentication Module (PAM) sessions.
- Explanation:
  - bpftrace -e: Executes a one-liner script.
  - 'u:/lib/x86_64-linux-gnu/libpam.so.0:pam_start { printf("%s: %s\n", str(arg0), str(arg1)); }':
  - u:/lib/x86_64-linux-gnu/libpam.so.0:pam_start: User-space probe in the PAM library.
  - { printf("%s: %s\n", str(arg0), str(arg1)); }: Prints the first two string arguments (arg0 and arg1).

### Trace Kernel Module Loads
```bash
bpftrace -e 't:module:module_load { printf("load: %s\n", str(args->name)); }'
```
- Purpose: Traces the loading of kernel modules.
- Explanation:
  - bpftrace -e: Executes a one-liner script.
  - 't:module:module_load { printf("load: %s\n", str(args->name)); }':
  - t:module:module_load: Tracepoint for kernel module load events.
  - { printf("load: %s\n", str(args->name)); }: Prints the name of the module being loaded.

## Summary
BCC: Uses predefined tools like funccount and trace to perform tracing tasks. It often requires specifying function names or tracepoints directly and can print specific arguments.
bpftrace: Provides a flexible scripting environment for writing custom probes. It allows for more complex logic and data manipulation directly in the one-liner.

### Example
#### Example 1: Counting Security Audit Events
Command:
```bash
# funccount -p 21086 'security_*'
```
Output:
```bash
Tracing 263 functions for "security_*"... Hit Ctrl-C to end.
^C
FUNC                             COUNT
security_task_setpgid            1
security_task_alloc              1
security_inode_alloc             1
security_d_instantiate           1
security_prepare_creds           1
security_file_alloc              2
security_file_permission         13
security_vm_enough_memory_mm     27
security_file_ioctl              34
Detaching...
```

Explanation:

**Command Breakdown**:
funccount: A BCC tol that counts the number of times functions are called.
-p 21086: Specifies the process ID (PID) to filter the function calls for this particular process (PID 21086 in this case).
'security_*': Uses a wildcard to match all functions that start with security_.

****Output Explanation****:
The tool traces 263 functions that match the pattern security_*. These are part of the Linux Security Module (LSM) hooks, which handle and audit security events.
Each line in the output lists a function name and the count of how many times it was called.
For example, security_file_ioctl was called 34 times, indicating frequent security checks related to file ioctl operations.

**Use Case**:
This command is useful for monitoring and auditing security-related activities in the system. It helps in understanding how often specific security hooks are being triggered, which can be crucial for security analysis and troubleshooting.
Example 2: Tracing PAM Session Starts
Command:
```bash
# trace 'pam:pam_start "%s: %s", arg1, arg2'
```

Output:

```bash
PID    TID    COMM     FUNC              -
25568  25568  sshd     pam_start         sshd: bgregg
25641  25641  sudo     pam_start         sudo: bgregg
25646  25646  sudo     pam_start         sudo: bgregg
[...]
```

Explanation:

**Command Breakdown**:
trace: A BCC tool used to trace function calls and print their arguments.
'pam:pam_start "%s: %s", arg1, arg2': Specifies to trace the pam_start function in the PAM library and print its first two arguments (arg1 and arg2) as formatted strings.

**Output Explanation**:
The output lists processes starting PAM sessions.
Columns in the output:
- PID: Process ID of the calling process.
- TID: Thread ID of the calling thread.
- COMM: Command name, i.e., the name of the process.
- FUNC: Function name, which is pam_start in this case.
The output also shows the arguments passed to pam_start. For example, sshd: bgregg indicates that the sshd process started a PAM session for the user bgregg.

**Use Case**:
This command is useful for monitoring authentication events in real-time. It helps in understanding which processes are initiating PAM sessions and for which users.
It's particularly valuable for security audits and troubleshooting authentication issues.

**Summary**
These examples demonstrate the power of BCC one-liners for tracing and monitoring system activities. By counting security audit events and tracing PAM session starts, system administrators and security professionals can gain valuable insights into the security and authentication mechanisms of their systems. The simplicity and efficiency of BCC tools make them highly effective for real-time monitoring and analysis.






