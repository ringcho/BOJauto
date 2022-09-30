def dfs(s):
    visited[s] = 1
    for w in adj_list[s]:
        if not visited[w]:
            dfs(w)

V = int(input())
E = int(input())
adj_list = [[] for _ in range(V+1)]
visited = [0]*(V+1)
for _ in range(E):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
dfs(1)
res = visited.count(1)
print(res-1)