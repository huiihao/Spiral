import numpy as np
import matplotlib.pylab as plt
from math import sqrt, pi
import matplotlib as mpl
#from palettable.colorbrewer.qualitative import Set1_8

from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.patheffects as path_effects
from matplotlib.legend_handler import HandlerTuple
import matplotlib.patches as mpatches

from matplotlib.colors import ListedColormap

#plt.style.use('nature.mplstyle')

plt.clf()
plt.close("all")

plt.rcParams.update( {'lines.markersize' : 7.7})
cutoff = 0.1

# Figure
fig = plt.figure(figsize=(4.72, 3.3))
gs = mpl.gridspec.GridSpec(1, 1, width_ratios=[1], left=0.03, right=0.95, wspace=0.0, height_ratios=[1], bottom=0.0, top=0.95, hspace=0.275)
axa = fig.add_subplot(gs[0])
#axa.set_box_aspect(1)
axa.axis('off')

ax1add = axa.inset_axes([-0.18, 0.09, 0.85, 0.85], transform=axa.transAxes)
ax1 = axa.inset_axes([0.3, 0.09, 0.8, 0.8], transform=axa.transAxes)
ax1add.axis('off')
#axE = axa.inset_axes([-0.035, 0.09, 0.48, 0.48], transform=axa.transAxes)

axa.text(-0.024, 1.05, 'a', ha='center', va='top', fontsize=8, fontweight='bold', transform=axa.transAxes)
axa.text(0.36, 1.05, 'b', ha='center', va='top', fontsize=8, fontweight='bold', transform=axa.transAxes)

# ground state a=b=3.8766394600045131 c=4.1866050603047533
#####################################################  DFT  #####################################################
ax1.set_box_aspect(1)

sss1=2.35
sss2=2.35
sss3=2.35

marker1='s'
marker2='^'
marker3='o'
marker4='D'
ecc='k'

file1="sortEmin1.log"
file2="sortEmin2.log"
file3="sortEmin3.log"
file4="sortEmin4.log"

