'''
Find the reverse complement of a DNA string.

Input: A DNA string Pattern.
Output: Patternrc , the reverse complement of Pattern.

Sample Input:
AAAACCCGGT
Sample Output:
ACCGGGTTTT

by: Subha M
'''

def rev_comp(strand):
    rev_strand=str()
    for _ in strand:
        if _=='A':
            rev_strand+='T'
        elif _=='G':
            rev_strand+='C'
        elif _=='C':
            rev_strand+='G'
        elif _=='T':
            rev_strand+='A'
    return(rev_strand[::-1])
f = open(r'dataset.txt')
strand=f.read()
complement=rev_comp(strand)
print(complement)