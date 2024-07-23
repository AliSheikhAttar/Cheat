you can detach, or leave, or exit tmux, while all those terminal
sessions that are managed by Tmux are still running in the background. Then you can come back at a later time and reattach to those terminal sessions. If you work on remote systems


- new session
```bash
tmux new -s backups # new-session
```
-  it exits that window and thus exits tmux as well
```bash
exit
```

- new window
```bash
Ctrl-b c
```
- next window
```bash
Ctrl-b n 
```

- previous window
```bash
Cntrl-b p 
```

- jump windows <n+1>
```bash
Cntrl-b <n> 
```

- naming the windows
```bash
Cntrl-b , 
```

- detach from session, If we need or want to disconnect again, leaving everything running
```bash
Ctrl-b d 
```

- attach to session
> If you just run tmux a, you’ll be connected to the most recently used Tmux session.
```bash
tmux a -t <session># “tmux attach”, and “tmux attach-session” 
```

- list of sessions
```bash
tmux ls # list-sessions 
```

- swith between sessions
```bash
Ctrl-b s 
```

- help
```bash
Ctrl-b ? 
```
- kill session
> in the session -> Cntrl + b -> : -> kill-session

