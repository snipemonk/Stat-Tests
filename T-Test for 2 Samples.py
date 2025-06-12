# This is an implementation of the T-Test for 2 samples
# This test checks whether the difference between the means of 2 independent populations is equal to the target value

def t_test(x1,x2):
    from scipy.stats import t
    n1,n2 = len(x1),len(x2)
    m1,m2 = sum(x1)/n1, sum(x2)/n2
    s1 = sum((i-m1)**2 for i in x1)/ (n1-1)
    s2 =   sum((i-m2)**2 for i in x2) / (n2-1)
    se = ((s1/n1)+(s2/n2))**0.5
    t_stat = (m1-m2)/se
    df = min(n1-1,n2-1)
    p = 2*(1-t.cdf(abs(t_stat),df))
    return t_stat,p