#!/bin/bash

# Directory containing the dump files
input_dir="../large_files/dumps"

# Output directory
output_dir="../large_files/processed_dumps"
mkdir -p "$output_dir"

# Process each file in the input directory
for file in "$input_dir"/*.out; do
    # Extract the chromosome name from the file name
    filename=$(basename "$file")
    chromosome=$(echo "$filename" | cut -d'_' -f1)
    
    # Create the output filename with .bedgraph extension
    output_filename="${filename%.out}.bedgraph"
    
    # Process the file with awk
    awk -v chr="$chromosome" '{print chr "\t" NR "\t" NR+1 "\t" $0}' "$file" > "$output_dir/$output_filename"
done