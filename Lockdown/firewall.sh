#!/bin/bash

# do we want to use multiport or weird port numbers?
# sudo apt-get install iptables-persistent (run this line before running the script)

# Flush existing rules and user defined chains
iptables -F; iptables -X

# SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT

#  established and related incoming connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
#iptables -A INPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT
#iptables -A OUTPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT

#  DNS
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT

# HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT

# FTP
#iptables -A INPUT -p tcp --dport ? -j ACCEPT
#iptables -A OUTPUT -p tcp --dport ? -j ACCEPT

# Whitelist (use principal of least privilege)
#sudo iptables -A INPUT -s 192.168.1.100 -j ACCEPT
#sudo iptables -A INPUT -s 192.168.1.101 -j ACCEPT

# Blacklist
#sudo iptables -A INPUT -s 192.168.1.100 -j DROP
#sudo iptables -A INPUT -s 192.168.1.101 -j DROP

#ICMP
#iptables -A INPUT -p icmp -s <insert ip range here> -j ACCEPT
#iptables -A INPUT -p icmp -j DROP

# Allow loopback traffic
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Set default policies to DROP for all unspecified ports
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Logged traffic is stored in /var/log/syslog
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
iptables-save > /etc/iptables/rules.v4 #is this the right spot to save this? needs practice to make sure this works!

# Restart the firewall service 
systemctl restart iptables

# Success message 
echo -e "\e[32mFirewall rules configured and restarted.\e[0m"



