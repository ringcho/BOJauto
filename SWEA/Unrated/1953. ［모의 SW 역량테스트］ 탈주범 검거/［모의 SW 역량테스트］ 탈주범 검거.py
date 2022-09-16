from collections import deque

def bfs(i, j):
    visited[i][j] = 1
    q = deque()
    q.append([i,j])
    while q:
        i, j = q.popleft()
        for di,dj in tunnel[str(maze[i][j])]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and maze[ni][nj]!=0:
                for dy,dx in tunnel[str(maze[ni][nj])]:
                    y = ni + dy
                    x = nj + dx
                    if 0<=y<N and 0<=x<M and visited[y][x]:
                        if y == i and x == j:
                            visited[ni][nj] = visited[i][j] + 1
                            q.append([ni,nj])

T = int(input())

for tc in range(1,T+1):
    N, M, R, C, L = map(int, input().split()) # 세로, 가로, 뚜껑세로, 뚜껑가로, 탈출 후 소요된 시간
    maze = [[] for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        maze[i] = list(map(int, input().split()))
    tunnel = {
        '1':[[1,0],[0,1],[-1,0],[0,-1]],
        '2':[[1,0],[-1,0]],
        '3':[[0,1],[0,-1]],
        '4':[[-1,0],[0,1]],
        '5':[[1,0],[0,1]],
        '6':[[1,0],[0,-1]],
        '7':[[-1,0],[0,-1]]
    }
    bfs(R,C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] <= L and visited[i][j] != 0:
                cnt += 1
    print(f'#{tc} {cnt}')
