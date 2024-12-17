#%%
import hicstraw as straw
import os
from collections import defaultdict
import pickle
import glob
import sys
import concurrent.futures

if os.path.exists("ref_bias"):
    os.chdir("./ref_bias")

# Load Hi-C data using straw
if len(sys.argv) > 1:
    hic_file = sys.argv[1]
else:
    hic_file = "gm12878_ultramap.hic"
start = 0
end = 1000000
gm12878_file = straw.HiCFile(hic_file)
print(gm12878_file.getResolutions())
chroms = gm12878_file.getChromosomes()[1:-2]
lowest_res = gm12878_file.getResolutions()[0]
highest_res = gm12878_file.getResolutions()[-1]
print(gm12878_file.getResolutions())
chroms = gm12878_file.getChromosomes()[1:-2]
print([c.name for c in chroms])

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

print(snp_positions.keys())

#%%


def extract_counts(chrom, positions):
    input_file = f"../large_files/{chrom}_VC_dump.out"
    output_file = f"../large_files/{chrom}_VC_snp_counts.out"
    
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        lines = infile.readlines()
        for pos in positions:
            if pos < len(lines):
                outfile.write(lines[pos])

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for chrom in chroms:
        if chrom.name in snp_positions:
            futures.append(executor.submit(extract_counts, chrom.name, snp_positions[chrom.name]))
    concurrent.futures.wait(futures)