#my_data = np.loadtxt(file1)
#X = my_data[:,0] 
#Y = my_data[:,1] 
#dx = np.abs(my_data[:,2])
#dy = np.abs(my_data[:,3])
#dz = np.abs(my_data[:,4])
#
#pp = np.sqrt(dx*dx + dy*dy + dz*dz)
#
#for i in range(len(X)):
#    if pp[i] < cutoff:
#        ax1.plot(X[i], Y[i], 's',color='gray',alpha=0.0, zorder=1)
#    else:
#        count = [0,0,0]
#        pj = pp[i]/sqrt(6.0)
#        if dx[i] >= 0.14:
#            count[0] = 1
#        elif 0.14 > dx[i] > 0.03:
#            count[0] = 0.5
#        if dy[i] >= 0.14:
#            count[1] = 1
#        elif 0.14 > dy[i] > 0.03:
#            count[1] = 0.5
#        if dz[i] >= 0.14:
#            count[2] = 1
#        elif 0.14 > dz[i] > 0.03:
#            count[2] = 0.5
#
#        if count == [0,0,0]:
#            print("You need test pj !!!")
#        elif count == [1,0,0]:
#            ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#        elif count == [0,1,0]:
#            ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#        elif count == [0,0,1]:
#            ax1.plot(X[i], Y[i], 's',color='#fad7b1', zorder=1)
#        elif count == [1,1,0]:
#            ax1.plot(X[i], Y[i], 's',color='#7fc986', zorder=1)
#        elif count == [0,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#        elif count == [1,0,1]:
#            ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#        elif count == [1,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#000000', zorder=1)
#        elif count == [0.5,0.5,0.5]:
#            ax1.plot(X[i], Y[i], 's',color='#00ffff', zorder=1)
#        
#        elif count == [0.5,0.5,1]: #M_A
#            ax1.plot(X[i], Y[i], 's',color='#ff0000', zorder=1)
#        elif count == [1,1,0.5]: #M_B
#            ax1.plot(X[i], Y[i], 's',color='#ff9977', zorder=1)
#        elif count == [0,0.5,1]: #M_C
#            ax1.plot(X[i], Y[i], 's',color='#800080', zorder=1)
#        elif count == [0.5,0,1]: #M_C
#            ax1.plot(X[i], Y[i], 's',color='#800080', zorder=1)
#        
#        elif count == [1,0.5,0.5]: #1MM
#            ax1.plot(X[i], Y[i], 's',color='#80b1d3', zorder=1)
#        elif count == [0.5,1,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#80b1d3', zorder=1)
#
#        elif count == [1,0,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bc80bd', zorder=1)
#        elif count == [0,1,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bc80bd', zorder=1)
#
#        elif count == [0.5,1,0]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bebada', zorder=1)
#        elif count == [1,0.5,0]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bebada', zorder=1)
#
#        elif count == [1,0.5,1]:
#            ax1.plot(X[i], Y[i], 's',color='#8dd3c7', zorder=1)
#        elif count == [0.5,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#8dd3c7', zorder=1)
#
#
#my_data = np.loadtxt(file1)
#X = my_data[:,1] 
#Y = my_data[:,0] 
#dx = np.abs(my_data[:,3])
#dy = np.abs(my_data[:,2])
#dz = np.abs(my_data[:,4])
#
#pp = np.sqrt(dx*dx + dy*dy + dz*dz)
#
#for i in range(len(X)):
#    if pp[i] < cutoff:
#        ax1.plot(X[i], Y[i], 's',color='gray',alpha=0.0, zorder=1)
#    else:
#        count = [0,0,0]
#        pj = pp[i]/sqrt(6.0)
#        if dx[i] >= 0.14:
#            count[0] = 1
#        elif 0.14 > dx[i] > 0.03:
#            count[0] = 0.5
#        if dy[i] >= 0.14:
#            count[1] = 1
#        elif 0.14 > dy[i] > 0.03:
#            count[1] = 0.5
#        if dz[i] >= 0.14:
#            count[2] = 1
#        elif 0.14 > dz[i] > 0.03:
#            count[2] = 0.5
#
#        if count == [0,0,0]:
#            print("You need test pj !!!")
#        elif count == [1,0,0]:
#            ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#        elif count == [0,1,0]:
#            ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#        elif count == [0,0,1]:
#            ax1.plot(X[i], Y[i], 's',color='#fad7b1', zorder=1)
#        elif count == [1,1,0]:
#            ax1.plot(X[i], Y[i], 's',color='#7fc986', zorder=1)
#        elif count == [0,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#        elif count == [1,0,1]:
#            ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#        elif count == [1,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#000000', zorder=1)
#        elif count == [0.5,0.5,0.5]:
#            ax1.plot(X[i], Y[i], 's',color='#00ffff', zorder=1)
#
#        elif count == [0.5,0.5,1]: #M_A
#            ax1.plot(X[i], Y[i], 's',color='#ff0000', zorder=1)
#        elif count == [1,1,0.5]: #M_B
#            ax1.plot(X[i], Y[i], 's',color='#ff9977', zorder=1)
#        elif count == [0,0.5,1]: #M_C
#            ax1.plot(X[i], Y[i], 's',color='#800080', zorder=1)
#        elif count == [0.5,0,1]: #M_C
#            ax1.plot(X[i], Y[i], 's',color='#800080', zorder=1)
#
#        elif count == [1,0.5,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#80b1d3', zorder=1)
#        elif count == [0.5,1,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#80b1d3', zorder=1)
#
#        elif count == [1,0,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bc80bd', zorder=1)
#        elif count == [0,1,0.5]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bc80bd', zorder=1)
#
#        elif count == [0.5,1,0]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bebada', zorder=1)
#        elif count == [1,0.5,0]: #?
#            ax1.plot(X[i], Y[i], 's',color='#bebada', zorder=1)
#
#        elif count == [1,0.5,1]:
#            ax1.plot(X[i], Y[i], 's',color='#8dd3c7', zorder=1)
#        elif count == [0.5,1,1]:
#            ax1.plot(X[i], Y[i], 's',color='#8dd3c7', zorder=1)
#
#my_data = np.loadtxt(file2)
#X = my_data[:,0] - 0.000
#Y = my_data[:,1] - 0.0005
#dx = np.abs(my_data[:,2])
#dy = np.abs(my_data[:,3])
#dz = np.abs(my_data[:,4])
#
#pp = np.sqrt(dx*dx + dy*dy + dz*dz)
#
#for i in range(len(X)):
#    if pp[i] < cutoff:
#        ax1.plot(X[i], Y[i], 's',color='gray',alpha=0.0, zorder=1)
#    else:
#        count = [0,0,0]
#        pj = pp[i]/sqrt(6.0)
#        if dx[i] >= 0.14:
#            count[0] = 1
#        elif 0.14 > dx[i] > 0.03:
#            count[0] = 0.5
#        if dy[i] >= 0.14:
#            count[1] = 1
#        elif 0.14 > dy[i] > 0.03:
#            count[1] = 0.5
#        if dz[i] >= 0.14:
#            count[2] = 1
#        elif 0.14 > dz[i] > 0.03:
#            count[2] = 0.5
#
#        if count == [0,0,0]:
#            print("You need test pj !!!")
#        elif count == [1,0,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#fad7b1',alpha=0.8, zorder=1)
#            #ax1.plot(X[i], Y[i], 's',color='#fabfd2', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#fad7b1', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [1,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#7fc986', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#7fc986', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [1,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [1,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#00ffff', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#000000', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0.5,0.5,0.5]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#00ffff', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,0.5,1]: #M_A
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff0000', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [1,1,0.5]: #M_B
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff9977', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0,0.5,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0.5,0,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#        elif count == [1,0,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0,1,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,1,0]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [1,0.5,0]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,1]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,1]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss3, linewidths=0.05, zorder=3)
#
#
#my_data = np.loadtxt(file3)
#X = my_data[:,0] + 0.000
#Y = my_data[:,1] + 0.0000
#dx = np.abs(my_data[:,2])
#dy = np.abs(my_data[:,3])
#dz = np.abs(my_data[:,4])
#
#pp = np.sqrt(dx*dx + dy*dy + dz*dz)
#
#for i in range(len(X)):
#    if pp[i] < cutoff:
#        ax1.plot(X[i], Y[i], 's',color='gray',alpha=0.0, zorder=1)
#    else:
#        count = [0,0,0]
#        pj = pp[i]/sqrt(6.0)
#
#        if dx[i] >= 0.14:
#            count[0] = 1
#        elif 0.14 > dx[i] > 0.03:
#            count[0] = 0.5
#        if dy[i] >= 0.14:
#            count[1] = 1
#        elif 0.14 > dy[i] > 0.03:
#            count[1] = 0.5
#        if dz[i] >= 0.14:
#            count[2] = 1
#        elif 0.14 > dz[i] > 0.03:
#            count[2] = 0.5
#
#        if count == [0,0,0]:
#            print("You need test pj !!!")
#        elif count == [1,0,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#fad7b1',alpha=0.8, zorder=1)
#            #ax1.plot(X[i], Y[i], 's',color='#fabfd2', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#fad7b1', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [1,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#7fc986', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#7fc986', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [1,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [1,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#00ffff', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#000000', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0.5,0.5,0.5]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#00ffff', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,0.5,1]: #M_A
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff0000', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [1,1,0.5]: #M_B
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff9977', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0,0.5,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0.5,0,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#        elif count == [1,0,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0,1,0.5]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,1,0]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [1,0.5,0]: #?
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,1]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,1]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss2, linewidths=0.05, zorder=3)
#
#
#my_data = np.loadtxt(file4)
#X = my_data[:,0] - 0.000
#Y = my_data[:,1] + 0.0005
#dx = np.abs(my_data[:,2])
#dy = np.abs(my_data[:,3])
#dz = np.abs(my_data[:,4])
#
#pp = np.sqrt(dx*dx + dy*dy + dz*dz)
#
#for i in range(len(X)):
#    if pp[i] < cutoff:
#        ax1.plot(X[i], Y[i], 's',color='gray',alpha=0.0, zorder=1)
#    else:
#        count = [0,0,0]
#        pj = pp[i]/sqrt(6.0)
#
#        if dx[i] >= 0.14:
#            count[0] = 1
#        elif 0.14 > dx[i] > 0.03:
#            count[0] = 0.5
#        if dy[i] >= 0.14:
#            count[1] = 1
#        elif 0.14 > dy[i] > 0.03:
#            count[1] = 0.5
#        if dz[i] >= 0.14:
#            count[2] = 1
#        elif 0.14 > dz[i] > 0.03:
#            count[2] = 0.5
#
#        if count == [0,0,0]:
#            print("You need test pj !!!")
#        elif count == [1,0,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#008000', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#008000', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#fad7b1',alpha=0.8, zorder=1)
#            #ax1.plot(X[i], Y[i], 's',color='#fabfd2', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#fad7b1', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [1,1,0]:
#            #ax1.plot(X[i], Y[i], 's',color='#7fc986', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#7fc986', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [1,0,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#ffff00', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ffff00', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [1,1,1]:
#            #ax1.plot(X[i], Y[i], 's',color='#00ffff', zorder=1)
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#000000', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0.5,0.5,0.5]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#00ffff', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,0.5,1]: #M_A
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff0000', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [1,1,0.5]: #M_B
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#ff9977', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0,0.5,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0.5,0,1]: #M_C
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#800080', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,0.5]: #vuu
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,0.5]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#80b1d3', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#
#        elif count == [1,0,0.5]: #v0u
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0,1,0.5]: 
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bc80bd', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#
#        elif count == [0.5,1,0]: 
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [1,0.5,0]: #vu0
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#bebada', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#
#        elif count == [1,0.5,1]: #vuv
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)
#        elif count == [0.5,1,1]:
#            ax1.scatter(X[i], Y[i], alpha=0.9, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=sss1, linewidths=0.05, zorder=3)

