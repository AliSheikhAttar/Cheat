# CMDZ

- scaning ports on local network
    ```bash
        sudo nmap localhost
    ```
    
  - Stealthy and Version
  ```bash
    sudo nmap -sS -sV localhost
  ```

## update scripts
```bash
sudo nmap --script-updatedb
```

## find specific script
```bash
ls /usr/share/nmap/scripts/ | grep backdoor
```