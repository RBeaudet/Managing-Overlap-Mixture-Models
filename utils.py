import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def Compute_accuracy(list_U, U_true, thresh=0, burn_in=1000):

    U = sum(list_U[burn_in:-1])/(len(list_U)-burn_in)
    U = np.vectorize(round)(U)
    return (np.abs(U - U_true) <= thresh).sum()/(np.prod(np.shape(U)))


def plot_similarity(U, title='', save_path='/media/sf_Debian-shared-folder/', name='fig'):

    sns.set(style="white")
    mask = np.zeros_like(U, dtype=np.bool)
    fig, ax = plt.subplots(figsize=(11, 9))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(U, mask=mask, cmap=cmap, vmax=U.max(), center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.title(title)
    plt.savefig('{0}/{1}.png'.format(save_path, name))


def plot_n_clusters(list_Z, True_n_clusters,  burn_in=1000, title='', save_path='/media/sf_Debian-shared-folder/', name='fig'):

    to_plot = [(Z.sum(axis=0) > 0).sum() for Z in list_Z[burn_in:-1]]
    fig, ax = plt.subplots(figsize=(11, 9))
    ax.plot(np.linspace(burn_in, len(list_Z), num=len(list_Z)-burn_in-1), to_plot)
    ax.axhline(y=True_n_clusters, color='r', linestyle='-')
    plt.title(title)
    plt.savefig('{0}/{1}.png'.format(save_path, name))