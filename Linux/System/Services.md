# Services

## Services in Linux

### Definition
Services are background programs with specific purposes, such as managing databases or handling web requests,
running or waiting to run.

### Characteristics of Services
- **No GUI**: Managed via the command line.
- **Start Behavior**: Can start at boot or manually.
- **Background Operation**: Often wait for events or signals to perform tasks.


### Systemctl
- ```bash 
    systemctl start <Service> 
  ```
- ```bash 
    systemctl status <Service> 
  ```
- ```bash 
    systemctl stop <Service> 
  ```
- start on boot 
  ```bash 
    systemctl enable <Service> 
  ```
- ```bash 
    systemctl disable <Service> 
  ```
- ```bash 
    systemctl is-enabled <Service>
  ```
- 
    - enabled: The service is enabled and set to start at boot.
    - disabled: The service is disabled and won't start at boot.
    - static: The service is enabled but is not meant to start on its own.
- start on boot services 
  ```bash 
      systemctl list-unit-files --state=enabled --type=service
  ```


#### Create service
```bash
    sudo nano /etc/systemd/system/startup_asa.service
```

```bash
[Unit]
Description=asa startup
After=graphical.target

[Service]
Type=simple
ExecStart=/home/asa/startup_asa.sh #(Path to script)
Restart=always
Environment=DISPLAY=:0 # $(DISPLAY)
Environment=XAUTHORITY=/home/asa/.Xauthority # $(XAUTHORITY)
User=asa
Group=asa

[Install]
WantedBy=graphical.target #runlevel
```
```bash
sudo systemctl daemon-reload
```



### Additional Points
- **Service Management Tools**: Common tools include `systemctl` for `systemd` and `service` or `update-rc.d` for SysVinit.
- **Monitoring Services**: Use `systemctl status` or `service status` to check the status of services.

## SysVinit

### Role
Manages the start of other processes.

### Commands for Managing Services in SysVinit
- List services
```bash
service --status-all
```
- start
```bash 
    sudo service start <Service>
```
- status
```bash 
  sudo service status <Service>
```
- stop
```bash 
  sudo service stop <Service>
```
- 
## Upstat
* If the /usr/share/upstart directory exists on your system, you are using Upstart.

### Job Files
All jobs executed by Upstart are located in /etc/init as .conf files:
```bash
root@Myserver:~# ls /etc/init
acpid.conf            mountnfs.sh.conf
alsa-restore.conf     mtab.sh.conf
alsa-state.conf       networking.conf
alsa-store.conf       network-interface.conf
anacron.conf          network-interface-container.conf
```
- View jobs ` initctl list `
- shutdown stop/waiting ` console stop/waiting `
- View specific job ` initctl status networking networking start/running ` 
- Manually start a job `sudo initctl start networking ` 
- Manually stop a job ` sudo initctl stop networking ` 
- Manually restart a job ` sudo initctl restart networking ` 
- anually emit an event ` sudo initctl emit some_event `

## Systemd

Another service management system currently used by most distributions is systemd. If the /usr/lib/system directory exists on your system, you are likely using systemd.

systemd was designed to address issues found in the init (SysV) system. It runs processes simultaneously during system boot to reduce boot time and resource consumption.

Features of Systemd
* Simultaneous Process Execution: Runs processes in parallel during boot.
* Logging: Uses journald to store logs in a binary format.
* User Session Control: Manages user logins with systemd-login.
* System Event Logging: Can be used for system event logging similar to syslog.
* Commands for Managing Services with Systemd
  
- List units: ` sudo systemctl list-units `
- View status of unit: ` sudo systemctl status networking.service `
- Start a service: ` sudo systemctl start networking.service `
- Stop a service: ` sudo systemctl stop networking.service `
- Restart a service: ` sudo systemctl restart networking.service `
- Enable a unit: ` sudo systemctl enable networking.service `
- Disable a unit: ` sudo systemctl disable networking.service `

### Example: SSH Service Configuration in Systemd
Configuration File:
/lib/systemd/system/ssh.service

[SSH Config](./SSH_Config.png)

- **[Unit]**
- Description: A short description of the service.
- Documentation: Path to the documentation for the unit.
- Before: List of units that should start after this unit.
- After: List of units that should start before this unit.
- Parameters in the [Service] Section
- **[Service]**
- Type: Indicates the start-up type of the service.
- ExecStartPre: Command to execute before starting the process.
- ExecStart: Command to start the process.
- ExecStartPost: Command to execute after starting the process.
- ExecStop: Command to stop the process.
- ExecReload: Command to reload the process.
- Restart: Defines when the service should automatically restart.
- PIDFile: File that contains the PID of the process.
- KillMode: Method used to kill the process.
- KillSignal: Signal used to stop the service.
- User: Username under which the service should run.
- Group: System group under which the service should run.
- TimeoutStopSec: Time to wait for the process to stop before attempting to kill it.
- **[Install]**
- RequiredBy: List of units that require this service to run.
- WantedBy: Targets or runlevels where this unit should be started, such as during shutdown or when the system enters multi-user runlevel.