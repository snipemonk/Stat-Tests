# This is an implementation of the Mcnemars Test using Python from scratch

import math
from scipy.stats import  chi2

def mcnemars_test(y_true,pred1,pred2,alpha=0.05):
    b=0
    c=0

    for yt,p1,p2 in zip(y_true,pred1,pred2):
        if p1 == yt and p2 != yt:
            b +=1
        elif p1 != yt and p2 == yt:
            c +=1

    if b + c ==0:
        print(" No disagreement between classifiers. Test not applicable")
        return None,None,None

    test_stat = ((abs(b-c)-1)**2)/(b+c)
    p_value = 1 - chi2.cdf(test_stat,df=1)
    significant = p_value < alpha

    return test_stat,p_value,significant


# True labels
y_true = [1, 0, 1, 1, 0, 1, 0, 0]

# Predictions from Classifier A and B
pred_a = [1, 0, 1, 1, 0, 0, 1, 0]
pred_b = [1, 1, 1, 0, 0, 1, 0, 0]

# Run test
stat, p, sig = mcnemars_test(y_true, pred_a, pred_b)

print("Chi-Square Statistic:", stat)
print("P-value:", p)
print("Is the difference significant?", sig)