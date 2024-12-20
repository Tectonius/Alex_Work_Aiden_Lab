import pickle
import os
import matplotlib.pyplot as plt

if os.path.basename(os.getcwd()) != 'ref_bias':
    os.chdir('/gpfs0/work/alex/ref_bias')

stats_pkl_file = 'pkl_files/stats_dict.pkl'   

with open(stats_pkl_file, 'rb') as f:
    stats_dict = pickle.load(f)

offsets = list(range(-150,151))

for key, stats in stats_dict.items():
    x = offsets
    x = x[len(x)//2 - 75: len(x)//2 + 75]
    stats['means'] = stats['means'][len(stats['means'])//2 - 75: len(stats['means'])//2 + 75]
    stats['medians'] = stats['medians'][len(stats['medians'])//2 - 75: len(stats['medians'])//2 + 75]
    stats['std_devs'] = stats['std_devs'][len(stats['std_devs'])//2 - 75: len(stats['std_devs'])//2 + 75]
    stats['variances'] = stats['variances'][len(stats['variances'])//2 - 75: len(stats['variances'])//2 + 75]
    plt.figure(figsize=(15, 6))
    print(f"x: {x}\n means: {stats['means']}")
    plt.plot(x, stats['means'], label='Mean')
    plt.title(f'{key} - Mean')
    plt.xlabel('Offsets')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig(f'graphs/{key}_mean.png')
    plt.close()

    plt.plot(x, stats['medians'], label='Median')
    plt.title(f'{key} - Median')
    plt.xlabel('Offsets')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig(f'graphs/{key}_median.png')
    plt.close()

    plt.plot(x, stats['std_devs'], label='Std Dev')
    plt.title(f'{key} - Std Dev')
    plt.xlabel('Offsets')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig(f'graphs/{key}_std_dev.png')
    plt.close()

    plt.plot(x, stats['variances'], label='Variance')
    plt.title(f'{key} - Variance')
    plt.xlabel('Offsets')
    plt.ylabel('Values')
    plt.legend()
    plt.savefig(f'graphs/{key}_variance.png')
    plt.close()