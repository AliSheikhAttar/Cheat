# CMDZ

## trace command execution
```bash
bpftrace -e 'tracepoint:syscalls:sys_enter_execve { printf("Command executed: PID %d, Comm %s, Filename %s\n", pid, comm, str(args->filename)); }'
```

