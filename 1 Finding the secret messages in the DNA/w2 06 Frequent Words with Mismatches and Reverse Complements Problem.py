'''
Frequent Words with Mismatches and Reverse Complements Problem:
Find the most frequent k-mers (with mismatches and reverse complements) in a string.

Input: A DNA string Text as well as integers k and d.
Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc)
        over all possible k-mers.

Sample Input:
   ACGTTGCATGTCGCATGATGCATGAGAGCT
   4 1
Sample Output:
   ATGT ACAT
'''

'''
NOTE: upload your answer without comas or any other symbol, JUST TEXT, in
the same way given in the Sample Output
'''

def frequentWordsWithMismatchesAndReverseComplements(s,k,d):
    counts = {}
    for i in range(len(s)-k+1):
        for sub in [s[i:i+k],reverseComplement(s[i:i+k])]:
            for neighbor in neighbors(sub,d):
                if neighbor not in counts:
                    counts[neighbor] = 0
                counts[neighbor] += 1
    m = max(counts.values())
    return [kmer for kmer in counts if counts[kmer] == m]

def neighbors( s, d ):
    if d == 0:
        return [s]
    if len(s) == 1:
        return ['A','C','G','T']
    out = []
    for neighbor in neighbors(s[1:],d):
        if hamming(s[1:],neighbor) < d:
            out.extend(['A'+neighbor,'C'+neighbor,'G'+neighbor,'T'+neighbor])
        else:
            out.append(s[0] + neighbor)
    return out

def hamming( s, t ):
    return sum([s[i] != t[i] for i in range(len(s))])

def reverseComplement( s ):
    return ''.join([complement(s[i]) for i in range(len(s)-1,-1,-1)])

def complement( s ):
    return {'A':'T','T':'A','C':'G','G':'C'}[s]

s = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4
d = 1
print(frequentWordsWithMismatchesAndReverseComplements(s,k,d))