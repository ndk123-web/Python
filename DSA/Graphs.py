n = 8

E = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [6, 7]]

M = []

for i in range(n):
    M.append([0] * n )
    
for u,v in E:
    M[u][v]=1 
    # M[v][u]=1 (for undirected graph)


# Adjacency List
from collections import defaultdict

D = defaultdict(list)
for u,v in E:
    D[u].append(v)

print(D)

