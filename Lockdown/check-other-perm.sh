#!/bin/bash

# Check if an argument (directory) was provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

# Check if the specified directory exists
directory="$1"
if [ ! -d "$directory" ]; then
  echo "Error: '$directory' is not a valid directory."
  exit 1
fi

# Generate a timestamp for the filename
timestamp=$(date +"%H-%M")
# Replace '/' characters in the directory path with underscores
escaped_directory=$(echo "$directory" | tr '/' '_')
report_filename="permrep${escaped_directory}_${timestamp}.txt"

# Find and save the permissions report
find "$directory" -type f -exec ls -l {} \; > "$report_filename"

# Inform the user about the generated report
echo "Permissions report for '$directory' has been saved to '$report_filename'."