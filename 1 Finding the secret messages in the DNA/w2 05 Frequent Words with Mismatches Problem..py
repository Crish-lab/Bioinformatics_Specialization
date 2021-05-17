'''
Code Challenge: Frequent Words with Mismatches Problem.
Sample Input:
    ACGTTGCATGTCGCATGATGCATGAGAGCT
    4 1

Sample Output:
    GATG ATGC ATGT
'''
# by: jmoggridge

def HammondD(p, q):
    if (p, q) in memo_H.keys():
        return memo_H[(p, q)]
    elif (q, p) in memo_H.keys():
        return memo_H[(q, p)]
    else:
        H = 0
        for i in range(len(p)):
            if p[i] != q[i]:
                H += 1
        memo_H[(p, q)] = H
        memo_H[(q, p)] = H
        return H
    ##


def most_freq_kmers_w_mismatches(genome, k, threshold):
    # Get a set of all kmers from the input string.
    kmers = []
    for i in range(len(genome) - k + 1):
        kmers.append(genome[i: i + k])

    # Generate all possible kmers, of len k
    import itertools
    all_kmers = [''.join(x) for x in itertools.product("ACGT", repeat=k)]

    # Initialize a dict and count how often kmer is within H <= d to a kmer from text
    counts = dict(zip(all_kmers, (0 for i in all_kmers)))
    for kmer in kmers:
        for a_kmer in all_kmers:
            if HammondD(kmer, a_kmer) <= threshold:
                counts[a_kmer] += 1

    # Get key of most frequently matched kmer
    most_freq = []
    for kmer in all_kmers:
        if counts[kmer] == max(counts.values()):
            most_freq.append(kmer)

    return most_freq


###


f = open('dataset.txt', 'r')
genome = str(f.readline().strip())
(k, threshold) = (int(i) for i in f.readline().strip().split(' '))
memo_H = {}
most_freq = most_freq_kmers_w_mismatches(genome, k, threshold)

string = ''
for f in most_freq:
    string += str(f) + ' '
print(string)