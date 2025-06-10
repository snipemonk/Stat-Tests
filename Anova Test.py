# This is the implementation in Python of the Anova Test
# The Anova test is used if 3 or more groups have the same mean

def one_way_anova(*groups,alpha=0.05):
    k = len(groups)
    N = sum(len(g) for g in groups) # total no. of observations

    #step 1
    grand_mean = sum(sum(g) for g in groups) /N
    # step 2: Between group variance (SSB)
    ssb  = sum(len(g)* (sum(g)/len(g) - grand_mean)**2 for g in groups)
    #step 3
    ssw = sum(sum((x - sum(g)/len(g))**2 for x in g)for g in groups)
    # step 4
    dfb = k-1
    dfw = N-k

    #step 5
    msb = ssb/dfb
    msw = ssw/dfw
    #step 6
    f_stat = msb/msw

    #step 7
    from scipy.stats import f as f_dist
    p_value = 1-f_dist.cdf(f_stat,dfb,dfw)

    reject_null = p_value < alpha
    return f_stat,p_value,reject_null



