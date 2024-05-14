# Linux System

## ["Directories.md"](/Linux/System/Directories.md)
- service and processes most using cpu

```bash
Top 
```
- Procceses
  -  Search processes
      ```bash
        ps -[option]
      ```
        - -a – show processes for all users.
        - -u – display the current user’s processes.
        - -x – include processes without a terminal.
        - -e – list all processes in the system, regardless of the owner or controlling terminal. 
        - -H – formats the CMD column’s data to display the parent-child relationship between processes.
        - -axjf – prettier output with a few more columns.
        - man ps – more human
      
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
          - -l – List the process names and the PIDs.
          - -n – returns only the newest instance among the matching processes. 
          - -o – returns only the oldest instance among the matching processes.
          - -u – matches processes that the specified user owns.
          - -x – Only find processes that exactly match the given pattern.


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

    - kill all the processes containing the process name <pname>
    ```bash
    pkill <pname> [option]
    ```
      - -u [username] – kills processes owned by a specific user.
      - -t [terminal] – kills processes attached to a specific terminal.
      - -l – provides a detailed process list along with the PID.
      - -n. Only kill the newest of the processes that are discovered.
      - -o. Only kill the oldest of the processes that are discovered.
      - -x. Only kill the processes that match the pattern exactly.
      - -signal. Send a specific signal to the process, rather than SIGTERM.

    - closes a given server's connection to clients. The syntax of the xkill command is;
    If a server has opened some unwanted processes, xkill aborts these processes.
    ```bash
    xkill <resource>
    ```

    - kill/terminate all processes named <pname>
    ```bash
    killall <pname> [option]
    ```
    - -e: This option specifies that the process name should match exactly. If this option is not used, "killall" will match any process name that contains the specified string.
    - -i: This option prompts the user before killing each process.
    - -s signal: This option allows you to specify a common signal to send to the background process. The default signal is SIGTERM.
    - -I. Ignore the case when trying to find the process name.
    - -u. Only kill processes owned by a specific user.
    - -v. Report back on whether the process has been successfully killed.
    - -o [time] – only kills processes older than the specified time.
    - -y [time] – only kills processes newer than the specified time.

    - Ex: terminates all currently running processes named chrome that have been running for longer than 30 minutes:
    ```bash
    killall -o 30m chrome
    ```
- change ownership of directories
```bash
  sudo chown -c -R $USER:$USER <directory>
```
Explanation:
chown: change the ownership of files/directories
-c: report all changes
-R: do this recursively (for all files/directories beneath the given one)
$USER:$USER: change the owner and the group that owns the the entry to the user that issues the command (sudo preserves the values)
$HOME: do this with your home directory
You can test those environment variables with the following commands

echo $USER
sudo echo $USER
echo $HOME
sudo echo $HOME


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

