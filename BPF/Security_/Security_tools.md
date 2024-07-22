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