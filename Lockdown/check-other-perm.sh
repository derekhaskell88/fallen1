#!/bin/bash
timestamp=$(date + "%H-%M")
start_dir="/"
output_file="flperm_report_$timestamp.txt"
find "$start_dir" -type f -o -type d -exec stat -c "%A %a %n" {} \; | \
  while read -r permissions octal_permissions filename; do
    if [[ "${permissions:6:1}" != "-" ]]; then
      echo "File: $filename"
      echo "Permissions: $permissions"
      echo "Octal Permissions: $octal_permissions"
      echo "-----------------------------"
    fi
  done > "$output_file"

echo "Report generated in $output_file"