import heapq
def find_price(start, end):
    pq = []
    heapq.heappush(pq, (0, start))
    D[start] = 0
    while pq:
        price, u = heapq.heappop(pq)

        if D[u] < price:
            continue

        for v, w in adjlist[u]:
            new_price = price + w
            if D[v] > new_price:
                D[v] = new_price
                heapq.heappush(pq, (new_price,v))
                parents[v] = u
    return D[end]

N = int(input())
M = int(input())
adjlist = [[] for _ in range(N+1)]
parents = [0]*(N+1)
D = [100000*100000]*(N+1)

for i in range(M):
    s, e, w = map(int, input().split())
    adjlist[s].append((e,w))
start, end = map(int, input().split())
res = find_price(start, end)
curr = end
path = []
while curr:
    path.append(curr)
    curr = parents[curr]
print(res)
print(len(path))
print(*path[::-1])