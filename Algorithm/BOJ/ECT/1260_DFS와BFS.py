import sys
from collections import defaultdict

N, M, V = map(int, sys.stdin.readline().strip().split())

graph = defaultdict(list)
for _ in range(M):
    node_a, node_b = map(int, sys.stdin.readline().strip().split())
    graph[node_a].append(node_b)

print(graph)