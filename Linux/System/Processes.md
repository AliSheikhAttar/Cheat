# Processes
 
## OS
- name of OS
```bash
uname <option>
```
- option
- -s : name of kernel
- -v : version of kernel
- -r : release of kernel
- -a : all system info

## States of process
* R => Running or Runnable
* D => Uninterruptible Sleep
* S => Interruptable Sleep
* T => Stopped
* Z => Zombie

## list processes
```bash
top # top consuming
htop # top consuming more human
ps aux
```


### Output
- **PID Column**: Unique identifier for each process.
- **USER Column**: The user running the process (note that the process's permissions are limited to those of this user).
- **PRI Column**: Process priority in the kernel.
- **NI Column**: User-space priority of the process (commonly known as Niceness). default = 0
- **VIRT Column** (equivalent to VSZ in the `ps` command): The amount of memory requested by the process (the entire amount might not be used by the process).
- **RES Column** (equivalent to RSS in the `ps` command): The amount of memory currently used by the process.
- **SHR Column**: The amount of shared memory used by the process.
- **S Column**: The current state of the process.
- **%CPU Column**: The percentage of CPU usage by the process.
- **%MEM Column**: The percentage of memory usage by the process.
- **+TIME Column**: The elapsed time since the process started.
- **Command Column**: The command of the process.

### options
- -s <column> : sort by column
- -u <user>   : belong to <user>

### Interaction

| Key  | Operation |
|------|-----------|
| F9   | Kill a process |
| F8   | Increase Nice value by one unit (requires `sudo` if running `htop`) |
| F7   | Decrease Nice value by one unit (requires `sudo` if running `htop`) |
| F6   | Sort processes by the selected column |
| F5   | Display processes in a tree format |
| F4   | Filter processes by name |
| F3   | Search for a process |
| F2   | Settings |
| F1   | Help |



## Control
- watch current shell processses
```bash
jobs 
```
- transfer process to background
```bash
bg JOB
```
- transfer process to foreground
```bash
fg JOB
```

##  Process status
  ```bash
    ps -[option]
  ```
    - -a – show processes for all users.
    - -u – more infos like resource usage, process owner etc. .
    - -x – include processes without a terminal.
    - -e/-A – list all processes in the system, regardless of the owner or controlling terminal or current shell. 
    - -H – formats the CMD column’s data to display the parent-child relationship between processes.
    - -T – tree structered
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

- **USER Column**: The user running the process (note that the process's permissions are limited to those of this user).
- **PID Column**: Unique identifier for each process.
- **%CPU Column**: The percentage of CPU usage by the process.
- **%MEM Column**: The percentage of memory usage by the process.
- **VSZ Column** (equivalent to VIRT in the `htop` command): The amount of memory used in bytes.
- **RSS Column** (equivalent to RES in the `htop` command): The amount of RAM used in kilobytes.
- **TTY Column**: The type of terminal in use.
- **STAT Column**: The state of each process.
- **START Column**: The time the process started.
- **TIME Column**: The amount of time the process has been running.
- **COMMAND Column**: The command of the process.


```bash 
pgrep [options] pattern
```
- DESCRIPTION
> pgrep looks through the  currently  running  processes  and  lists  the
>process IDs which match the selection criteria to stdout.  All the cri‐
>teria have to match.  For example,
```bash
      $ pgrep -u root sshd
```
> will only list the processes called sshd AND owned  by  root.   On  the
> other hand,
```bash
      $ pgrep -u root,daemon
```
> will list the processes owned by root OR daemon.
> pkill  will  send  the  specified  signal  (by default SIGTERM) to each
>process instead of listing them on stdout.
>pidwait will wait for each process instead of listing them on stdout.



## Kill
  ```bash
  kill -l
  ```
    - SIGTERM (15) – this is the default and safest way to kill a running process in Linux. It allows the process to terminate gracefully.can be achived also by Ctr+c.
    - SIGKILL (9) – this signal immediately stops any primary or background process without allowing it to clean up.can be achived also by Ctr+z.
    - SIGSTOP (19) – pauses a current process without terminating it.can be achived also by Ctr+z.
    - SIGHUP (1) – this signal reports that the user’s terminal is disconnected, often leading to the process’s termination.
    - SIGINT (2) – this signal interrupts a process, typically sent from the keyboard shortcut Ctrl+C.

  ```bash
  kill -[option(15, 9, 19, 1, 2)] <pid>
  ```
  - sigkill
  ```bash
  kill -9 <pid>
  ```
  
  ```bash
  kill -NAME <PID>
  kill -SIGSTOP <PID>
  ```
  - kill multiple
  ```bash
  kill <pid1> <pid2> ...
  ```
  
  - kill with pattern
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
    - -e, --echo. Display name and PID of the process being killed.  (pkill only.)

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

- find the executable file for a command
```bash
which <executable file>
```

## Memory
- memory
```bash
free -mt # m : megabyte, t : total
```
![Swap](swap.png)
![Virtual memory](Virtual%20memory.png)

## Priority
![Priority nice](Priority_nice.png)
nice : kernel space priority = range -20 -- 19 
priority : user space priority = nice + 20 

niceness between -20 to 0 = high, 1 to 19

- run command/process with priority
```bash
nice -n <nice_value> <command>
```

only root can create process with niceness -20 to 0 

- change priority
```bash
renice -n <nice_value> -p <pid>
renice -n <nice_value> -u <user>
```

