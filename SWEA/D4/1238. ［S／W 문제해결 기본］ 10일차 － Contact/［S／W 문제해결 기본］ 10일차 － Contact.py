from collections import deque
def bfs(n):
    vistied[n] = 1
    q = deque()
    q.append(n)
    while q:
        v = q.popleft()
        for w in adj_list[v]:
            if vistied[w] == 0:
                q.append(w)
                vistied[w] = vistied[v] + 1

for tc in range(1,11):
    N, start = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_list = [[] for _ in range(101)]
    vistied = [0] * 101
    for i in range(N//2):
        f, t = edges[2*i], edges[2*i + 1]
        if t in adj_list[f]:
            pass
        else:
            adj_list[f].append(t)
    bfs(start)
    maxV = 0
    ans = 0
    for i in range(100, 0, -1):
        if maxV < vistied[i]:
            maxV = vistied[i]
            ans = i
    print(f'#{tc} {ans}')
