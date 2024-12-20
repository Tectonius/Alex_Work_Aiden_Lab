#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=fix_formatting
#SBATCH --output=/gpfs0/work/alex/logs/fix_formatting_%j.out
#SBATCH --error=/gpfs0/work/alex/logs/fix_formatting_%j.err
#SBATCH --time=1:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=20G

# Run the fix_formatting.py script
python fix_formatting.py
