#!/bin/bash

# do we want to use multiport?

# Flush existing rules and user defined chains
iptables -F; iptables -X

# Set default policies to DROP
#iptables -P INPUT DROP
#iptables -P FORWARD DROP
#iptables -P OUTPUT DROP

# Allow SSH in
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
#iptables -A OUTPUT -p tcp --dport 22 -j ACCEPT

# Allow established and related incoming connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
#iptables -A INPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT
#iptables -A OUTPUT -m conntrack --cstate ESTABLISHED,RELATED -j ACCEPT

# Allow HTTP and HTTPS out
iptables -A OUTPUT -p tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT

# DNS
iptables -A INPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT

#ICMP
#iptables -A INPUT -p icmp -s <insert ip range here> -j ACCEPT

# FTP
#iptables -A INPUT -p tcp --dport ? -j ACCEPT
#iptables -A OUTPUT -p tcp --dport ? -j ACCEPT

# set default policy for forward to drop
iptables -P FORWARD DROP

# Allow loopback traffic
#iptables -A INPUT -i lo -j ACCEPT
#iptables -A OUTPUT -o lo -j ACCEPT

# Allow HTTP and HTTPS in
#iptables -A INPUT -p tcp --dport 80 -j ACCEPT
#iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Log denied traffic (optional)
iptables -A INPUT -j LOG --log-prefix "Denied: "

# Save the rules to make them persistent
iptables-save > /etc/iptables/rules.v4 #is this the right spot to save this?

# Restart the firewall service 
systemctl restart iptables

# Success message 
echo "Firewall rules configured and restarted."



