#!/bin/bash

# Define the VCF file
vcf_file="NA12878.vcf"

# Extract unique chromosome values from the VCF file
awk 'BEGIN {FS="\t"} !/^#/ {print $1}' "$vcf_file" | sort | uniq