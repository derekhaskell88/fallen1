#!/bin/bash

locations=(
    "/etc/shadow"
    "/etc/passwd"
    "/root"
    "/etc/ssh/sshd_config"
    "/etc/crontab"
    "/var/spool/cron/crontabs"
    "/etc/group"
    "/etc/hosts"
    "/etc/resolv.conf"
    "/home"
)

timestamp=$(date +"%H-%M")
report_file="permrep-$timestamp.txt"

check_permissions() {
    file="$1"
    echo "Permissions for $file:" >> "$report_file"
    ls -la "$file" >> "$report_file"
    echo -e "\n" >> "$report_file"
}

for location in "${locations[@]}"; do
    if [ -e "$location" ]; then
        check_permissions "$location"
    else
        echo "$location does not exist" >> "$report_file"
        echo -e "\n" >> "$report_file"
    fi
done

echo "Permission check completed. Report saved as $report_file"