#!/bin/bash

set -e

# Treat unset variables as an error
set -u

# Define the list of chromosomes
chromosomes=('chr1' 'chr2' 'chr3' 'chr4' 'chr5' 'chr6' 'chr7' 'chr8' 'chr9' 'chr10' 'chr11' 'chr12' 'chr13' 'chr14' 'chr15' 'chr16' 'chr17' 'chr18' 'chr19' 'chr20' 'chr21' 'chr22' 'chrX' 'chrY' 'chrM')


# Ensure the logs directory exists
mkdir -p logs

# Loop through each chromosome and submit a job
for chr in "${chromosomes[@]}"; do
    sbatch <<EOF
#!/bin/bash
#SBATCH --job-name=VC_dump_${chr}
#SBATCH --output=logs/${chr}_juicer.out
#SBATCH --error=logs/${chr}_juicer.err
#SBATCH --time=02:00:00
#SBATCH --partition=weka
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=100G

# Load necessary modules (adjust if needed)
module load java

# Run the Juicer Tools command for the chromosome
bash /gpfs0/juicer2/scripts/juicer_tools dump norm VC gm12878_ultramap.hic ${chr} BP 1 ${chr}_VC_dump.out
EOF
done
