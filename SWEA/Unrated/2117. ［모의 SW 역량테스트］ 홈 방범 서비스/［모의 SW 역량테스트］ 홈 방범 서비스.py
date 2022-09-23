def bfs(i,j,n):
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    price = n*n+(n-1)*(n-1)
    if arr[i][j] == 1:
        cnt = 1
    else:
        cnt = 0
    q = [[i,j]]
    while q:
        i, j = q.pop(0)
        if visited[i][j] == n:
            if cnt*M - price>= 0:
                return cnt
            else:
                return -1
        for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
            ni = i + di
            nj = j + dj
            if 0<= ni < N and 0<= nj < N and visited[ni][nj] == 0:
                q.append([ni,nj])
                visited[ni][nj] = visited[i][j] + 1
                if arr[ni][nj] == 1:
                    cnt += 1
    return -1
T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    res = []
    for i in range(N):
        for j in range(N):
            n = 1
            while n<=N+1:
                check = bfs(i,j,n)
                if check >= 0:
                    res.append(check)
                n += 1
    print(f'#{tc} {max(res)}')