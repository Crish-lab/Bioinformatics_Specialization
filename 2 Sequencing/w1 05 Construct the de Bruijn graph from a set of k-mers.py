def Grafico(Patterns):
    n=len(Patterns)
    k=len(Patterns[0])
    Grafico=nx.MultiDiGraph()
    #PreSuf=[Patterns[0][0:-1]]
    Prefix=[]
    Suffix=[]
    for i in range(0,n):
        kmer=Patterns[i]
        Prefix.append(kmer[0:-1])
        Suffix.append(kmer[1:])
    Nodes=Prefix+Suffix
    Grafico.add_nodes_from(Nodes)
    for j in range(0,n):
        kmer=Patterns[j]
        Grafico.add_edges_from([(kmer[0:-1],kmer[1:])])
    return Grafico

Patterns=['GAGG','CAGG','GGGG','GGGA','CAGG','AGGG','GGAG']
DeBruij=Grafico(Patterns)
Adj_list=dict(DeBruij.out_degree)
print(Adj_list) # Here I get {'GAG': 1, 'CAG': 2, 'GGG': 2, 'AGG': 1, 'GGA': 1} (The correct number of outputs for each node)
Nodos=list(Adj_list.keys()) # This is a list with the nodes that have an output, which I use to iterate for Adj_list printing
for i in range(0,len(Nodos)):
    Nodo=Nodos[i]
    if Adj_list[Nodo]>0:
        print(Nodo + ' -> ' + ','.join(list(DeBruij.successors(Nodo)))) # For some reason here, even though I manage to
        # create two edges from CAG to AGG with multigraph, when getting the successors I only get one copy of AGG from CAG, I
        # dont know how to tell the program to take them both 'AGG' even though they are the same
