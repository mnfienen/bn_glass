import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
mpl.rcParams['pdf.fonttype'] = 42

infiles = ['GLASS_NET_STEADY.cas','GLASS_NET_TRANS.cas','GLASS_NET_STEADY_CONSTQ.cas']

logme = ['Q_SUSTAINED','TRANGM']

for infile in infiles:
    fig_path = infile[:-4] + '_figs'
    if os.path.exists(fig_path) == False:
        os.mkdir(fig_path)
    
    indat = np.genfromtxt(infile,dtype=None,names=True)
    
    allvars = open(infile,'r').readline().strip().split()
    
    for cv in allvars:
        #plot histograms
        cdat = indat[cv]
        plt.figure()
        plt.hist(cdat,bins=60)
        plt.title('%s: Histogram for %s' %(infile[:-4],cv))
        plt.savefig(os.path.join(fig_path,'hist_' + cv + '.pdf'))
    
        #plot response graphs
        if cv != 'SW_SRC':
            fig = plt.figure()
            ax = fig.add_subplot(111)
            plt.plot(cdat,indat['SW_SRC'],'.')
            plt.title('%s: %s vs. SW_SRC' %(infile[:-4],cv))
            plt.xlabel(cv)
            if cv in logme:
                ax.set_xscale('log')
            plt.ylabel('SW_SRC')
            plt.savefig(os.path.join(fig_path,'descript_' + cv + '.pdf'))