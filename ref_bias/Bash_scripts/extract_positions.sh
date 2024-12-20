#!/bin/bash

# Define the VCF file
vcf_file="NA12878.vcf"

# Use AWK to extract chromosome and positions with genotype 1|1 for all chromosomes
awk '
BEGIN { FS = "\t"; OFS = "\t" }
!/^#/ && $10 == "1|1" { print $1, $2 }
' "$vcf_file" > positions.txt

# Print a message indicating completion
echo "Chromosome and positions extracted to positions.txt"