#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=average_counts
#SBATCH --output=../logs/average_counts_%j.out
#SBATCH --error=../logs/average_counts_%j.err
#SBATCH --time=02:00:00
#SBATCH --partition=int
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100G


# Run the average_counts.sh script
bash average_counts.sh