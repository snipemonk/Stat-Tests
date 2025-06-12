# this is an implementation of the Z test
# the Z test checks the mean of a normally distributed population with a known variance

def z_test(sample,popn_mean,popn_std):
    from scipy.stats import norm
    n = len(sample)
    z = (sum(sample)/n - popn_mean)/(popn_std / (n**0.5))
    p = 2*(1 - norm.cdf(abs(z)))
    return z,p
