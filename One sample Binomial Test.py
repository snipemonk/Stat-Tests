# This test is used to check whether the proportion of "success" in a sample differs
# from a hypothesized population proportion
from scipy.stats import binom_test

def one_sample_binomial_test(successes, n_trials, p_null):
    # Perform the binomial test
    p_value = binom_test(x=successes, n=n_trials, p=p_null, alternative='greater')
    return p_value

# Example usage
successes = 8
n_trials = 10
p_null = 0.5

p_val = one_sample_binomial_test(successes, n_trials, p_null)
print(f"P-value: {p_val:.4f}")