'''
Hamming Distance Problem:
    Compute the Hamming distance between two strings.

    Input: Two strings of equal length.
    Output: The Hamming distance between these strings.

Sample Input:
GGGCCGTTGGT
GGACCGTTGAC
Sample Output:
3
'''

with open('dataset.txt', 'r') as file:
  p = file.readline().strip()
  q = file.readline().strip()

def HammingDistance(p, q):
  ham_dis = 0
  for i in range(0, len(p)):
    if p[i] != q[i]:
      ham_dis += 1
  return(ham_dis)
print(HammingDistance(p,q))
