import pickle
import os
import matplotlib.pyplot as plt

if os.path.basename(os.getcwd()) != 'ref_bias':
    os.chdir('/gpfs0/work/alex/ref_bias')

stats_pkl_file = 'pkl_files/stats_dict.pkl'   

with open(stats_pkl_file, 'rb') as f:
    stats_dict = pickle.load(f)

offsets = list(range(-150,151))

num_subplots = 4
fontsize = 15
for key, stats in stats_dict.items():
    x = offsets
    x = x[len(x)//2 - 75: len(x)//2 + 75]
    stats['means'] = stats['means'][len(stats['means'])//2 - 75: len(stats['means'])//2 + 75]
    stats['medians'] = stats['medians'][len(stats['medians'])//2 - 75: len(stats['medians'])//2 + 75]
    stats['std_devs'] = stats['std_devs'][len(stats['std_devs'])//2 - 75: len(stats['std_devs'])//2 + 75]
    stats['variances'] = stats['variances'][len(stats['variances'])//2 - 75: len(stats['variances'])//2 + 75]


    fig, ax = plt.subplots(num_subplots, figsize=(15,6*num_subplots), gridspec_kw={'hspace': 0.5})

    ax[0].plot(x, stats['means'], label='Mean')
    ax[0].set_title(f'{key} - Mean', fontsize=fontsize)

    ax[1].plot(x, stats['medians'], label='Median')
    ax[1].set_title(f'{key} - Median', fontsize=fontsize)

    ax[2].plot(x, stats['std_devs'], label='Std Dev')
    ax[2].set_title(f'{key} - Std Dev', fontsize=fontsize)

    ax[3].plot(x, stats['variances'], label='Variance')
    ax[3].set_title(f'{key} - Variance', fontsize=fontsize)

    for i in range(num_subplots):
        ax[i].set_xlabel('Offsets', fontsize=fontsize)
        ax[i].set_ylabel('Values', fontsize=fontsize)
        ax[i].legend(fontsize=fontsize)

    fig.savefig(f'graphs/{key}_stats.png')
    plt.close()
