import pickle
import numpy as np
from scipy import stats
import os

if os.path.basename(os.getcwd()) != 'ref_bias':
    os.chdir('/gpfs0/work/alex/ref_bias')

pkl_file = 'pkl_files/snp_counts_dict.pkl'

with open(pkl_file, 'rb') as f:
    snp_counts_dict = pickle.load(f)

offsets = snp_counts_dict.pop('offsets', None)

print(f"offsets: {offsets}")
def calculate_stats(snp_counts_dict):
    stats_dict = {}
    stats_dict['offsets'] = offsets
    for key, value in snp_counts_dict.items():
        value = np.array(value).astype(float)
        stats_dict[key] = {
            'means': np.mean(value, axis=0),
            'medians': np.median(value, axis=0),
            'std_devs': np.std(value, axis=0),
            'variances': np.var(value, axis=0),
            'mins': np.min(value, axis=0),
            'maxes': np.max(value, axis=0),
            'ranges': np.ptp(value, axis=0),
            'skewnesses': stats.skew(value, axis=0),
            'kurtosises': stats.kurtosis(value, axis=0),
        }

    return stats_dict

stats_pkl_file = 'pkl_files/stats_dict.pkl'   

stats_dict = calculate_stats(snp_counts_dict)
with open(stats_pkl_file, 'wb') as f:
    pickle.dump(stats_dict, f)
