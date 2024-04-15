# Linux System
- service and processes most using cpu

```bash
Top 
```
- Procceses
  -  Search processes
  ```bash
  - ps -[option]
  ```
    - -a – show processes for all users.
    - -u – display the current user’s processes.
    - -x – include processes without a terminal.

  - processes with specific name
  ```bash
  ps -aux | grep <process name>
  ```
  - finds the PID of a process by its name.
    - ```bash
      pidof -[option] <processname>
      ```
      - -c – ensures that only PIDs from the current root directory are returned.
      - -o – omits the specified PIDs from the results.
      - -s – returns only a single PID, typically the oldest, among the matching processes.


    - ```bash
      pgrep -[option] [pattern]
      ```
      - -n – returns only the newest instance among the matching processes. 
      - -o – returns only the oldest instance among the matching processes.
      - -u – matches processes that the specified user owns.


  - Kill
  ```bash
  kill -l
  ```
    - SIGTERM (15) – this is the default and safest way to kill a running process in Linux. It allows the process to terminate gracefully.
    - SIGKILL (9) – this signal immediately stops any primary or background process without allowing it to clean up.
    - SIGSTOP (19) – pauses a current process without terminating it.
    - SIGHUP (1) – this signal reports that the user’s terminal is disconnected, often leading to the process’s termination.
    - SIGINT (2) – this signal interrupts a process, typically sent from the keyboard shortcut Ctrl+C.

  ```bash
  kill -[option(15, 9, 19, 1, 2)] <pid>
  ```
  - sigkill
  ```bash
  kill -9 <pid>
  ```

  - kill multiple
  ```bash
  kill <pid1> <pid2> ...
  ```

  - kill with patter
  ```bash
  kill $(pgrep pattern)
  ```

  - change ownership of directories
  ```bash
    sudo chown newuser filename
  ```

  - kill all the processes containing the process name <pname>
  ```bash
  pkill apache <pname> [option]
  ```
    - -u [username] – kills processes owned by a specific user.
    - -t [terminal] – kills processes attached to a specific terminal.
    - -l – provides a detailed process list along with the PID.


  - kill/terminate all processes named <pname> [option]
  ```bash
  killall apache <pname>
  ```
  -o [time] – only kills processes older than the specified time.
  -y [time] – only kills processes newer than the specified time.

  - Ex: terminates all currently running processes named chrome that have been running for longer than 30 minutes:
  ```bash
  killall -o 30m chrome
  ```

- Service
  - Systemctl
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

  - ```bash 
      sudo service start <Service>
    ```
  - 

  - ```bash 
    sudo service status <Service>
  ```
  - 

  - ```bash 
    sudo service stop <Service>
  ```
  - 

