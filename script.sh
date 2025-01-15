#!/bin/bash
input_file="data.csv"
output_file="output.txt"
grep -vi "skip" "$input_file" | tr 'A-Z' 'a-z' | sed 's/[0-9]//g' | sed 's/_/ /g' | awk -F, '{print $2}' > "$output_file"
echo "Processing complete. The output has been saved to $output_file."
