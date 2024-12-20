import os
import glob
import numpy as np
import pickle
from decimal import Decimal
from scipy import stats
import sys
import matplotlib.pyplot as plt

if os.path.basename(os.getcwd()) != 'ref_bias':
    os.chdir('/gpfs0/work/alex/ref_bias')

def import_snp_counts(directory):
    snp_counts = {}
    file_pattern = os.path.join(directory, '*.out')
    files = glob.glob(file_pattern)

    for file_path in files:
        file_name = os.path.basename(file_path)
        parts = file_name.split('_')
        key = parts[0]        
        with open(file_path, 'r') as file:
            data = file.readlines()
        snp_counts['offsets'] = np.array(data[0].strip().split(':'))
        snp_counts[key] = np.array([np.array(line.strip().split(':')).astype(float) for line in data[1:] if line.strip()])
    return snp_counts

directory = '../large_files/fixed_cpulls_300'

pkl_file = 'pkl_files/snp_counts_dict.pkl'

snp_counts = import_snp_counts(directory)

with open(pkl_file, 'wb') as f:
    pickle.dump(snp_counts, f)