# Linux System

## Processes
```bash
Top 
```
###  Search processes
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

- -c, --count
  print a count of matching processes. 

- -d, --delimiter delimiter
      Sets  the  string  used to delimit each process ID in the output
      (by default a newline).  (pgrep only.)



- -f, --full
      The pattern is normally only matched against the  process  name.
      When -f is set, the full command line is used.

- -g, --pgroup pgrp,...
      Only  match  processes in the process group IDs listed.  Process
      group 0 is translated into pgrep's, pkill's,  or  pidwait's  own
      process group.

- -G, --group gid,...
      Only  match processes whose real group ID is listed.  Either the
      numerical or symbolical value may be used.

- -i, --ignore-case
      Match processes case-insensitively.

- -l, --list-name
      List the process name as well as the process ID.  (pgrep only.)

- -a, --list-full
      List the full command line as well as the  process  ID.   (pgrep
      only.)

- -n, --newest
      Select  only  the newest (most recently started) of the matching
      processes.

- -o, --oldest
      Select only the oldest (least recently started) of the  matching
      processes.

- -O, --older secs
      Select processes older than secs.

- -P, --parent ppid,...
      Only match processes whose parent process ID is listed.

- -s, --session sid,...
      Only  match  processes whose process session ID is listed.  Ses‐
      sion ID 0 is translated into pgrep's, pkill's, or pidwait's  own
      session ID.
- -t, --terminal term,...
      Only  match processes whose controlling terminal is listed.  The
      terminal name should be specified without the "/dev/" prefix.

- -u, --euid euid,...
      Only match processes whose effective user ID is listed.   Either
      the numerical or symbolical value may be used.

- -U, --uid uid,...
      Only  match  processes whose real user ID is listed.  Either the
      numerical or symbolical value may be used.

- -v, --inverse
      Negates the matching.  This option is usually used in pgrep's or
      pidwait's  context.  In pkill's context the short option is dis‐
      abled to avoid accidental usage of the option.

- -w, --lightweight
      Shows all thread ids instead of pids  in  pgrep's  or  pidwait's
      context.  In pkill's context this option is disabled.

- -x, --exact
      Only  match  processes  whose  names  (or command lines if -f is
      specified) exactly match the pattern.

- -F, --pidfile file
      Read PIDs from file.  This option is more useful for pkillorpidwait than pgrep.

- -L, --logpidfile
      Fail if pidfile (see -F) not locked.

- -r, --runstates D,R,S,Z,...
      Match only processes which match the process state.

- --ns pid
      Match  processes that belong to the same namespaces. Required to
      run as root to match processes from other  users.  See  --nslist
      for how to limit which namespaces to match.

- --nslist name,...
      Match  only  the provided namespaces. Available namespaces: ipc,
      mnt, net, pid, user,uts.

- -q, --queue value
      Use sigqueue(3) rather than kill(2) and the  value  argument  is
      used  to  specify  an integer to be sent with the signal. If the
      receiving process has installed a handler for this signal  using
      the  SA_SIGINFO  flag  to sigaction(2) , then it can obtain this
      data via the si_value field of the siginfo_t structure.




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
## Permissions
- change ownership of directories
```bash
  sudo chown -c -R $USER:$USER <directory>
```
- add user to app group
```bash
  sudo usermod -a -G <app> <user>
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

