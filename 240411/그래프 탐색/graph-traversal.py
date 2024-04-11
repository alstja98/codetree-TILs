import sys

N,M = map(int, sys.stdin.readline().split())

edge_list = []
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    edge_list.append((node1, node2))

graph = [ [] for _ in range(N+1) ]
for node1, node2 in edge_list:
    graph[node1].append(node2)
    graph[node2].append(node1)

print(len(graph[1]))