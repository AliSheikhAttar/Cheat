# Shell

## info
- Information about ls. use “q” to exit
```bash
info ls
```
- Complete information about ls
```bash
man ls
```

- help
```bash
<command> --help
```

## History

```bash
history
history <n> #last <n> commands
```
- run previous commands
```bash
!! # previous command
!<n> # nth previous command
```

- delete history
```bash
history -c; history -w;
```

- terminate session
```bash
exit
```

- execute command
```bash
eval $(command: echo "hello linux")
```

## chaining commands
- run cmd1 and cmd2
```bash
cmd1 ; cmd2
```

- if any cmds fail, the other wont get executed
```bash
cmd1 && cmd2
```

- if cmd1 executed then cmd2 won't but if cmd1 fails, cmd2 will get executed
```bash
cmd1 || cmd2
```

break up a long command into mulitple lines
```bash
mkdir hello; \
cd hello;\
echo done
```