ax1t = ax1.twiny()
ax1t.set_box_aspect(1)

ax1.set_xlabel(r'$a$ ($\rm \AA$)')#, labelpad=3.6)
ax1.set(xlim=(3.9309,3.9731))
ax1.set_xticks(np.linspace(3.932, 3.972, 6))

ax1s = ax1.twinx()
ax1s.set_box_aspect(1)

ax1.set_ylabel(r'$b$ ($\rm \AA$)')#, labelpad=3.6)
ax1.set(ylim=(3.9309,3.9731))
ax1.set_yticks(np.linspace(3.932, 3.972, 6))

#ax1.xaxis.set_major_locator(plt.MaxNLocator(11))
#ax1.yaxis.set_major_locator(plt.MaxNLocator(11))
#ax1.set_xlabel(r'$a$ ($\rm \AA$)')
#ax1.set_ylabel(r'$b$ ($\rm \AA$)')
ax1t.set_xlabel(r'$\varepsilon_a$ (%)')
ax1s.set_ylabel(r'$\varepsilon_b$ (%)', rotation=-90)

ax1t.set_xlim([3.9309,3.9731])
ax1s.set_ylim([3.9309,3.9731])

x_labels = [1.5, 1.8, 2.1, 2.4]
x_ticks = [3.8766394600045131*(1.5/100+1), 3.8766394600045131*(1.8/100+1), 3.8766394600045131*(2.1/100+1), 3.8766394600045131*(2.4/100+1)]
ax1t.set_xticks(x_ticks)
ax1t.set_xticklabels(x_labels)

