'''SOLVE THE EULERIAN CYCLE PROBLEM
     Input: The adjacency list of an Eulerian directed graph.
     Output: An Eulerian cycle in this graph.

Sample Input:
0 -> 3
1 -> 0
2 -> 1,6
3 -> 2
4 -> 2
5 -> 4
6 -> 5,8
7 -> 9
8 -> 7
9 -> 6
Sample Output:
6->8->7->9->6->5->4->2->1->0->3->2->6
'''
import sys

sys.setrecursionlimit(10 ** 6)

"""Eularian path/circuit dfs"""


def dfs(v, graph, circuit, stack):
    if len(graph[v]) == 0:
        circuit.append(v)
        if len(stack) == 0:
            return
        else:
            dfs(stack.pop(), graph, circuit, stack)
    else:
        stack.append(v)
        dfs(graph[v].pop(0), graph, circuit, stack)
    ###


f = open('cool_dataset.txt', 'r')
lines = list(str(l.strip('\n')) for l in f.readlines())

Edges = [[i.strip(' ') for i in line.split('->')] for line in lines]

Adj = {}
for edge in Edges:
    Adj[int(edge[0])] = [int(i) for i in edge[1].split(',')]
del ((Edges, lines, f))

i = 0
stack = []
circuit = []

dfs(i, Adj, circuit, stack)
circuit.reverse()
string = '->'.join(str(i) for i in circuit)
# print('\n\n\n',string)

with open('cool_dataset.txt', 'w') as wr:
    wr.write(string)
    wr.close()