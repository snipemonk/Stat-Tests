
# Initial Data
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]

def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)
# Step 0 output
friedman_test_verbose(t1,t2,t3)

# Step 1
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]
def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)
    data = np.array(args)
    print("\n🔹 Step 1: Combined Data Matrix (Treatments × Subjects):\n", data)

    k, n = data.shape
    print(f"\n  Number of treatments (k): {k}")
    print(f"  Number of subjects (n): {n}")

# step 1 output
friedman_test_verbose(t1,t2,t3)


# Step 2
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]


def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)

    # Step 1: Convert input into a 2D numpy array (k treatments × n subjects)
    data = np.array(args)
    print("\n🔹 Step 1: Combined Data Matrix (Treatments × Subjects):\n", data)

    if data.ndim != 2:
        raise ValueError("Input data must be 2D with equal-length lists.")

    k, n = data.shape
    print(f"\n  Number of treatments (k): {k}")
    print(f"  Number of subjects (n): {n}")

    # Step 2: Rank scores for each subject (i.e., column-wise)
    print("\n🔹 Step 2: Ranking Each Subject's Scores Across Treatments:")
    ranked_data = []
    for i, col in enumerate(data.T):
        ranked = rankdata(col)
        print(f"  Subject {i + 1} original scores: {col}, ranked: {ranked}")
        ranked_data.append(ranked)

    ranked_data = np.array(ranked_data).T
    print("\n🔹 Step 2 Output: Ranked Data Matrix:\n", ranked_data)

friedman_test_verbose(t1,t2,t3)

# Step 3
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]


def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)

    # Step 1: Convert input into a 2D numpy array (k treatments × n subjects)
    data = np.array(args)
    print("\n🔹 Step 1: Combined Data Matrix (Treatments × Subjects):\n", data)

    if data.ndim != 2:
        raise ValueError("Input data must be 2D with equal-length lists.")

    k, n = data.shape
    print(f"\n  Number of treatments (k): {k}")
    print(f"  Number of subjects (n): {n}")

    # Step 2: Rank scores for each subject (i.e., column-wise)
    print("\n🔹 Step 2: Ranking Each Subject's Scores Across Treatments:")
    ranked_data = []
    for i, col in enumerate(data.T):
        ranked = rankdata(col)
        print(f"  Subject {i + 1} original scores: {col}, ranked: {ranked}")
        ranked_data.append(ranked)

    ranked_data = np.array(ranked_data).T
    print("\n🔹 Step 2 Output: Ranked Data Matrix:\n", ranked_data)

    # Step 3: Sum the ranks for each treatment
    rank_sums = np.sum(ranked_data, axis=1)
    print("\n🔹 Step 3: Rank Sums for Each Treatment:")
    for i, s in enumerate(rank_sums, 1):
        print(f"  Treatment {i} Rank Sum: {s}")

friedman_test_verbose(t1,t2,t3)

# Step 4
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]


def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)

    # Step 1: Convert input into a 2D numpy array (k treatments × n subjects)
    data = np.array(args)
    print("\n🔹 Step 1: Combined Data Matrix (Treatments × Subjects):\n", data)

    if data.ndim != 2:
        raise ValueError("Input data must be 2D with equal-length lists.")

    k, n = data.shape
    print(f"\n  Number of treatments (k): {k}")
    print(f"  Number of subjects (n): {n}")

    # Step 2: Rank scores for each subject (i.e., column-wise)
    print("\n🔹 Step 2: Ranking Each Subject's Scores Across Treatments:")
    ranked_data = []
    for i, col in enumerate(data.T):
        ranked = rankdata(col)
        print(f"  Subject {i + 1} original scores: {col}, ranked: {ranked}")
        ranked_data.append(ranked)

    ranked_data = np.array(ranked_data).T
    print("\n🔹 Step 2 Output: Ranked Data Matrix:\n", ranked_data)

    # Step 3: Sum the ranks for each treatment
    rank_sums = np.sum(ranked_data, axis=1)
    print("\n🔹 Step 3: Rank Sums for Each Treatment:")
    for i, s in enumerate(rank_sums, 1):
        print(f"  Treatment {i} Rank Sum: {s}")

    # Step 4: Compute the Friedman test statistic
    friedman_stat = (12 / (n * k * (k + 1))) * np.sum((rank_sums - n * (k + 1) / 2) ** 2)
    print("\n🔹 Step 4: Friedman Test Statistic Calculation:")
    print(f"  Friedman Statistic: {friedman_stat:.4f}")

friedman_test_verbose(t1,t2,t3)

# step 5
t1 = [3,5,7,8,10,12]
t2 = [2,13,8,6,9,11]
t3 = [5,8,3,2,10,14]


def friedman_test_verbose(*args):
    print("\n🔹 Step 0: Original Input Lists (Each for a treatment)")
    for i, arr in enumerate(args, 1):
        print(f"  Treatment {i}:", arr)

    # Step 1: Convert input into a 2D numpy array (k treatments × n subjects)
    data = np.array(args)
    print("\n🔹 Step 1: Combined Data Matrix (Treatments × Subjects):\n", data)

    if data.ndim != 2:
        raise ValueError("Input data must be 2D with equal-length lists.")

    k, n = data.shape
    print(f"\n  Number of treatments (k): {k}")
    print(f"  Number of subjects (n): {n}")

    # Step 2: Rank scores for each subject (i.e., column-wise)
    print("\n🔹 Step 2: Ranking Each Subject's Scores Across Treatments:")
    ranked_data = []
    for i, col in enumerate(data.T):
        ranked = rankdata(col)
        print(f"  Subject {i + 1} original scores: {col}, ranked: {ranked}")
        ranked_data.append(ranked)

    ranked_data = np.array(ranked_data).T
    print("\n🔹 Step 2 Output: Ranked Data Matrix:\n", ranked_data)

    # Step 3: Sum the ranks for each treatment
    rank_sums = np.sum(ranked_data, axis=1)
    print("\n🔹 Step 3: Rank Sums for Each Treatment:")
    for i, s in enumerate(rank_sums, 1):
        print(f"  Treatment {i} Rank Sum: {s}")

    # Step 4: Compute the Friedman test statistic
    friedman_stat = (12 / (n * k * (k + 1))) * np.sum((rank_sums - n * (k + 1) / 2) ** 2)
    print("\n🔹 Step 4: Friedman Test Statistic Calculation:")
    print(f"  Friedman Statistic: {friedman_stat:.4f}")

    # Step 5: Compute the p-value
    p_value = 1 - chi2.cdf(friedman_stat, df=k - 1)
    print("\n🔹 Step 5: p-value Calculation:")
    print(f"  p-value: {p_value:.4f}")

friedman_test_verbose(t1,t2,t3)