y_labels = [1.5, 1.8, 2.1, 2.4]
y_ticks = [3.8766394600045131*(1.5/100+1), 3.8766394600045131*(1.8/100+1), 3.8766394600045131*(2.1/100+1), 3.8766394600045131*(2.4/100+1)]
ax1s.set_yticks(y_ticks)
ax1s.set_yticklabels(y_labels)

ax1t.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(3))
ax1s.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(3))

ax1.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
ax1.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))

#对角线
ax1.plot(np.linspace(3.931, 3.973, 2), np.linspace(3.931, 3.973, 2), alpha=0.9, ls='-', c='k', lw=0.3, zorder=2)
#ax1.plot(np.linspace(3.941, 3.967, 2), np.linspace(3.941, 3.967, 2), alpha=1, ls='-', c='k', lw=0.8, zorder=2)

#cphase4='#f4f7f7'
#cphase3='#aacfd0'
#cphase2='#79a8a9'
#cphase1='#1f4e5f'

#ax1.text(3.971, 3.972, '1', ha='center', va='center', size=5, color='k', path_effects=[path_effects.Stroke(linewidth=1, foreground='w'), path_effects.Normal()], zorder=10)

#patch1 = mpatches.Patch(color='#fad7b1', label=r'$[001]$')
#patch2 = mpatches.Patch(color='#ffff00', label=r'$[101]$')
#patch4 = mpatches.Patch(color='#7fc986', label=r'$[110]$')
##patch3 = mpatches.Patch(color='#000000', label=r'$[111]$')
##patch5 = mpatches.Patch(color='#008000', label=r'$[100]$')
#patch5 = mpatches.Patch(color='#008000', label=r'$[100]$')
#patch6 = mpatches.Patch(color='#00ffff', label=r'$[uuu]$')
#legend = ax1.legend(handles=[patch1,patch2,patch4,patch5,patch6], loc='upper left', ncol=6, frameon=False, bbox_to_anchor=(-0.02, 1.12), columnspacing=1.8, handlelength=0.8)
#ax1.add_artist(legend)
#
#patch1 = mpatches.Patch(color='#ff0000', label=r'$M_A[uuv]$')
#patch2 = mpatches.Patch(color='#ff9977', label=r'$M_B[vvu]$')
#patch3 = mpatches.Patch(color='#800080', label=r'$M_C[u0v]$')
#patch4 = mpatches.Patch(color='#80b1d3', label=r'$[vuu]$')
#patch5 = mpatches.Patch(color='#bc80bd', label=r'$[v0u]$')
#patch6 = mpatches.Patch(color='#bebada', label=r'$[vu0]$')
#patch7 = mpatches.Patch(color='#8dd3c7', label=r'$[vuv]$')
#legend = ax1.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6,patch7], loc='upper left', ncol=7, frameon=False, bbox_to_anchor=(-0.02, 1.07), columnspacing=1., handlelength=0.8)
#ax1.add_artist(legend)

patch1 = mpatches.Patch(color='#fad7b1', label=r'$[001]$')
patch3 = mpatches.Patch(color='#ffff00', label=r'$[101]$')
patch5 = mpatches.Patch(color='#7fc986', label=r'$[110]$')
patch7 = mpatches.Patch(color='#008000', label=r'$[100]$')
patch9 = mpatches.Patch(color='#00ffff', label=r'$[uuu]$')
patch11 = mpatches.Patch(color='#80b1d3', label=r'$[1uu]$')
patch2 = mpatches.Patch(color='#ff0000', label=r'$M_A[uu1]$')
patch4 = mpatches.Patch(color='#ff9977', label=r'$M_B[11u]$')
patch6 = mpatches.Patch(color='#800080', label=r'$M_C[u01]$')
patch8 = mpatches.Patch(color='#bc80bd', label=r'$[10u]$')
patch10 = mpatches.Patch(color='#bebada', label=r'$[1u0]$')
patch12 = mpatches.Patch(color='#8dd3c7', label=r'$[1u1]$')
legend = ax1.legend(handles=[patch1,patch2,patch3,patch4,patch5,patch6,patch7,patch8,patch9,patch10,patch11,patch12], loc='upper left', ncol=6, frameon=False, bbox_to_anchor=(-0.015, 1.20), columnspacing=1.4, handlelength=1)
ax1.add_artist(legend)


