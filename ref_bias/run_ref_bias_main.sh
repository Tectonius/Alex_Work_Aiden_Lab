#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=ref_bias_main
#SBATCH --output=ref_bias_main.out
#SBATCH --error=ref_bias_main.err
#SBATCH --time=02:00:00
#SBATCH --partition=int
#SBATCH --ntasks=1
#SBATCH --mem=200G



# Run the Python script
python ref_bias_main.py
