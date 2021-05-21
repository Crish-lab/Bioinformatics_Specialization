'''CODE CHALLENGE: Solve the De Bruijn Graph from a String Problem.
     Input: An integer k and a string Text.
    Output: DeBruijnk(Text), in the form of an adjacency list.
Sample Input:
4
AAGATTCTCTAAGA
Sample Output:
AAG -> AGA,AGA
AGA -> GAT
ATT -> TTC
CTA -> TAA
CTC -> TCT
GAT -> ATT
TAA -> AAG
TCT -> CTA,CTC
TTC -> TCT

By: Hashim Mushtasin Reza
'''

def StringKmerCompo(sequence, kmerlenght):
    compo,i =[],0
    while i < (len(sequence)-kmerlenght+1):
        compo.append(sequence[i:i+kmerlenght])
        i+=1
    return compo

def PathGraph(text,k):
    #path pattern: [edge,[node, node]]
    pathEdge = []
    #path of successive k-mers
    pathEdge = StringKmerCompo(text,k)
    pathGraph = []
    for e in pathEdge:
        pathGraph.append([e[:-1],e[1:]])
    return pathGraph
def DeBruijnGraph(seq,k):
    path = PathGraph(seq,k)
    i = 0
    for e in path:
        for b in path[i+1:]:
            if e[0] == b[0] :
                e.append(b[1])
        i += 1
    # Just remove duplicate edges
    finalPath = []
    check = {}
    check = set(check)
    for e in path:
        check.add(e[0])
    for e in path:
        if e[0] in check:
            finalPath.append(e)
            check.remove(e[0])
    for i in finalPath:
        print(i[0],'->',','.join(i[1:]))
DeBruijnGraph('AAGATTCTCTAAGA',12)