from collections import deque
def solution(n, wires):
    answer = -1
    res = []
    for i in wires:
        temp = [x for x in wires]
        temp.remove(i)
        adj_list = [[] for _ in range(n+1)]
        for edge in temp:
            a, b = edge[0], edge[1]
            adj_list[a].append(b)
            adj_list[b].append(a)
        visited = []
        for i in range(n+1):
            if adj_list[i] and i not in visited:
                visited.append(i)
                q = deque([i])
                while q:
                    v = q.popleft()
                    for w in adj_list[v]:
                        if w not in visited:
                            visited.append(w)
                            q.append(w)
                res.append(abs(len(visited)-(n-len(visited))))
    answer = min(res)
    return answer