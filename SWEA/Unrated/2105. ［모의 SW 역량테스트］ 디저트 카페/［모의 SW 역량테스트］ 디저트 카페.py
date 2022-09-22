def dfs (y,x,res,pre_pattern):
    global max_v,i,j
    if pre_pattern == (-1,1) and y == i and x == j:
        if max_v < len(res):
            max_v = len(res)
    else:
        for di, dj in pattern[pre_pattern]:
            ni = y + di
            nj = x + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and (arr[ni][nj] not in res):
                visited[ni][nj] == 1
                tmp = arr[ni][nj]
                res.append(tmp)
                dfs(ni,nj,res,(di,dj))
                visited[ni][nj] == 0
                res.pop()

T = int(input())

for tc in range(1,T+1):
    pattern = {
        (1, 1): [[1, 1], [1, -1]],
        (1, -1): [[1, -1], [-1, -1]],
        (-1, -1): [[-1, -1], [-1, 1]],
        (-1, 1): [[-1, 1]],
    }
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_v = -1
    stack = []
    for i in range(N):
        for j in range(N):
            res = []
            temp = dfs(i,j,res,(1,1))
    print(f'#{tc} {max_v}')
    