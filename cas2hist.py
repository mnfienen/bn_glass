import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
mpl.rcParams['pdf.fonttype'] = 42

infile = 'GLASS_NET_STEADY.cas'

fig_path = infile[:-4]
if os.path.exists(fig_path) == False:
    os.mkdir(fig_path)

indat = np.genfromtxt(infile,dtype=None,names=True)

allvars = open(infile,'r').readline().strip().split()

for cv in allvars:
    cdat = indat[cv]
    plt.figure()
    plt.hist(cdat,bins=60)
    plt.title('Histogram for %s' %(cv))
    plt.savefig(fig_path + '/' + cv + '.pdf')
