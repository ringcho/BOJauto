from collections import deque

N, M = map(int, input().split())
adjList = [[] for _ in range(N+1)]
cnt = 0


for _ in range(M):
    u, v = map(int, input().split())
    adjList[u].append(v)
    adjList[v].append(u)

visited = [0 for _ in range(N+1)]
def bfs(i):
    visited[i] = 1
    q = deque()
    q.append(i)
    while q:
        v = q.popleft()
        for w in adjList[v]:
            if not visited[w]:
                visited[w] = 1
                q.append(w)

for i in range(N+1):
    if not visited[i] and i != 0:
        bfs(i)
        cnt += 1
print(cnt)