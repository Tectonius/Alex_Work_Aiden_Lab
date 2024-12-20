#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=dump_to_bedgraph
#SBATCH --output=/gpfs0/work/alex/logs/dump_to_bedgraph_%j.out
#SBATCH --error=/gpfs0/work/alex/logs/dump_to_bedgraph_%j.err
#SBATCH --time=01:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --mem=20G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=Alexander.Ellis@bcm.edu

# Run the dump_to_bedgraph.sh script
bash dump_to_bedgraph.sh