# The Mann whitney test is used to compare the differences between groups
#when the dependent variable is ordinal or continuous and there is no normal distribution

def mann_whitney_simple(group1,group2):
    #combine the groups with labels
    combined = [(x,'A') for x in group1] + [(x,'B') for x in group2]
    # Sort by value
    combined.sort(key=lambda x: x[0])

    # Assign ranks (average ranks in case of ties)
    ranks =[]
    i=0
    while i < len(combined):
        j = i
        while j < len(combined) and combined[j][0] == combined[i][0]:
            j += 1
        avg_rank = sum(range(i+1,j+1))/(j-i)
        for k in range(i,j):
            ranks.append((combined[k][1],avg_rank))
        i = j

    # Sum ranks for each group
    R1 = sum(rank for label, rank in ranks if label == 'A')
    R2 = sum(rank for label, rank in ranks if label == 'B')

    n1,n2 = len(group1),len(group2)
    U1 = R1 - n1*(n1+1)/2
    U2 = R2 - n2*(n2+1)/2

    print("U1",U1)
    print("U2", U2)
    print("U (smaller one):", min(U1, U2))

# Example use
group1 = [12, 15, 14, 10, 13]
group2 = [18, 20, 22, 19, 17, 21]

mann_whitney_simple(group1, group2)

