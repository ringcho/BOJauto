from collections import deque
def bfs(i,j):
    visited[i][j] = 1
    q = deque()
    q.append((i,j))
    while q:
        i, j = q.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j]
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and maze[ni][nj] == '1':
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni,nj))

N, M = map(int, input().split()) #세로, 가로
maze = [list(input()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
res = bfs(0,0)
print(res)