import numpy as np
import scipy
import scipy.stats as st
import matplotlib.pyplot as pyplot

size= 100

#data = np.random.random(size)*50
data = np.random.normal(loc=20, scale=3.57,size=size)
print(data)
bins = np.linspace(-10, 60, 60)
pyplot.hist(data, bins=bins, alpha=0.5)
pyplot.xlim(0,60)
#pyplot.show()


candidate_dists = [st.laplace, st.norm]
results=[]
for dist in candidate_dists:
    esti_params = dist.fit(data)
    mle = dist.nnlf(esti_params, data)
    results.append((dist.name, mle))
    print((dist.name,esti_params))

    fitted = dist.pdf(bins,
                      *esti_params[:-2],
                      loc=esti_params[-2], scale=esti_params[-1]) * 100
    print(fitted)
    pyplot.plot(fitted, label=dist.name)
    pyplot.xlim(0,60)

pyplot.legend(loc='upper right')
pyplot.show()
