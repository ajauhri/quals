#! /usr/bin/env python
import sys
import os

from optparse import OptionParser

# for plotting
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib
import math

params = {'legend.linewidth': 10}
plot_coords = [(0,0),(0,1),(1,0),(1,1)]
es_gens = {1:480, 2:3850, 3:8400, 4:1540 }
es_runs = {1:'0', 2:'3', 3:'2', 4:'1'}

plt.rcParams.update(params)
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
matplotlib.rcParams.update({'font.size': 8})

def main():
    parser = OptionParser()
    
    fig, ax = plt.subplots(2,2)
    fig.subplots_adjust(hspace=.5)
    for i in range(4):
        x_i = []
        y_i = []
        folder = "tc" + str(i+1)
        file = folder + "/" + folder + "_sa"  + "_r9_iters.csv"
        if os.path.exists(file):
            f = open(file, 'r')
            lines = f.readlines()
            for l in xrange(0, len(lines), len(lines)/50):
                iter = float(lines[l].split(",")[0])
                fitness = float(lines[l].split(",")[1])
                x_i.append(iter)#*es_gens[options.tc_id])
                y_i.append(fitness)
            x_i.append(lines[len(lines)-1].split(",")[0])
            y_i.append(lines[len(lines)-1].split(",")[1])

        plt.setp(ax[plot_coords[i][0], plot_coords[i][1]].get_xticklabels(), rotation=30)
        ax[plot_coords[i][0], plot_coords[i][1]].set_ylim((0.4,1))
        ax[plot_coords[i][0], plot_coords[i][1]].set_xlim((0,8000))
        ax[plot_coords[i][0], plot_coords[i][1]].plot(x_i, y_i, linestyle='-', marker='o', markersize=2)
        ax[plot_coords[i][0], plot_coords[i][1]].set_xlabel('evaluations', fontsize=10)
        ax[plot_coords[i][0], plot_coords[i][1]].set_ylabel('fitness', fontsize=10)
        ax[plot_coords[i][0], plot_coords[i][1]].set_title("Test Case " + str(i+1), fontsize=10)

    plt.tight_layout()
    plt.savefig('../FIG/sa.eps', format='eps', dpi=1000)
    plt.show()

if __name__ == "__main__":
    main()
