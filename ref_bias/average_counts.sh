#!/bin/bash

# Define the list of chromosomes
chromosomes=('chr1' 'chr2' 'chr3' 'chr4' 'chr5' 'chr6' 'chr7' 'chr8' 'chr9' 'chr10' 'chr11' 'chr12' 'chr13' 'chr14' 'chr15' 'chr16' 'chr17' 'chr18' 'chr19' 'chr20' 'chr21' 'chr22' 'chrX')

# Define the list of N values
Ns=(1 5 10 20 50 100 200 500 1000 2000)

# Output file
output_file="averages_output.txt"

# Function to calculate the average
calculate_average() {
    local file=$1
    if [ -f "$file" ]; then
        local sum=0
        local count=0
        while read -r value; do
            sum=$(echo "$sum + $value" | bc)
            count=$((count + 1))
        done < "$file"
        if [ $count -ne 0 ]; then
            local average
            average=$(echo "scale=2; $sum / $count" | bc)
            echo "$file: $average" >> $output_file
        else
            echo "$file: No data" >> $output_file
        fi
    else
        echo "$file: File not found" >> $output_file
    fi
}

# Loop through each N value and each chromosome to calculate averages
for N in "${Ns[@]}"; do
    for chr in "${chromosomes[@]}"; do
        calculate_average "../large_files/${chr}_VC_snp_counts_${N}.out"
    done
done

echo "Averages calculated and written to $output_file"