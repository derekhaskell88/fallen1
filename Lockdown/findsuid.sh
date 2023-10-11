#!/bin/bash
# run as standard user
timestamp=$(date +"%H-%M")
output_file="suid-rep-$timestamp.txt"
echo -e "\e[32mFinding SUID binaries"
find / -type f -perm /4000 -exec ls -l {} \; > "$output_file" 2>/dev/null
echo -e "Complete!"
echo -e "SUID Report generated in $output_file \e[0m"