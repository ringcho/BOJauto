from heapq import heappop, heappush

def dijkstra(arr, start):
    heap = []
    heappush(heap,(0, start))
    arr[start] = 0
    while heap:
        distance, i = heappop(heap)
        if arr[i] < distance:
            continue
        for w in adjlist[i]:
            n_distance = w[1]
            if n_distance + distance < arr[w[0]]:
                arr[w[0]] = n_distance + distance
                heappush(heap,(n_distance + distance,w[0]))


T = int(input())

for tc in range(1,T+1):
    V, E, goal = map(int, input().split())
    adjlist = [[]*(V+1) for _ in range(V+1)]
    D = [1000000]*(V+1)
    for i in range(E):
        fr, to, w = map(int, input().split())
        adjlist[fr].append((to, w))
    # goal 에서 다른정점으로 거리 모두 구하고 -> dijkstra 시작점 goal해서 D[]에 저장 되어있음
    # 다른정점에서 goal거리 모두 구하고
    # 두개 더해서 가장큰거
    dijkstra(D, goal)
    max_v = 0
    for i in range(1, V+1):
        new_D = [1000000] * (V + 1)
        if i == goal:
            pass
        else:
            dijkstra(new_D, i)
            if D[i] + new_D[goal] > max_v:
                max_v = D[i] + new_D[goal]
    print(f'#{tc} {max_v}')