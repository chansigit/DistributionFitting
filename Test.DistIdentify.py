import numpy as np
import scipy.stats as st
from DistIdentify.Shotgun import ShotgunIdentification

data = np.random.normal(loc=40, scale=3.57,size=500)
matcher = ShotgunIdentification(data=data)
matcher.summary( plot=True)
matcher.setCandidateDists([st.norm, st.lognorm, st.gamma, st.erlang, st.invweibull,st.invgauss, st.invgamma, st.beta])
#matcher.fitting(plot=True, file="fitting.pdf")
matcher.fitting(plot=True, file=None)