########################  detail  ###############################
ax1detail = ax1add.inset_axes([0.275, 1.015, 0.1, 0.1], transform=ax1add.transAxes)
ax1detailk = ax1add.inset_axes([0.46, 1.015, 0.1, 0.1], transform=ax1add.transAxes)
ax1detailm = ax1add.inset_axes([0.516, 1.015, 0.1, 0.1], transform=ax1add.transAxes)

ax1detail.axis('off')
ax1detail.set_box_aspect(1)
ax1detailk.axis('off')
ax1detailk.set_box_aspect(1)
ax1detailk.set(xlim=(0, 1), ylim=(0, 1))
ax1detailk.set_facecolor('none')

ax1detail.set(xlim=(0, 1), ylim=(0, 1))
ax1detail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='k', alpha=0.2)#fill=None, hatch='//')
ax1detail.add_patch(p)

ax1detailk.scatter(0.5, 0.20, alpha=1, marker=marker4, c='k', edgecolor='k', s=15, linewidths=0.1, zorder=3)
ax1detailk.scatter(0.5, 0.50, alpha=1, marker=marker4, c='grey', edgecolor='k', s=15, linewidths=0.1, zorder=3)
ax1detailk.scatter(0.5, 0.80, alpha=1, marker=marker4, c='w', edgecolor='k', s=15, linewidths=0.1, zorder=3)

ax1detail.text(-0.55, 0.5, 'Ground\nstate', ha='center', va='center', fontsize=5.5, fontweight='bold', transform=ax1detail.transAxes)
ax1detailk.text(1.2, 0.1, 'Low-$E$', ha='center', va='center', fontsize=5.5, fontweight='bold', transform=ax1detailk.transAxes)
ax1detailk.text(1.2, 0.9, 'High-$E$', ha='center', va='center', fontsize=5.5, fontweight='bold', transform=ax1detailk.transAxes)
ax1detailk.text(-0.55, 0.5, 'Metastable\nstates', ha='center', va='center', fontsize=5.5, fontweight='bold', transform=ax1detailk.transAxes)

ax1detailm.axis('off')
ax1detailm.set_box_aspect(1)
ax1detailm.set(xlim=(0, 1), ylim=(0, 1))
ax1detailm.set_facecolor('none')
ax1detailm.arrow(0.45, 0.29, 0.0,  0.4, color='k', head_length = 0.07, head_width = 0.06, length_includes_head = True, zorder=9,alpha=0.9)

################################################ example
#         3.946
# 3.9460000000	3.9460000000	0.0000000000	0.0000000000	0.2547044208
# 3.9460000000 3.9460000000 0.123115200 0.123115200 0.151717514
# 3.9460000000 3.9460000000 0.152065687 0.152065687 0.000000000

axa = ax1add.inset_axes([0.16, 0.66, 0.25, 0.25], transform=ax1add.transAxes)
axa.set_box_aspect(1)
axa.axis('off')
image = plt.imread('./final_a3.946_b3.946_green.png')
im = axa.imshow(image)

axadetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axa.transAxes)
axadetail.axis('off')
axadetail.set_box_aspect(1)
axadetail.set(xlim=(0, 1), ylim=(0, 1))
axadetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#fad7b1', alpha=1)#fill=None, hatch='//')
axadetail.add_patch(p)

axadetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#ff0000', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axadetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#7fc986', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)

axadetail.text(-1.1, 0.90, r'$a$$=3.946$', ha='center', va='top', fontsize=6, fontweight='bold')
axadetail.text(-1.1, 0.45, r'$b$$=3.946$', ha='center', va='top', fontsize=6, fontweight='bold')

axaa = axa.inset_axes([0.0, 0.0, 1, 1], transform=axa.transAxes)
axaa.axis('off')
axaa.set_box_aspect(1)
axaa.set_facecolor('none')
axaa.set(xlim=(0, 1), ylim=(0, 1.))

#axaa.scatter([0.49], [0.56],  c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.307], [0.862], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.711], [0.764], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.31], [0.27],   c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)

#solve {  0.862=a*(0.307)+b,  0.764=a*(0.711)+b  }
x = np.arange(0.308, 0.711, 0.001)
a=-49/202
b=189167/202000
y = a*x+b
axaa.plot(x, y, alpha=0.4, ls='-', c='k', lw=0.4)

#solve {  0.27=a*(0.31)+b,  0.56=a*(0.49)+b  }
x = np.arange(0.49, 2119633/3370000, 0.001)
a=29/18
b=-413/1800
y = a*x+b
axaa.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

