import os
import pickle
import concurrent.futures

if os.path.basename(os.getcwd()) != 'ref_bias':
    os.chdir('/gpfs0/work/alex/ref_bias')


Ns = list(range(-150,151))

chroms = ['All', 'chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', \
    'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY', 'chrM'][1:-2]

with open("snp_positions_dict.pkl", "rb") as f:
        snp_positions = pickle.load(f)

def extract_counts(chrom, positions, Ns):
    input_file = f"../large_files/dumps/{chrom}_VC_dump.out"
    
    with open(input_file, "r") as infile, open(f"../large_files/fixed_cpulls_300/{chrom}_VC_snp_counts_{min(Ns)}_{max(Ns)}.out", "w+") as outfile:
        lines = infile.readlines()
        ln = ":".join([str(N).strip() for N in Ns])
        outfile.write(ln)
        for pos in positions:
            line = []
            if pos+max(Ns) < len(lines) and pos-min(Ns) >= 0:
                for N in Ns:
                    line.append(lines[pos+N])
            outfile.write(":".join(line)+"\n")
                
        

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for chrom in chroms:
        if chrom in snp_positions:
            futures.append(executor.submit(extract_counts, chrom, snp_positions[chrom], Ns))
    concurrent.futures.wait(futures)
print("\n=====Done=====\n")