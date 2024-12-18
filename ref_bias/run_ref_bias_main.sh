#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=ref_bias_main_extract_T2
#SBATCH --output=ref_bias_main_%j.out
#SBATCH --error=ref_bias_main_%j.err
#SBATCH --time=02:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=24 
#SBATCH --mem=200G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=alexbrazil2001@gmail.com



# Check if an argument is provided
if [ -z "$1" ]; then
    # No argument provided
    python ref_bias_main.py
else
    # Argument provided
    python ref_bias_main.py "$1"
fi