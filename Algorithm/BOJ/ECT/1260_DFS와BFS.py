import sys
from collections import defaultdict

N, M, V = map(int, sys.stdin.readline().strip().split())

graph = defaultdict(set)
for _ in range(M):
    node_a, node_b = map(int, sys.stdin.readline().strip().split())
    graph[node_a].add(node_b)
    graph[node_b].add(node_a)

def dfs_recusive(graph, start, visited=[]):
    visited.append(start)
    for node in graph[start]:
        if node not in visited:
            dfs_recusive(graph, node, visited)
    return visited

result = map(str, dfs_recusive(graph, V))
print(' '.join(result))

def bfs(graph, start):
    tovisit, visited  = [], []
    tovisit.append(start)
    while tovisit:
        node = tovisit[0]
        del tovisit[0]
        if node not in visited:
            visited.append(node)
            tovisit.extend(graph[node])
    return visited

result = map(str, bfs(graph, V))
print(' '.join(result))