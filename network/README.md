# network


## ip addr

![ip-addr](screenshots/screenshot-ip-addr.png)

* **eth1** - Interface name
* **mtu 1500** - maximum transmission unit, 1500, size of the largest frame/protocol-dat-unit(PDU), that can be send over this interface
* **qdisc** - queuing discipline, shows the queuing algorithm used on the interface
* **qlen 1000** - transmission queue length
* **link/ether** - data link layer protocol, Ethernet
* **08:00:27:a8:01:7b** - MAC address, 48 bits, 6 octets, MM:MM:MM:SS:SS:SS, M-ID number of the adapter manufacturer, S-serial number assigned to the adapter by the manufacturer
* **brd ff:ff:ff:ff:ff:ff** - broadcast MAC address
* **inet** - network layer protocol, internet IPv4
* **192.168.30.20/24** - IP address
* **brd 192.168.30.255** - broadcast IP address


## ethtool

![ethtool](screenshots/screenshot-ethtool.png)

Statistic

![ethtool-s](screenshots/screenshot-ethtool-s.png)

* **tx_packets** - trasmitted packets
* **rx_packets** - received packets
* **tx_errors** - trasmission errors
* **rx_errors** - teceived errors
* **rx_missed** - recieved misses


## ifconfig

![ifconfig](screenshots/screenshot-ifconfig.png)

* **eth1** - Interface name
* **flags** - Interface status
    * **UP/DOWN** - initialized/not initialized 
    * **BROADCAST** - broadcast status, indicates that the interface supports IPv4 broadcasts
    * **RUNNING** - transmission status, indicates that the system is transmitting packets through the interface
    * **MULTICAST** - multicast status, shows that the interface supports multicast transmissions
* **mtu 1500** - maximum transmission unit, 1500, shows that this interface has a maximum transfer size of 1500 octets. 
* **inet 192.168.30.20** - IP address, IPv4
* **netmask 255.255.255.0** - netmask, displays the IPv4 netmask of the particular interface.
* **broadcast 192.168.30.255** - broadcast IP address
* **ether 08:00:27:a8:01:7b** - MAC address, shows the interface's Ethernet layer address. 
* **RX packets** - total number of packets received
    * **RX bytes** - total number of bytes received over interface
* **RX errors** - total number of packets received with error
* **TX packets** - total number of packets transmitted
    * **TX bytes** - total number of bytes transmitted over interface
* **TX errors** - total number of packets transmitted with error


## arp

ARP Cache

![arp](screenshots/screenshot-arp.png)

* **192.168.30.21** - IP address of the neighboring host
* **ether** - Hardware Type, Ethernet
* **08:00:27:6c:5d:2c** -  MAC address of the neighboring host
* **eth1** - Interface name

## IP

IP address - 4 octets, total 8+8+8+8 = 32 Bits
Contains of a network address, and a host address

```
11000000.10101000.01111011.10000100 -- IP address (192.168.123.132) 
11111111.11111111.11111111.00000000 -- Subnet mask (255.255.255.0)
```
means
```
11000000.10101000.01111011.00000000 -- Network address (192.168.123.0) 
00000000.00000000.00000000.10000100 -- Host address (000.000.000.132)
```

Network classes
* **Class A** - first octet 0-127, default subnet mask 255.0.0.0
* **Class B** - first octet 128-191, default subnet mask 255.255.0.0
* **Class C** - first octet 192-223, default subnet mask 255.255.255.0

IP Packet = Header + Payload(data)

Main fields of IP Header: 
* Source IP Address - **32 bit**
* Destination IP Address  - **32 bit**
* Version(IPv4) - **4 bit**
* Protocol(TCP) - **4 bit**
* Total Length(all IP packet, header+payload) - **16 bit**

IP packet may be fragmented, if packet size is bigget than MTU and packet header flag DF is set to 0

IP message types:
* **unicast** - one to one
* **broadcast** - one to all
* **multicast** - one to several


## netstat

Show all TCP and UDP listening sockets, PID and program

Flags:
* **-p** - show the PID and name of the program to which each socket belongs
* **-l** - show only listening sockets
* **-u** - show UDP
* **-n** - show numerical addresses instead of trying to determine symbolic host, port or user names
* **-t** - show TCP

![netstat](screenshots/screenshot-netstat.png)

* **Proto** - the protocol (tcp, udp, udpl, raw) used by the socket
* **Recv-Q** - the count of bytes not copied by the user program connected to this socket
* **Send-Q** - the count of bytes not acknowledged by the remote host
* **Local Address** - address and port number of the local end of the socket
* **Foreign Address** - address and port number of the remote end of the socket
* **State** - the state of the socket
    * **LISTEN** - the socket is listening for incoming connections
    * **ESTABLISHED** - the socket has an established connection
* **PID/Program name** - slash-separated  pair  of  the process id (PID) and process name of the process that owns the socket

