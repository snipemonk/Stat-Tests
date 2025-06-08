# This code shows the implementation of the one sample t-test
# this test is used to check if the sample mean is significantly different from a known population mean

import math
from scipy.stats import t as t_dist
def one_sample_t_test(sample,population_mean,alpha=0.5):
    n = len(sample)
    sample_mean = sum(sample)/n
    sample_var = sum((x - sample_mean)**2 for x in sample)/(n-1)
    sample_std = math.sqrt(sample_var)

    t_stat = (sample_mean-population_mean)/(sample_std/math.sqrt(n))

    df = n-1

    p_value = 2*(1-t_dist.cdf(t_stat,df))

    reject_null = p_value < alpha
    return reject_null,p_value,t_stat



