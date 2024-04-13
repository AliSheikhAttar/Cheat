# Linux System
- service and processes most using cpu

```bash
Top 
```
- change ownership of directories
```bash
  sudo chown newuser filename
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

