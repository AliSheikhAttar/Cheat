# namespace

## pid namespace
```bash
sudo unshare --pid --fork bash
```
create a new namespace with children process running bash


```bash
sudo unshare --pid --fork --mount-proc bash
```
create a new namespace with children process running bash with /proc filesystem mounted to the namespace