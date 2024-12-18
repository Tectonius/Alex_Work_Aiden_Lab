#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=extract_snp_offset
#SBATCH --output=../logs/extract_snp_offset_%j.out
#SBATCH --error=../logs/extract_snp_offset_%j.err
#SBATCH --time=08:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --mem=200G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Alexander.Ellis@bcm.edu

which python

# Run the extract_snp_offset.py script
# python extract_snp_offset.py