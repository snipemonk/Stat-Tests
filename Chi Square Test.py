# This is the second part in our series of Implementation of statistical tests in Python
# This is the Chi Square Test
# The purpose of this test is to check if the observed frequencies match the expected frequencies

from scipy.stats import chi2

def chi_square_test(observed,expected,alpha=0.5):
    chi_stat= sum((o-e)**2/e for o,e in zip(observed,expected))

    #calculate the degrees of freedom
    df = len(observed)-1

    #calculate the P-value
    p_value = 1-chi2.cdf(chi_stat,df)

    reject_null = p_value < alpha
    return p_value,reject_null,chi_stat


