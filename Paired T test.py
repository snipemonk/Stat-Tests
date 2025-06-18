# This is the implementation of the Paired T test in python from scratch

import math
from scipy.stats import t

def paired_t_test (sample1,sample2,alpha=0.5):
    #step 1 calculate the difference between the paired samples
    differences = [x-y for x,y in zip(sample1,sample2)]
    # compute the mean of the differences
    mean_diff = sum(differences)/len(differences)
    # compute the std deviation of the differences
    n = len(differences)
    squared_diffs = [(d -mean_diff)**2 for d in differences]
    std_diff = math.sqrt(sum(squared_diffs)/(n-1))

    # compute the std error
    se = std_diff/math.sqrt(n)
    t_stat = mean_diff/se

    df = n -1
    p_value = 2*(1-t.cdf(abs(t_stat),df))

    reject_null = p_value < alpha
    return t_stat,p_value, reject_null

before = [200, 220, 250, 210, 230]
after = [195, 215, 240, 205, 225]

t_stat, p_value, reject = paired_t_test(before, after)

print(f"T-statistic: {t_stat:.3f}")
print(f"P-value: {p_value:.4f}")
print("Reject Null Hypothesis:" if reject else "Fail to Reject Null Hypothesis")