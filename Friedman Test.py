import numpy as np
from scipy.stats import rankdata, chi2


def friedman_test(*args):
    data = np.array(args)

    if data.ndim != 2:
        raise ValueError("All treatment lists must be the same length.")

    k, n = data.shape  # k = number of treatments, n = number of subjects

    # Rank each column (subject-wise ranking across treatments)
    ranked_data = np.array([rankdata(subject_scores) for subject_scores in data.T]).T

    # Sum ranks for each treatment
    rank_sums = np.sum(ranked_data, axis=1)

    # Compute Friedman statistic
    friedman_stat = (12 / (n * k * (k + 1))) * np.sum((rank_sums - n * (k + 1) / 2) ** 2)

    # Compute p-value
    p_value = 1 - chi2.cdf(friedman_stat, df=k - 1)

    return friedman_stat, p_value

t1 = [8, 6, 7, 9, 10]
t2 = [6, 5, 7, 8, 8]
t3 = [7, 4, 6, 8, 9]

# Run test
statistic, p_val = friedman_test(t1, t2, t3)

# Print results
print("Friedman Test Statistic:", round(statistic, 2))
print("p-value:", round(p_val, 4))