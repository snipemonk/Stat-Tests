# This is the third part in our series of implementations of the Statistical Tests using Python
# This is the Pearsons Correlation
# This test is used to check the linear relationship between 2 variables
import math


def pearson_corr(x,y):
    n = len(x)
    mean_x,mean_y = sum(x)/n,sum(y)/n

    #calculate the numerator
    numerator = sum((a - mean_x)*(b - mean_y) for a,b in zip(x,y))

    # calculate the denominator
    denominator =  math.sqrt(sum((a - mean_x)**2  for a in x)*sum((b - mean_y)**2 for b in y))

    r = numerator/denominator
    return r

