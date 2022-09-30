from collections import deque
def bfs(start, distance):
    vistied = [0]*(N+1)
    vistied[start] = 1
    q = deque()
    q.append(start)
    while q:
        i = q.popleft()
        if vistied[i] == distance + 1:
            res.append(i)
        for w in adjlist[i]:
            if not vistied[w]:
                vistied[w] = vistied[i] + 1
                q.append(w)
    return -1

N, M, K, X = map(int, input().split()) # 정점의 개수, 간선의 개수, 거리, 출발 도시 번호

adjlist= [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    adjlist[a].append(b)

res = []
ans = bfs(X,K)
res.sort()
if not res:
    print(-1)
else:
    for r in res:
        print(r)