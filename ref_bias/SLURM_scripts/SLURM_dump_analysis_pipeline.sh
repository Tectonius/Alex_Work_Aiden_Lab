#!/bin/bash -l

# SBATCH directives
#SBATCH --job-name=dump_analysis_pipeline
#SBATCH --output=/gpfs0/work/alex/logs/dump_analysis_pipeline_%j.out 
#SBATCH --error=/gpfs0/work/alex/logs/dump_analysis_pipeline_%j.err
#SBATCH --time=2:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=75G


# Run the extract_offset_counts.py script
python /gpfs0/work/alex/ref_bias/Python_scripts/extract_offset_counts.py

# Check the exit status of the previous command
if [ $? -ne 0 ]; then
    echo "extract_offset_counts.py failed" >&2
    exit 1
fi

# Run the next script if the previous one succeeded
python /gpfs0/work/alex/ref_bias/Python_scripts/calculate_stats.py

if [ $? -ne 0 ]; then
    echo "calculate_stats.py failed" >&2
    exit 1
fi

python /gpfs0/work/alex/ref_bias/Python_scripts/graph_stats.py

if [ $? -ne 0 ]; then
    echo "graph_stats.py failed" >&2
    exit 1
fi