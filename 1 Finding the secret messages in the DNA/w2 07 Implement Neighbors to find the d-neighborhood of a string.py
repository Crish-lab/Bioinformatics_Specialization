'''
Code Challenge: Implement Neighbors to find the d-neighborhood of a string.

Input: A string Pattern and an integer d.
Output: The collection of strings Neighbors(Pattern, d). (You may return the
strings in any order, but each line should contain only one string.)

Sample Input:
  ACG
  1
Sample Output:
  CCG TCG GCG AAG ATG AGG ACA ACC ACT ACG

'''

def HammingDistance(p, q):
    ham_dis = 0
    for i in range(0, len(q)):
        if p[i] != q[i]:
            ham_dis += 1
    return (ham_dis)


def Suffix(Pattern):
    return (Pattern[1::])


def Neighbors(Pattern, d):
    if d == 0:
        return (Pattern)
    if len(Pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    Neighborhood = []
    SuffixNeighbors = Neighbors(Suffix(Pattern), d)
    for Text in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), Text) < d:
            for x in ['A', 'T', 'G', 'C']:
                Neighborhood.append(x + Text)
        else:
            Neighborhood.append(Pattern[0] + Text)
    return (Neighborhood)

#Input
with open('dataset.txt', 'r') as file:
    Pattern = file.readline().strip()
    d = int(file.readline().strip())

a = ' '.join(Neighbors(Pattern, d))

#Output
with open('dataset.txt', 'w') as output:
    output.write(a)