#solve {  y=x*(29/18)+(-413/1800),  y=x*(-49/202)+(189167/202000)  }
axaa.scatter([2119633/3370000], [5283473/6740000],   c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)

axaa.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axaa.text(0.57, 0.5, r'$M_A$', ha='center', va='top', fontsize=6, fontweight='normal')
axaa.text(0.69, 0.16, '[110]', ha='center', va='top', fontsize=5, fontweight='normal')


#3.946 c dz 0.2547044208
####################################        3.948
#3.9480000000 3.94800000   0.	       0.          0.2531457919 norm 0 0 0.99388063664	 
#3.9480000000 3.9480000000 0.134797880 0.134797880 0.124394394  norm 0.52923258880 0.52923258880 0.488387259
#3.9480000000 3.9480000000 0.153182400 0.153182400 0.000000000  norm 0.60141241 0.60141241 0

axa = ax1add.inset_axes([0.37, 0.66, 0.25, 0.25], transform=ax1add.transAxes)
axa.set_box_aspect(1)
axa.axis('off')
image = plt.imread('./final_a3.948_b3.948_green.png')
im = axa.imshow(image)

axadetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axa.transAxes)
axadetail.axis('off')
axadetail.set_box_aspect(1)
axadetail.set(xlim=(0, 1), ylim=(0, 1))
axadetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#fad7b1', alpha=1)#fill=None, hatch='//')
axadetail.add_patch(p)

axadetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#00ffff', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axadetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#7fc986', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)

axadetail.text(-1.1, 0.90, r'$a$$=3.948$', ha='center', va='top', fontsize=6, fontweight='bold')
axadetail.text(-1.1, 0.45, r'$b$$=3.948$', ha='center', va='top', fontsize=6, fontweight='bold')

axaa = axa.inset_axes([0.0, 0.0, 1, 1], transform=axa.transAxes)
axaa.axis('off')
axaa.set_box_aspect(1)
axaa.set_facecolor('none')
axaa.set(xlim=(0, 1), ylim=(0, 1.))

#axaa.scatter([0.49], [0.56],  c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.307], [0.862], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.711], [0.764], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axaa.scatter([0.31], [0.27],   c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)

##solve {  0.862=a*(0.307)+b,  0.764=a*(0.711)+b  }
#x = np.arange(0.308, 0.711, 0.001)
#a=-49/202
#b=189167/202000
#y = a*x+b
#axaa.plot(x, y, alpha=0.4, ls='-', c='k', lw=0.4)
##solve {  0.27=a*(0.31)+b,  0.56=a*(0.49)+b  }
#x = np.arange(0.49, 2119633/3370000, 0.001)
#a=29/18
#b=-413/1800
#y = a*x+b
#axaa.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)
##solve {  y=x*(29/18)+(-413/1800),  y=x*(-49/202)+(189167/202000)  }
#axaa.scatter([2119633/3370000], [5283473/6740000],   c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)

axaa.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axaa.text(0.65, 0.52, '[uuu]', ha='center', va='top', fontsize=5, fontweight='normal')
axaa.text(0.69, 0.16, '[110]', ha='center', va='top', fontsize=5, fontweight='normal')


####################################        3.954
# 3.9540000000 3.9540000000 0.154469600 0.154469600 0.0452878953   norm  0.606466113 0.606466113 0.177805690
# 3.9540000000 3.9540000000 0.156697020 0.156697020 0.000000000    norm  0.615211230 0.615211230 0
# 3.9540000000 3.9540000000 0.000000000 0.000000000 0.248927769    norm  0           0           0.977320175
# 3.9540000000 3.9540000000 0.155998480 0.000000000 0.160081513    norm  0.612468678 0           0.628499154

axb = ax1add.inset_axes([0.16, 0.285, 0.25, 0.25], transform=ax1add.transAxes)
axb.set_box_aspect(1)
axb.axis('off')
image = plt.imread('./final_a3.954_b3.954_green.png')
im = axb.imshow(image)

axbdetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axb.transAxes)
axbdetail.axis('off')
axbdetail.set_box_aspect(1)
axbdetail.set(xlim=(0, 1), ylim=(0, 1))
axbdetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#ff9977', alpha=1)#fill=None, hatch='//')
axbdetail.add_patch(p)
axbdetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#7fc986', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axbdetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#fad7b1', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axbdetail.scatter(0.5, 0.80, alpha=1, marker=marker4, c='#ffff00', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)

axbdetail.text(-1.1, 0.90, r'$a$$=3.954$', ha='center', va='top', fontsize=6, fontweight='bold')
axbdetail.text(-1.1, 0.45, r'$b$$=3.954$', ha='center', va='top', fontsize=6, fontweight='bold')

