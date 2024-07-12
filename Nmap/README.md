# Nmap

- stealth syn (default) scan for ports 23 and 80 in specified network
```bash
nmap -sS -p22,80 <192.168.0.0/27>
```

- list scan 
> target enumeration & reverse-dns
> list all hosts be scanned & perform reverse-DNS
```bash
nmap -sL <domain>
```

- host discovery (default)
> target enumeration, host discovery, reverse-dns
> find list of available hosts 
> sends ICMP & TCP packets to determin  if a host is up
```bash
nmap -sn <net add>
```
- exclude 
```bash
nmap -sL <ipadd-range> --exclude <hostname/ipadd,more>
```

- input from file
```bash
nmap -sL -iL <file address>
```

- scan on random ip addresses
```bash
nmap -sL -iR 
```

## Defense against ping scan

> configure host or network firewall to block ICMP traffic
> configure firewall to drop TCP packets for PORT 80 & 443 unless needed
> limit the ability external devices to scan devices

## States of Ports
- **Open**
> The port is open and actively accepting connection- This typically indicates a service is listening on the port.
Example: An HTTP server listening on port 80.

- **Closed**

> The port is accessible but there is no service listening on i- It can be reached but is not open.
Example: A port that is not currently in use but is not blocked by a firewall.

- **Filtered**

> Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the por- This often indicates the presence of a firewall.
Example: A firewall blocking access to a specific port.

- **Unfiltered**

> The port is accessible, but Nmap cannot determine if it is open or close- This state is less common and usually results from using certain scan types like ACK scan.
Example: An ACK scan shows a port as unfiltered.

- **Open|Filtered**

> Nmap cannot determine whether the port is open or filtere- This can happen with scan types that do not distinguish between open ports and filtered ports (e.g., a UDP scan).
Example: A UDP scan where the response is ambiguous.

- **Closed|Filtered**

> Nmap cannot determine if the port is closed or filtere- This state is also less common.
Example: This might be seen with IP ID header scan where responses are not clear.

## Most usefull options

- **TCP SYN Scan (-sS)**
> >Description: This is the default and most popular scan option because it is fast and relatively stealthy.
How it Works: Sends a SYN packet (as if to initiate a TCP connection) and waits for a response:
- SYN-ACK: The port is open.
- RST: The port is closed.
- No response or ICMP unreachable: The port is filtered.
```bash
nmap -sS <target>
```
- **TCP Connect Scan (-sT)**
>>Description: This scan is used when the user does not have raw packet privileges, as it relies on the operating system to make the connection.
How it Works: Completes the three-way TCP handshake.
Advantages: Works without raw packet privileges.
Disadvantages: Less stealthy and slower than SYN scan.
```bash
nmap -sT <target>
```
- **UDP Scan (-sU)**
>>Description: Scans UDP ports.
How it Works: Sends a UDP packet to the target port and waits for a response.
No response: The port is open or filtered.
ICMP port unreachable: The port is closed.
Advantages: Identifies services running on UDP ports.
Disadvantages: Slower and can be more easily blocked.
```bash
nmap -sU <target>
```
- **Service Version Detection (-sV)**
>Description: Determines the version of services running on open ports.
How it Works: Sends various probes to open ports and compares responses with a database of known service signatures.
```bash
nmap -sV <target>
```
- **OS Detection (-O)**
>Description: Attempts to determine the operating system of the target.
How it Works: Sends a series of TCP and ICMP packets and compares responses with a database of known OS signatures.
```bash
nmap -O <target>
```
- **Ping Scan (-sn)**
>Description: Discovers which hosts are up without doing a port scan.
How it Works: Sends ICMP echo requests, TCP SYN to port 443, TCP ACK to port 80, and ICMP timestamp requests.
```bash
nmap -sn <target>
```
- **Intense Scan**
>Description: Combines several advanced features for a comprehensive scan.
How it Works: Typically includes TCP SYN scan, service version detection, OS detection, traceroute, and script scanning.
```bash
nmap -A <target>
```
- **Aggressive Scan (-A)**
>Description: Enables OS detection, version detection, script scanning, and traceroute in one scan.
```bash
nmap -A <target>
```
- **Script Scan (-sC)**
>Description: Uses Nmap Scripting Engine (NSE) to run a collection of scripts against the target.
How it Works: The scripts can perform a variety of tasks, including vulnerability detection, backdoor detection, and more.
```bash
nmap -sC <target>
```
- **--script**
>this is used to run specific scripts from the Nmap Scripting Engine (NSE).NSE scripts can perform a wide range of tasks, including vulnerability detection, network discovery, and more
- Auth: Scripts related to authentication.
- Broadcast: Scripts for discovering hosts and services through broadcast messages.
- Brute: Scripts that perform brute-force password guessing.
- Default: Scripts that run in the default scan mode.
- Discovery: Scripts for host and service discovery.
- Dos: Scripts for testing Denial of Service vulnerabilities.
- Exploit: Scripts that exploit vulnerabilities.
- External: Scripts that interact with third-party services.
- Fuzzer: Scripts that perform fuzzing.
- Intrusive: Scripts that might disrupt the target.
- Malware: Scripts for detecting malware.
- Safe: Scripts that are considered safe and unlikely to cause disruptions.
- Version: Scripts that perform service version detection.
- Vuln: Scripts for vulnerability detection.<br><br>

