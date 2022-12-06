from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append((0,0))
    while q:
        i,j = q.popleft()
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<n and 0<=nj<m and maps[ni][nj] == 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    if visited[n-1][m-1]:
        answer = visited[n-1][m-1]
    else:
        answer = -1
    return answer