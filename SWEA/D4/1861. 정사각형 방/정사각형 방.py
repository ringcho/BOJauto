from collections import deque

def bfs(i,j):
    q = deque()
    max_cnt = 0
    q.append([i,j])
    cnt = 1
    while q:
        i, j = q.popleft()
        max_cnt = max(cnt, max_cnt)
        for di, dj in [[0,1], [1,0], [-1,0], [0,-1]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and (rooms[ni][nj]-rooms[i][j])==1:
                q.append([ni,nj])
                cnt += 1
    return max_cnt
T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 정사각형의 사이즈
    rooms = [[] for _ in range(N)]
    for i in range(N):
        rooms[i] = list(map(int, input().split()))
    res = 1
    min_room = N ** 2
    for i in range(N):
        for j in range(N):
            able = bfs(i,j)
            if res < able:
                res = able
                min_room = rooms[i][j]
                ans = [rooms[i][j], res]
            elif res == able and rooms[i][j] < min_room:
                min_room = rooms[i][j]
                ans = [rooms[i][j], res]

    print(f'#{tc}', *ans)
