#!/bin/bash
timestamp=$(date +"%H-%M")
output_file="suid_report_$timestamp.txt"
echo -e "\e[32mFinding SUID binaries"
find / -type f -perm /4000 -exec ls -l {} \; > "$output_file" 2>/dev/null
echo -e "Complete!"
echo "SUID Report generated in $output_file\e[0m"