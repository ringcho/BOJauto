def dfs(start):
    visited[start] = 1
    dfs_arr.append(start)
    for w in adjlist[start]:
        if not visited[w]:
            dfs(w)

def bfs(start):
    visited_bfs[start] = 1
    q = [start]
    while q:
        now = q.pop(0)
        bfs_arr.append(now)
        for w in adjlist[now]:
            if not visited_bfs[w]:
                visited_bfs[w] = 1
                q.append(w)

N, M, V = map(int, input().split())
adjlist = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)
for arr in adjlist:
    arr.sort()
dfs_arr = []
bfs_arr = []
visited = [0]*(N+1)
visited_bfs = [0]*(N+1)
dfs(V)
bfs(V)
print(*dfs_arr)
print(*bfs_arr)