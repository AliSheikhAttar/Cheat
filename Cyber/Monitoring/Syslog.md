## Syslog
Syslog is an industry-standard protocol that allows you to have any systems, devices, and applications that support syslog send log messages to a central syslog server so that you can centrally review and manage your logs. Syslog can be configured on your switches, routers, servers, firewalls, and intrusion detection systems (IDSs) to send logged events to the syslog server.

The data is sent from the system or device to the syslog server via:

UDP/514
TCP/6514

these ports are on the syslog server

| Log Level | Message | Description |
|-----------|---------|-------------|
0 | Emergency (system unstable) | The system is unusable, a catastrophic failure has occurred. Immediate action is needed.
1 | Alert | A situation requiring immediate attention, such as a failure in a critical system.
2 |	Critical | A severe issue that affects functionality, but the system is still operational.
3 |	Error | An error that has occurred in the system, but it doesn't necessarily cause a halt in operation.
4 |	Warning | A warning indicating a potential issue that requires attention but isn't immediately critical.
5 |	Notification | A normal but significant condition or event has occurred, worth being aware of.
6 |	Information | Informational messages providing routine information, such as successful operations.
7 |	Debugging | Detailed debugging messages used to troubleshoot issues. High verbosity for developers or administrators.


- Send switch logs to syslog server
```bash
enable
```
This command switches the router from user EXEC mode to privileged EXEC mode.
In privileged mode, you can run more advanced commands and access configuration options.
R1 is the hostname of the device (router or switch).

```bash
config term
```
This command puts the device into global configuration mode.
In this mode, you can change system-wide settings, such as syslog, routing protocols, interfaces, etc.
The prompt changes to R1(config) to indicate that you are in global configuration mode.

```bash
logging host 10.0.0.5 #syslog server address
```
This command tells the device to send log messages to the syslog server located at IP address 10.0.0.5.
This IP address refers to the remote syslog server where the logs will be sent and stored.
R1(config) # logging trap 3

```bash
logging trap 3
```
This command sets the syslog logging level to 3, which is Error level, based on the syslog severity levels.
This means the device will only send log messages with a severity of 3 (Error) or higher (i.e., Critical, Alert, and Emergency) to the syslog server. It will ignore lower-priority messages like warnings or informational logs.

