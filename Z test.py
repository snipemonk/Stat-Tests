# this is an implementation of the Z test
# the Z test checks the mean of a normally distributed population with a known variance

def z_test(sample,popn_mean,popn_std):
    from scipy.stats import norm
    n = len(sample)
    z = (sum(sample)/n - popn_mean)/(popn_std / (n**0.5))
    p = 2*(1 - norm.cdf(abs(z)))
    return z,p

sample  = [102,98,100,97,103]
popn_mean = 100
popn_std = 2

z,p = z_test(sample,popn_mean,popn_std)
print("Z-score",z)
print("p-value",p)
