# This is an implementation of the Wilcoxon Test
from imagecodecs import none_decode

import math

def wilcoxon_test(x,y):

    import scipy.stats as stats

    #calculate the difference and remove zero difference
    diff = [a - b for a,b in zip(x,y)]
    non_zero = [(i,d) for i,d in enumerate(diff) if d!= 0]

    if len(non_zero)==0:
        return None,None
    # step 2 rank the differences
    abs_diff = [abs(d) for _, d in non_zero]
    ranks = stats.rankdata(abs_diff)

    # step 3: Sum positive and negative ranks
    pos_rank = sum(r for (_,d), r in zip(non_zero,ranks) if d >0)

    neg_rank = sum(r for (_,d), r in zip(non_zero,ranks) if d <0)

    # calculate the test statistic and two sided p value
    W = min(pos_rank,neg_rank)
    n = len(non_zero)
    mean = n*(n+1)/4
    std = (n* (n+1)*(2*n +1 )/24)**0.5

    z = (W-mean)/std
    p = 2 * stats.norm.cdf(z)

    return W,p

x = [85, 70, 90, 60, 75]
y = [80, 65, 88, 55, 70]

W, p_value = wilcoxon_test(x, y)

print("Wilcoxon Test Statistic (W):", W)
print("P-value:", p_value)