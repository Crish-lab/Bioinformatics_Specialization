'''CODE CHALLENGE: Solve the Overlap Graph Problem (restated below)
     Input: A collection Patterns of k-mers.
     Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)
Sample Input:
ATGCG
GCATG
CATGC
AGGCA
GGCAT
GGCAC
Sample Output:
CATGC -> ATGCG
GCATG -> CATGC
GGCAT -> GCATG
AGGCA -> GGCAC,GGCAT

code by: Rukhan4
'''

from collections import defaultdict

file = open("C:/Users/18687/Desktop/Bio Informatics/Bioinformatics specialization/cool_dataset.txt", mode="r")
patterns = file.read().strip().splitlines()


def Overlap(patterns):
    # Default_factory, list is created with distinct objects
    adjacency_list = defaultdict(set)
    for patt in patterns:
        adjacency_list[patt[:-1]].add(patt)
    for patt in patterns:
        suffixes = adjacency_list[patt[1:]]
        if suffixes:
            print(patt + " -> " + ",".join(suffixes))
        else:
            continue


Overlap(patterns)