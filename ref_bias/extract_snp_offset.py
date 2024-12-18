import hicstraw as straw
import os
from collections import defaultdict
import pickle
import glob
import sys
import concurrent.futures

Ns = [1,5,10,20,50,100,200,500,1000,2000]

hic_file = "gm12878_ultramap.hic"

gm12878_file = straw.HiCFile(hic_file)

chroms = gm12878_file.getChromosomes()[1:-2]

with open("snp_positions_dict.pkl", "rb") as f:
        snp_positions = pickle.load(f)

def extract_counts(chrom, positions, Ns):
    input_file = f"../large_files/{chrom}_VC_dump.out"
    
    with open(input_file, "r") as infile:
        lines = infile.readlines()
        output_files = {N: open(f"../large_files/temp/{chrom}_VC_snp_counts_{N}.out", "a") for N in Ns}
        
        for pos in positions:
            for N in Ns:
                if pos + N < len(lines):
                    output_files[N].write(lines[pos + N])
        
        for f in output_files.values():
            f.close()
        

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for chrom in chroms:
        if chrom.name in snp_positions:
            futures.append(executor.submit(extract_counts, chrom.name, snp_positions[chrom.name], Ns))
    concurrent.futures.wait(futures)
print("\n=====Done=====\n")