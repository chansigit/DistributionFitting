import numpy as np
import scipy
import scipy.stats as st
import matplotlib.pyplot as pyplot
from pdb import set_trace
import sys
import warnings
from tabulate import tabulate


class DistIdentify:
    def __init__(self, data):
        self.data = data
        self.ndata = len(self.data)
        # default 69 candidate distribuions
        self.candidate_dists = [
                                    st.alpha, st.anglit, st.beta, st.bradford, st.burr,
                                    st.cauchy, st.cosine, st.dgamma, st.dweibull, st.erlang,
                                    st.expon, st.exponnorm, st.f, st.fatiguelife, st.fisk,
                                    st.foldcauchy, st.foldnorm, st.genlogistic, st.gennorm,
                                    st.gamma, st.gilbrat, st.gompertz, st.gumbel_r, st.genexpon,
                                    st.gumbel_l, st.halfcauchy, st.halflogistic, st.halfnorm,
                                    st.hypsecant, st.invgamma, st.invgauss, st.kstwobign,
                                    st.invweibull, st.johnsonsb, st.johnsonsu, st.ksone,
                                    st.laplace, st.levy, st.levy_l, st.levy_stable,
                                    st.logistic, st.loggamma, st.loglaplace, st.lognorm,
                                    st.nct, st.norm, st.pareto, st.pearson3, st.powerlaw,
                                    st.powerlognorm, st.powernorm, st.reciprocal, st.t,
                                    st.rayleigh, st.rice, st.recipinvgauss, st.semicircular,
                                    st.triang, st.truncexpon, st.truncnorm, st.tukeylambda,
                                    st.uniform, st.vonmises_line, st.wald, st.wrapcauchy,
                                    st.lomax, st.maxwell, st.mielke, st.ncf,
                                ]
        self.xmin = min(self.data)
        self.xmax = max(self.data)
    def setCandidateDists(self, distributionList):
        self.candidate_dists = distributionList

    def summary(self, plot=False, file=None):
        perc25  = np.percentile(self.data, 25)
        median  = np.percentile(self.data, 50)
        perc75  = np.percentile(self.data, 75)

        print("%d data items in total with mean=%.6f and std= %.6f\n"%
                (self.ndata, np.mean(self.data), np.std(self.data)) )
        print(tabulate([[self.xmin,perc25,median,perc75,self.xmax], ],
                        headers=['Min', '1/4 Quad','Median','3/4 Quad','Max'],
                        tablefmt='orgtbl'))
        if plot:
            bins = np.linspace(self.xmin, self.xmax, self.ndata)
            pyplot.hist(self.data, bins=bins, normed=True, alpha=0.7)
            pyplot.xlim(self.xmin, self.xmax)
            if file==None:
                pyplot.show()
            else:
                pyplot.savefig(file, dpi=1080)

    def fitting(self, plot, file=None):
        if plot:
            bins = np.linspace(self.xmin, self.xmax, self.ndata)
            pyplot.hist(self.data, bins=bins, normed=True, alpha=0.7)
            pyplot.xlim(self.xmin,self.xmax)

        fittingResults=[]
        for dist in self.candidate_dists:
            with warnings.catch_warnings():
                print("Processing:%s" % dist.name)
                try:
                    warnings.filterwarnings('ignore')
                    # Fit dist to data
                    params = dist.fit(self.data)

                    # get fitted parameters
                    arg   = params[:-2]
                    loc   = params[-2]
                    scale = params[-1]

                    # likelihood and putative
                    mle = dist.nnlf(params, self.data)
                    result = (dist.name, mle, params)
                    fittingResults.append(result)
                    print(params)
                    if plot:
                        # putative histogram bar height
                        putative_heights = dist.pdf(bins, *arg, loc=loc, scale=scale)
                        pyplot.plot(bins, putative_heights, label=dist.name)
                        pyplot.xlim(self.xmin, self.xmax)
                except NotImplementedError:
                    print(">> %s not implemented"% dist.name)
        fittingResults =  sorted(fittingResults, key=lambda x:x[1])
        for result in fittingResults:
            print("%s with likelihood %.4f"%(result[0], result[1]))
        if plot:
            pyplot.legend(loc='upper right')
            if file==None:
                pyplot.show()
            else:
                pyplot.savefig(file, dpi=1080)
        return fittingResults
