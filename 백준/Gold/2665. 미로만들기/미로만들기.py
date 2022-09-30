import heapq

def find_min_change():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    D[0][0] = 0
    while pq:
        changed, i, j = heapq.heappop(pq)

        if D[i][j] < changed:
            continue

        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = i + di
            nj = j + dj
            if 0<= ni < N and 0<= nj < N:
                if maze[ni][nj] == '1':
                    temp = 0
                else:
                    temp = 1
                new_changed = temp + changed
                if new_changed < D[ni][nj]:
                    D[ni][nj] = new_changed
                    heapq.heappush(pq, (new_changed, ni, nj))

N = int(input())
maze = [list(input()) for _ in range(N)]
D = [[N**2]*N for _ in range(N)]
find_min_change()
print(D[N-1][N-1])