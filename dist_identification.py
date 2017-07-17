import numpy as np
import scipy
import scipy.stats as st
import matplotlib.pyplot as pyplot
from pdb import set_trace
import sys
import warnings
data = np.random.normal(loc=40, scale=3.57,size=1000)
xmin = min(data)
xmax = max(data)
ndata= len(data)
print("std=",np.std(data))
print("mean=",np.mean(data))

bins = np.linspace(xmin, xmax, ndata)
pyplot.hist(data, bins=bins, normed=True, alpha=0.7)
pyplot.xlim(20,60)
#pyplot.show()
#sys.exit()


#candidate_dists = [st.laplace, st.norm]
candidate_dists = [st.norm, st.lognorm, st.gamma, st.weibull_min, st.chi2,
                   st.erlang, st.invweibull, st.invgauss, st.invgamma, st.beta]


fittingResults=[]
for dist in candidate_dists:
    with warnings.catch_warnings():
        print("Processing:%s" % dist.name)
        try:
            warnings.filterwarnings('ignore')
            # Fit dist to data
            params = dist.fit(data)

            # get fitted parameters
            arg   = params[:-2]
            loc   = params[-2]
            scale = params[-1]

            # likelihood and putative
            mle = dist.nnlf(params, data)
            result = (dist.name, mle, params)
            print(result)
            fittingResults.append(result)

            # putative histogram bar height
            putative_heights = dist.pdf(bins, *arg, loc=loc, scale=scale)

            pyplot.plot(bins, putative_heights, label=dist.name)
            pyplot.xlim(20, 60)
        except NotImplementedError:
            print(">> %s not implemented"% dist.name)
        # put result in the


pyplot.legend(loc='upper right')
pyplot.show()

set_trace()

fittingResults= sorted(fittingResults, key=lambda x:x[1])
for result in fittingResults:
    print("%s with likelihood %.4f"%(result[0], result[1]))
