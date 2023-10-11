#!/bin/bash

# Define the maximum number of failed login attempts
MAX_ATTEMPTS=3

# Define the time frame in seconds for rate limiting
TIME_FRAME=60

# Define the SSH port (default is 22)
SSH_PORT=22

# Get the current IP address making the connection
CURRENT_IP="$SSH_CLIENT"

# Extract the IP address from the SSH_CLIENT variable (format: IP_ADDRESS PORT USER)
CURRENT_IP=$(echo "$CURRENT_IP" | awk '{print $1}')

# Check if the IP address has exceeded the maximum failed login attempts
if [ "$(iptables -L -n | grep -cE "DROP.*$CURRENT_IP.*sshd.*recent\/set.*name: ssh")" -ge "$MAX_ATTEMPTS" ]; then
  echo "Blocking IP address $CURRENT_IP due to excessive failed login attempts."
  exit 0
fi

# Add the current IP address to the recent list for the SSH service
iptables -A INPUT -p tcp --dport "$SSH_PORT" -m recent --set --name ssh --rsource

# Allow the SSH connection
echo "Allowing SSH connection from $CURRENT_IP."
# Add your SSH-related rules here if needed.

# Sleep for a moment to allow successful SSH connections to complete
sleep 2

# Remove the current IP address from the recent list for the SSH service after the TIME_FRAME
iptables -D INPUT -p tcp --dport "$SSH_PORT" -m recent --name ssh --update --seconds "$TIME_FRAME" --hitcount "$MAX_ATTEMPTS" --rsource -j DROP
