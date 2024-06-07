# Init and Service Management in Linux

### Additional Points
- **Service Management Tools**: Common tools include `systemctl` for `systemd` and `service` or `update-rc.d` for `SysVinit`.
- **Monitoring Services**: Use `systemctl status` or `service status` to check the status of services.

## Init in Linux

### Definition
`init` is the first process started by the kernel, responsible for managing other processes.

### Implementations
- **SysVinit**: Traditional, script-based init system.
- **Upstart**: Event-driven, designed to replace SysVinit.
- **Systemd**: Modern, feature-rich init system used by most distributions.

### Additional Points
- **Systemd Advantages**: Faster boot times, better process management, and advanced logging with `journalctl`.
- **Upstart Usage**: Primarily found in older Ubuntu versions, replaced by `systemd` in recent releases.

## SysVinit

### Role
Manages the start of other processes.

### Configuration File
`/etc/inittab` contains instructions for `init`.

### Runlevels

#### Definition
States of the system post-boot, determining available services.

#### Runlevel Examples in Red Hat Enterprise Linux
- **0**: Halt (shutdown)
- **1**: Single-user mode (maintenance)
- **2**: Multi-user mode without networking (not commonly used)
- **3**: Multi-user mode with networking
- **4**: User-definable (rarely used)
- **5**: Multi-user mode with graphical interface
- **6**: Reboot

#### Commands
- **Check Current Runlevel**: `runlevel`
  - **Output**: `N 3` (N means no change since boot, second number is current runlevel)
- **Change Runlevel**: `telinit 5`

### Additional Points
- **Runlevel in systemd**: Uses targets instead of runlevels. Example: `multi-user.target` replaces runlevel 3.
  - **Check Target in systemd**: `systemctl get-default`
  - **Change Target in systemd**: `systemctl set-default graphical.target`

## chkconfig Command

### Purpose
Manages service runlevels in SysVinit systems.

### Check Service Status
`chkconfig --list`

### Set Service Status
Example: `chkconfig --levels 123 network on` # on levels 1 2 and 3 the network service must be on

### Boot Scripts Execution
Located in `/etc/rc.d/rc[runlevel_number].d/` or `/etc/init.d`.

Scripts start with `S` (start) or `K` (kill) followed by a number indicating execution priority.

### Additional Points
- **Systemd Equivalent**: Use `systemctl` commands such as `systemctl enable` and `systemctl disable`.
  - Example: `systemctl enable apache2` to start Apache at boot.

