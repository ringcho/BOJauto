import sys
import heapq

def dijstra(start):
    dp = [float('inf') for _ in range(n+1)]
    heap = []
    dp[start] = 0
    heapq.heappush(heap, [0, start])
    
    while heap:
        wei, cp = heapq.heappop(heap)
        for cp_n in graph[cp]:
            wei_cp, cp_cp = cp_n[0], cp_n[1]
            check_wei = wei + wei_cp
            if check_wei < dp[cp_cp]:
                dp[cp_cp] = check_wei
                heapq.heappush(heap, [dp[cp_cp], cp_cp])

    return dp

def min_distance(start, cp1, cp2, dt):
    distance1 = distance_dic[start][cp1] + distance_dic[cp1][cp2] + distance_dic[cp2][dt]
    distance2 = distance_dic[start][cp2] + distance_dic[cp2][cp1] + distance_dic[cp1][dt]
    return min(distance1, distance2)

T = int(input())
# T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, input().split()) # n: 교차로 수(정점) / m: 도로 수(간선) / t: 목적지 후보의 개수
    # n, m, t = map(int, sys.stdin.readline().split()) # n: 교차로 수(정점) / m: 도로 수(간선) / t: 목적지 후보의 개수
    s, g, h = map(int, input().split()) # s: 출발지점 / g, h : 반드시 지나야하는 경로 
    # s, g, h = map(int, sys.stdin.readline().split()) # s: 출발지점 / g, h : 반드시 지나야하는 경로 
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split()) # a, b : 서로 이어진 정점(양방향) / d : 간선의 가중치
        # a, b, d = map(int, sys.stdin.readline().split()) # a, b : 서로 이어진 정점(양방향) / d : 간선의 가중치
        graph[a].append([d, b])
        graph[b].append([d, a])

    distance_dic = dict()
    ans = []
    distance_dic[s] = dijstra(s)
    distance_dic[g] = dijstra(g)
    distance_dic[h] = dijstra(h)
    for _ in range(t):
        dt = int(input())
        # dt = int(sys.stdin.readline())
        distance_dic[dt] = dijstra(dt)
        if min_distance(s, g, h, dt) == distance_dic[s][dt] and distance_dic[s][dt] != float('inf'):
            ans.append(dt)
    ans.sort()
    print(*ans)