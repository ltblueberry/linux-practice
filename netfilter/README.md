# netfilter

## firewalld

Get state and list all

![firewall-cmd](screenshots/screenshot-firewall-cmd-basic.png)


Get info about zone (example public)

![public-zone](screenshots/screenshot-firewall-cmd-zone.png)


add and remove service (example mysql, port 3306)

![mysql-service](screenshots/screenshot-firewall-cmd-service.png)


Curl check

![mysql-service-curl](screenshots/screenshot-firewall-cmd-service-curl.png)


Add port forwarding (3307->3306)

![port-forward](screenshots/screenshot-firewall-cmd-forward.png)


Curl check

![port-forward-curl](screenshots/screenshot-firewall-cmd-forward-curl.png)


Check if service and interface were added to zone

![query](screenshots/screenshot-firewall-cmd-query.png)


**/usr/lib/firewalld/services/*.xml**

![query](screenshots/screenshot-firewall-cmd-service-xml.png)


**check changes in iptables IN_public_allow**

![query](screenshots/screenshot-firewall-cmd-IN_public_allow.png)


Add new zone for mysql and add source

![query](screenshots/screenshot-firewall-cmd-new-zone.png)


Check with curl from two hosts

![query](screenshots/screenshot-firewall-cmd-new-zone-check.png)



