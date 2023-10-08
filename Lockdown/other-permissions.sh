#!/bin/bash
#this is untested I'm unsure how it will run I will be creating a virtual machine to test it asap
# Specify the directory to start the search from
start_dir="/"

# Specify the output file for the report
output_file="file_permissions_report.txt"

# Find all files and directories under the specified directory
# and check their permissions for the "other" group
find "$start_dir" -type f -o -type d -exec stat -c "%A %a %n" {} \; | \
  while read -r permissions octal_permissions filename; do
    # Check if the permissions for the "other" group are set
    if [[ "${permissions:6:1}" != "-" ]]; then
      echo "File: $filename"
      echo "Permissions: $permissions"
      echo "Octal Permissions: $octal_permissions"
      echo "-----------------------------"

      # Remove the "other" group permissions
      chmod o= "$filename"
      echo "Removed 'other' group permissions."
    fi
  done > "$output_file"

echo "Report generated in $output_file"