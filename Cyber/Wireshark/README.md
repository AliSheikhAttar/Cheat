# Wireshark

Protocol: tcp (udp, icmp, …)
* IP address: `ip.addr == x.x.x.x`
* Source address: `ip.src == x.x.x.x`
* Destination address: `ip.dst == x.x.x.x`
* Sequence number: `tcp.seq >= x`
* Port number: `tcp.port == xxx`
* Content: `tcp contains xxx`
* Conditions: `ip.src == x.x.x.x and(or) ip.dst != x.x.x.x`