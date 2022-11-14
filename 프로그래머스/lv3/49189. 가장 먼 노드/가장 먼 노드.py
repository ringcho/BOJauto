from collections import deque
def solution(n, edge):
    adjList = [[] for _ in range(n+1)]
    for line in edge:
        a, b = line[0], line[1]
        adjList[a].append(b)
        adjList[b].append(a)
    visited = [0 for _ in range(n+1)]
    q = deque()
    q.append(1)
    visited[1] = 1
    print(q,visited)
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                q.append(w)
    max_distance = max(visited)
    answer = visited.count(max_distance)
    return answer