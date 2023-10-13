#!/bin/bash

# do we want to use multiport or weird port numbers?
# sudo apt-get install iptables-persistent (run this line before running the script)

# Flush existing rules and user defined chains
iptables -F; iptables -X

# SSH (trusted)
#iptables -A INPUT -p tcp --dport 22 -s trusted_ip1 -j ACCEPT
#iptables -A INPUT -p tcp --dport 22 -s trusted_ip2 -j ACCEPT

# SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT

# established and related connections(i couldn't get cstate to work on my ubuntu server)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
#iptables -A INPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT
#iptables -A OUTPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT


# DNS
#iptables -A INPUT -p udp --dport 53 -s trusted_ip1 -j ACCEPT
#iptables -A OUTPUT -p udp --dport 53 -s trusted_ip1 -j ACCEPT
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT

# HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT

# FTP (trusted)
#iptables -A INPUT -p tcp --dport 21 -s trusted_ip1 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 21 -s trusted_ip1 -j ACCEPT
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 21 -j ACCEPT

# MySQL (trusted)
#iptables -A INPUT -p tcp --dport 3306 -s db_server_ip1 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 3306 -s db_server_ip2 -j ACCEPT
iptables -A INPUT -p tcp --dport 3306 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 3306 -j ACCEPT

# Whitelist 
#sudo iptables -A INPUT -s trusted-ip -j ACCEPT
#sudo iptables -A INPUT -s trusted-ip -j ACCEPT

# Blacklist
#sudo iptables -A OUTPUT -s not-trustedip -j DROP
#sudo iptables -A INPUT -s not-trustedip -j DROP

#ICMP
iptables -A INPUT -p icmp -j ACCEPT
iptables -A OUTPUT -p icmp -j ACCEPT
#iptables -A INPUT -p icmp -s <insert ip range here> -j ACCEPT
#iptables -A INPUT -p icmp -j DROP

# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Set default policies to DROP for all unspecified ports
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Logged traffic is stored in /var/log/syslog, do we need to log outbount traffic?
iptables -A INPUT -j LOG --log-prefix "Denied: "
iptables -A OUTPUT -j LOG --log-prefix "Denied: "
iptables -A INPUT -j LOG --log-prefix "Forwarded: "
iptables -A OUTPUT -j LOG --log-prefix "Forwarded: "
iptables -A INPUT -j LOG --log-prefix "Blocked: "
iptables -A OUTPUT -j LOG --log-prefix "Blocked: "
iptables -A INPUT -j LOG --log-prefix "Dropped: "
iptables -A OUTPUT -j LOG --log-prefix "Dropped: "
iptables -A INPUT -j LOG --log-prefix "Intrusion: "
iptables -A OUTPUT -j LOG --log-prefix "Intrusion: "



# Save the rules to make them persistent
iptables-save > /etc/iptables/rules.v4 

# Restart the firewall service 
systemctl restart iptables

# Success message 
echo  "Firewall rules configured and restarted."
echo 'Rules have been saved to /etc/iptables/rules.v4'


