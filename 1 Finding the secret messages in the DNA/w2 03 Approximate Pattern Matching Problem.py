'''
Approximate Pattern Matching Problem:
     Find all approximate occurrences of a pattern in a string.

    Input: Strings Pattern and Text along with an integer d.
    Output: All starting positions where Pattern appears as a substring of
    Text with at most d mismatches.

Sample Input:
ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
3
Sample Output:
6 7 26 27
'''

with open('dataset.txt', 'r') as file:
    Pattern = file.readline().strip()
    Text = file.readline().strip()
    d = int(file.readline().strip())


def HammingDistance(p, q):
    ham_dis = 0
    for i in range(0, len(q)):
        if p[i] != q[i]:
            ham_dis += 1
    return (ham_dis)


def AppPattMach(p, t, d):  # pattern, text, number of mismatch
    ind = []
    for j in range(len(t) - len(p) + 1):
        # print(t[j:(j+len(p))], p)
        if HammingDistance(t[j:(j + len(p))], p) <= d:
            ind.append(str(j))
            # print(ind)
    return (ind)


a = ' '.join(AppPattMach(Pattern, Text, d))

with open('dataset.txt', 'w') as output:
    output.write(a)