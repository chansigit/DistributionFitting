# -*- coding: utf-8 -*-
'''
Original Author：Toby
from http://www.cnblogs.com/webRobot/p/6760839.html
all right reversed,no commercial use

Modified by Sijie Chen
'''

import scipy
from scipy.stats import f
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
# additional packages
from statsmodels.stats.diagnostic import lillifors

# Normality Test
def normalityTest(data, pval_cutoff):
    """
    This function accepts a series of number and returns a 3-element tuple
    containing:
        A boolean Indicator(True for normal),
        A p-value ( < pval_cutoff ==> not normal ),
        Test Name
    """
    size = len(data)
    ## sample size < 50, use Shapiro-Wilk algorithm
    if size <50:
        p_value= stats.shapiro(data)[1]
        if p_value<0.05:
            return (False, p_value, "scipy.stats.shapiro")
        else:
            return (True, p_value, "scipy.stats.shapiro")

    ## 50<= sample size <=300, use Lillifors
    if 300>=size >=50:
        p_value= lillifors(data)[1]
        if p_value<0.05:
            return (False, p_value,"statsmodels.stats.diagnostic.lillifors")
        else:
            return (True, p_value,"statsmodels.stats.diagnostic.lillifors")

    ## sample size > 300, use Kolmogorov-Smirnov test
    if size >300:
        p_value= stats.kstest(data,'norm')[1]
        if p_value<0.05:
            return (False, p_value,"Kolmogorov-Smirnov")
        else:
            return (True, p_value,"Kolmogorov-Smirnov")
