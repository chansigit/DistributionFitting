DistIdentify

This python package helps to identify which distribution a series of numbers follows.
Current version supports continous random variable only.

By default, this package can automatically calculates the negative log likelihood of 69 probability distributions, including:

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
    st.lomax, st.maxwell, st.mielke, st.ncf

,which are provided by `scipy.stats` model.

You can also manually specify a subset of distributions above as candidates for fitting.

See Test.DistIdentify.py for usage.


Referenced Codes
https://stackoverflow.com/questions/6620471/fitting-empirical-distribution-to-theoretical-ones-with-scipy-python

All rights reserved by Sijie Chen