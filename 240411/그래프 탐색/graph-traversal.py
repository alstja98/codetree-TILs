import sys

def dfs(start, graph, visited):
    count = 1
    
    for target in graph[start]:
        if visited[target] == 0:
            visited[target] = 1
            count += dfs(target, graph, visited)

    return count

N,M = map(int, sys.stdin.readline().split())

edge_list = []
for _ in range(M):
    node1, node2 = map(int, sys.stdin.readline().split())
    edge_list.append((node1, node2))

graph = [ [] for _ in range(N+1) ]
for node1, node2 in edge_list:
    graph[node1].append(node2)
    graph[node2].append(node1)

visited = [ 0 for _ in range(N+1)]
visited[1] = 1

answer = dfs(1, graph, visited)

print(answer-1)