axbb = axb.inset_axes([0.0, 0.0, 1, 1], transform=axb.transAxes)
axbb.axis('off')
axbb.set_box_aspect(1)
axbb.set_facecolor('none')
axbb.set(xlim=(0, 1), ylim=(0, 1.))

#axbb.scatter([0.16], [0.635], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axbb.scatter([0.315], [0.27], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axbb.scatter([0.31], [0.27], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axbb.scatter([0.58], [0.288], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)

#solve {  0.27=a*(0.31)+b,  0.288=a*(0.58)+b  }
x = np.arange(0.55, 0.711, 0.001)
a=1/15
b=187/750
y = a*x+b
axbb.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

#solve {  0.788=a*(0.091)+b,  0.635=a*(0.16)+b  }
x = np.arange(0.091, 0.18, 0.001)
a=-51/23
b=4553/4600
y = a*x+b
axbb.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

#solve {  y=x*(-73/31)+(6273/6200),  x=0.097  }
axbb.scatter([0.091], [0.788],   c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)

#solve {  y=x*(1/15)+(187/750),  x=0.711  }
axbb.scatter([0.711], [4451/15000],   c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)

axbb.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axbb.text(0.56, 0.45,r'$M_B$', ha='center', va='top', fontsize=6, fontweight='normal')
axbb.text(0.69, 0.16, '[110]', ha='center', va='top', fontsize=5, fontweight='normal')
axbb.text(0.06, 0.50, '[101]', ha='center', va='top', fontsize=5, fontweight='normal')

###########################################     3.958
# 3.9580000000	3.958000000 0.1590192467 0.1590192467 -0.0000000000   norm  0.624328570 0.624328570 0
# 3.9580000000 3.9580000000 0.000000000 0.000000000 0.245997762       norm  0           0           0.965816617
# 3.9580000000 3.9580000000 0.137883527 0.000000000 0.183145724       norm  0.541347208 0           0.719052003

axc = ax1add.inset_axes([0.37, 0.285, 0.25, 0.25], transform=ax1add.transAxes)
axc.set_box_aspect(1)
axc.axis('off')
image = plt.imread('./final_a3.958_b3.958_green.png')
im = axc.imshow(image)

axcdetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axc.transAxes)
axcdetail.axis('off')
axcdetail.set_box_aspect(1)
axcdetail.set(xlim=(0, 1), ylim=(0, 1))
axcdetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#7fc986', alpha=1)#fill=None, hatch='//')
axcdetail.add_patch(p)
axcdetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#fad7b1', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axcdetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#800080', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
#axcdetail.scatter(0.5, 0.80, alpha=1, marker=marker4, c='', edgecolor=ecc,    s=10, linewidths=0.1, zorder=3)

#3.8766394600045131
axcdetail.text(-1.1, 0.90, r'$a$$=3.958$', ha='center', va='top', fontsize=6, fontweight='bold')
axcdetail.text(-1.1, 0.45, r'$b$$=3.958$', ha='center', va='top', fontsize=6, fontweight='bold')

axcc = axc.inset_axes([0.0, 0.0, 1, 1], transform=axc.transAxes)
axcc.axis('off')
axcc.set_box_aspect(1)
axcc.set_facecolor('none')
axcc.set(xlim=(0, 1), ylim=(0, 1.))

#axcc.scatter([0.18], [0.7], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
axcc.scatter([0.145], [0.81], c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)

#solve {  0.7=a*(0.18)+b,  0.81=a*(0.15)+b  }
x = np.arange(0.15, 0.195, 0.001)
a=-11/3
b=34/25
y = a*x+b
axcc.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

axcc.text(0.16, 0.50,r'$M_C$', ha='center', va='top', fontsize=6, fontweight='normal')
axcc.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.69, 0.16, '[110]', ha='center', va='top', fontsize=5, fontweight='normal')


###########################################         3.958 3.932
#3.9580000000	3.9320000000	0.0000  	0.0 0.2563332288 norm 0 0 1.00639489489379133697
#3.9580000000 3.9320000000 0.032086187 0.000000000 0.253235210   norm 0.125974205 0 0.9942317027895
#3.9580000000 3.9320000000 0.151525433 0.081693853 0.153646459   norm 0.59490696126935854110 0.32073983146192804518 0.60323436286426639046
#3.9580000000 3.9320000000 0.188466767 0.101484920 0.000000000   norm 0.73994305402334814912 0.39844192606177175547 0

axc = ax1add.inset_axes([0.16, -0.09, 0.25, 0.25], transform=ax1add.transAxes)
axc.set_box_aspect(1)
axc.axis('off')
image = plt.imread('./final_a3.958_b3.932_green.png')
im = axc.imshow(image)

axcdetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axc.transAxes)
axcdetail.axis('off')
axcdetail.set_box_aspect(1)
axcdetail.set(xlim=(0, 1), ylim=(0, 1))
axcdetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#fad7b1', alpha=1)#fill=None, hatch='//')
axcdetail.add_patch(p)
axcdetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#800080', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axcdetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#8dd3c7', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axcdetail.scatter(0.5, 0.80, alpha=1, marker=marker4, c='#bebada', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)

