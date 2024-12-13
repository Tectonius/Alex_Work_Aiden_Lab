
#%%
import hicstraw as straw
import os
from collections import defaultdict
import pickle
import glob
import concurrent.futures

if os.path.exists("ref_bias"):
    os.chdir("./ref_bias")

# Load Hi-C data using straw
hic_file = "gm12878_ultramap.hic"
start = 0
end = 1000000
file = straw.HiCFile(hic_file)
print(file.getResolutions())

chroms = file.getChromosomes()[1:-2]
print(len(chroms))
#%%
if not os.path.exists("snp_positions_dict.pkl"):
    snp_positions = defaultdict(list)
    with open("positions.txt", "r") as f:
        for line in f:
            chrom, pos = line.strip().split()
            snp_positions[chrom].append(int(pos))
    with open("snp_positions_dict.pkl", "wb") as f:
        pickle.dump(snp_positions, f)
else:
    with open("snp_positions_dict.pkl", "rb") as f:
        snp_positions = pickle.load(f)


chroms = file.getChromosomes()[1:-2]
chroms_straw = []

if False:
    def process_chromosome(chromosome):
        hic_data = straw.straw('observed', 'NONE', hic_file, chromosome.name, chromosome.name, 'BP', 1)
        with open(f"{chromosome}_contacts.pkl", "wb") as f:
            pickle.dump(hic_data, f)
        return hic_data

    if not glob.glob("*_contacts.pkl"):
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(chroms)) as executor:
            chroms_straw = list(executor.map(process_chromosome, chroms))
else:
    for chromosome in [chroms[0]]:
        hic_data = straw.straw('observed', 'NONE', hic_file, chromosome.name, chromosome.name, 'BP', 1)
        with open(f"{chromosome}_contacts.pkl", "wb") as f:
            pickle.dump(hic_data, f)
        chroms_straw.append(hic_data)

hic_data_dict = defaultdict(list)
for pkl_file in glob.glob("*_contacts.pkl"):
    chrom_name = os.path.splitext(pkl_file)[0]
    with open(pkl_file, "rb") as f:
        hic_data = pickle.load(f)
        hic_data_dict[chrom_name].extend(hic_data)

if 'chr1' in snp_positions:
    chr1_snp_positions = snp_positions['chr1']
    hic_data_chr1 = hic_data_dict['chr1']
    snp_reads = 0
    non_snp_reads = 0
    for snp in chr1_snp_positions:
        snp_reads += hic_data_chr1[snp]
        non_snp_reads += hic_data_chr1[snp + 1000]
    snp_reads /= len(chr1_snp_positions)
    non_snp_reads /= len(chr1_snp_positions)
    print(f"{snp_reads}, {non_snp_reads}")