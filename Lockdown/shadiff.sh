#!/bin/bash

if [ $# -ne 2 ]; then
  echo -e "\e[31mUsage:\e[0m $0 <file1> <file2>"
  exit 1
fi

file1="$1"
file2="$2"

if [ ! -f "$file1" ]; then
  echo -e "\e[31mError:\e[0m '$file1' does not exist or is not a file."
  exit 1
fi

if [ ! -f "$file2" ]; then
  echo -e "\e[31mError:\e[0m '$file2' does not exist or is not a file."
  exit 1
fi

sha256_file1=$(sha256sum "$file1" | awk '{print $1}')
sha256_file2=$(sha256sum "$file2" | awk '{print $1}')

if [ "$sha256_file1" == "$sha256_file2" ]; then
  echo -e "\e[32mSHA-256 sums match:\e[0m '$file1' and '$file2'"
else
  echo -e "\e[31mSHA-256 sums do not match:\e[0m '$file1' and '$file2'"
  differences=$(diff "$file1" "$file2")
  timestamp=$(date +"%H-%M")
  echo -e "\e[31mDifferences: "
  echo -e "$differences\e[0m"
  echo "$differences" > "whatdiff-$timestamp.txt"
fi
