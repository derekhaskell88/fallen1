#!/bin/bash
timestamp=$(date +"%H-%M")
output_file="suid_report_$timestamp.txt"
find / -type f -perm /4000 -exec ls -l {} \; > "$output_file" 2>/dev/null
echo "SUID Files Report generated in $output_file"