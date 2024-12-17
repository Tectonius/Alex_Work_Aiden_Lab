#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=ref_bias_main_chr1_T5
#SBATCH --output=ref_bias_main.out
#SBATCH --error=ref_bias_main.err
#SBATCH --time=02:00:00
#SBATCH --partition=int
#SBATCH --ntasks=1
#SBATCH --mem=100G



# Check if an argument is provided
if [ -z "$1" ]; then
    # No argument provided
    python ref_bias_main.py
else
    # Argument provided
    python ref_bias_main.py "$1"
fi