- List Available Scripts:
This command lists all available scripts with description
```bash
nmap --script-help all
```

- View Script Documentation:
```bash
nmap --script-help http-title
```


- Running a Single Script
```bash
nmap --script http-title target
```
This runs the http-title script, which retrieves the title of a web page.

- Running Multiple Scripts
You can specify multiple scripts by separating them with commas:

```bash
nmap --script=http-title,http-headers target
```
This runs both the http-title and http-headers scripts.

- Running a Category of Scripts
To run all scripts in a specific category, prefix the category name with category:

```bash
nmap --script "vuln" target
```
This runs all scripts in the vuln category, which are used for vulnerability detection.

- Running Multiple Categories
You can combine categories by separating them with commas:

```bash
nmap --script "default,vuln" target
```
This runs all scripts in the default and vuln categories.

- Using Wildcards
You can use wildcards to match script names or categories:

```bash
nmap --script "http-*" target
```
This runs all scripts that start with http-.

- Script Arguments
Some scripts accept arguments to customize their behavior. Use the --script-args option to provide these arguments:
```bash
nmap --script http-brute --script-args http-brute.path=/admin target
```
This runs the http-brute script and sets the path to /admin.<br>


- **Usefull scripts**:
- Vulnerability Detection
The vulners script checks for vulnerabilities using the Vulners database.
```bash
nmap --script=vulners target
```

- Banner Grabbing
The banner script grabs banners from open ports, which can provide information about running services.
```bash
nmap --script=banner target
```


- **Stealth Scan (-sN, -sF, -sX)**
>Description: Various scan types that attempt to evade detection.
How it Works: Uses different packet flags to perform scans in a less detectable way:
- Null Scan (-sN): No flags set.
- FIN Scan (-sF): Only the FIN flag set.
- Xmas Scan (-sX): FIN, PSH, and URG flags set.
```bash
nmap -sN <target>
nmap -sF <target>
nmap -sX <target>
```
- **Top Ports Scan (--top-ports)**
>Description: Scans only the most commonly used ports.
How it Works: Limits the scan to a specified number of top ports based on frequency.
```bash
nmap --top-ports 100 <target>
```
- **Trace Route (--traceroute)**
>Description: Maps the path packets take to reach the target.
How it Works: Uses the traceroute method to determine the route to the target.
```bash
nmap --traceroute <target>
```

- **Combining Options**
This command performs a TCP SYN scan, service version detection, OS detection, and scans all 65535 ports on the target.
```bash
nmap -sS -sV -O -p 1-65535 target
```