#3.8766394600045131
axcdetail.text(-1.1, 0.90, r'$a$$=3.958$', ha='center', va='top', fontsize=6, fontweight='bold')
axcdetail.text(-1.1, 0.45, r'$b$$=3.932$', ha='center', va='top', fontsize=6, fontweight='bold')

axcc = axc.inset_axes([0.0, 0.0, 1, 1], transform=axc.transAxes)
axcc.axis('off')
axcc.set_box_aspect(1)
axcc.set_facecolor('none')
axcc.set(xlim=(0, 1), ylim=(0, 1.))

##axcc.scatter([0.18], [0.7], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axcc.scatter([0.15], [0.81], c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)
##solve {  0.7=a*(0.18)+b,  0.81=a*(0.15)+b  }
#x = np.arange(0.15, 0.195, 0.001)
#a=-11/3
#b=34/25
#y = a*x+b
#axcc.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

axcc.text(0.16, 0.78,r'$M_C$', ha='center', va='top', fontsize=6, fontweight='normal')
axcc.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.55, 0.16, '[1u0]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.53, 0.58, '[1u1]', ha='center', va='top', fontsize=5, fontweight='normal')


###########################################         3.968 3.932
#3.9680000000	3.9320000000	0.2013760000	0.0832535467 0.00 norm 0.79062624577735637009 0.32686337535292595125 0
#3.9680000000 3.9320000000 0.197474133 0.082650640 0.052775297    norm 0.77530704955867809578 0.32449629158537165052 0.20720212407086732434
#3.9680000000 3.9320000000 0.208505173 0.000000000 0.052364579    norm 0.81861623110076776492 0 0.20558959611116416083
#3.9680000000 3.9320000000 0.000000000 0.000000000 0.252125038    norm 0 0 0.98987303482248785530

axc = ax1add.inset_axes([0.37, -0.09, 0.25, 0.25], transform=ax1add.transAxes)
axc.set_box_aspect(1)
axc.axis('off')
image = plt.imread('./final_a3.968_b3.932_green.png')
im = axc.imshow(image)

axcdetail = ax1.inset_axes([0.64, 1.00, 0.28, 0.28], transform=axc.transAxes)
axcdetail.axis('off')
axcdetail.set_box_aspect(1)
axcdetail.set(xlim=(0, 1), ylim=(0, 1))
axcdetail.set_facecolor('none')

p = mpatches.Rectangle((0,0), 1, 1, linewidth=0, facecolor='#bebada', alpha=1)#fill=None, hatch='//')
axcdetail.add_patch(p)
axcdetail.scatter(0.5, 0.20, alpha=1, marker=marker4, c='#80b1d3', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axcdetail.scatter(0.5, 0.50, alpha=1, marker=marker4, c='#bc80bd', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)
axcdetail.scatter(0.5, 0.80, alpha=1, marker=marker4, c='#fad7b1', edgecolor=ecc, s=8., linewidths=0.1, zorder=3)

#3.8766394600045131
axcdetail.text(-1.1, 0.90, r'$a$$=3.968$', ha='center', va='top', fontsize=6, fontweight='bold')
axcdetail.text(-1.1, 0.45, r'$b$$=3.932$', ha='center', va='top', fontsize=6, fontweight='bold')

axcc = axc.inset_axes([0.0, 0.0, 1, 1], transform=axc.transAxes)
axcc.axis('off')
axcc.set_box_aspect(1)
axcc.set_facecolor('none')
axcc.set(xlim=(0, 1), ylim=(0, 1.))

##axcc.scatter([0.18], [0.7], c='k', marker='.', s=1, edgecolors='k', lw=0.5, zorder=9)
#axcc.scatter([0.15], [0.81], c='red', marker='.', s=1, edgecolors='red', lw=0.5, zorder=9)
##solve {  0.7=a*(0.18)+b,  0.81=a*(0.15)+b  }
#x = np.arange(0.15, 0.195, 0.001)
#a=-11/3
#b=34/25
#y = a*x+b
#axcc.plot(x, y, alpha=0.4, ls='--', c='k', lw=0.4)

axcc.text(0.14, 0.44, '[10u]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.47, 0.92, '[001]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.50, 0.16, '[1u0]', ha='center', va='top', fontsize=5, fontweight='normal')
axcc.text(0.50, 0.42, '[1uu]', ha='center', va='top', fontsize=5, fontweight='normal')

#3.9720000000	3.9320000000	0.2059482000	0.0765429333	0.0000000000	
#3.9720000000 3.9320000000 0.213971640 0.000000000 0.024987542

######################################################################################################################################################
# Save
fig.savefig('Fig1.png')
fig.savefig('Fig1.pdf')

# 清空绘图缓存
plt.clf()

