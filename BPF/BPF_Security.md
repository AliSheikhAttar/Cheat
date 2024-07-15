# BPF Security

## Background on security
* Security analysis
  * Sniffing activity for real-time forensics
  * Privilege debugging
  * Executable usage whitelists
  * Reverse engineering of malware
* Monitoring
  * Custom auditing
  * Host-based intrusion detection systems (HIDS)
  * Container-based intrusion detection systems (CIDS)
* Policy enforcement
  * Networking firewalls
  * Detecting malware and dynamically blocking packets and taking other preventive actions


## BPF Capabilities
BPF can help with these security tasks, including analysis, monitoring, and policy enforcement.
For security analysis, the types of questions that BPF can answer include:
- Which processes are being executed?
- What network connections are being made? By which processes?
- Which system privileges are being requested by which processes?
- What permission denied errors are happening on the system?
- Is this kernel/user function being executed with these arguments (in checking for active
exploits)?