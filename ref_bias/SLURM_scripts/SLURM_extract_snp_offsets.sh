#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=extract_snp_offset_combined_-250_150
#SBATCH --output=/gpfs0/work/alex/logs/extract_snp_offset_%j.out
#SBATCH --error=/gpfs0/work/alex/logs/extract_snp_offset_%j.err
#SBATCH --time=02:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24
#SBATCH --mem=200G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Alexander.Ellis@bcm.edu

# Run the extract_snp_offset.py script
python extract_snp_offset.py