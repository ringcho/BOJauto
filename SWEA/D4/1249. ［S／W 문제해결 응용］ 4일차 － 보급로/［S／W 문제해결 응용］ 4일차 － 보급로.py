import heapq

def find_min():
    pq = []
    heapq.heappush(pq, (0, 0, 0))
    D[0][0] = 0
    while pq:
        price, i, j = heapq.heappop(pq)

        if D[i][j] < price:
            continue

        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0<= nj < N:
                new_price = price + int(arr[ni][nj])
                if new_price < D[ni][nj]:
                    D[ni][nj] = new_price
                    heapq.heappush(pq, (new_price, ni, nj))


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    D = [[9*N**2]*N for _ in range(N)]
    find_min()
    print(f'#{tc} {D[N-1][N-1]}')
