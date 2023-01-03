from collections import deque

T = int(input())
for tc in range(T):
    X, Y, K = map(int, input().split())
    arr = [[0]*X for _ in range(Y)]
    cnt = 0

    for line in range(K):
        x, y = map(int, input().split())
        arr[y][x] = 1

    def bfs(y,x):
        visited = [[0]*X for _ in range(Y)]
        visited[y][x] = 1
        q = deque()
        q.append((y,x))
        while q:
            y,x = q.popleft()
            arr[y][x] = 0
            for dy, dx in [[1,0],[0,1],[-1,0],[0,-1]]:
                ny = y + dy
                nx = x + dx
                if 0<= ny < Y and 0<= nx < X and visited[ny][nx]==0 and arr[ny][nx]==1:
                    q.append((ny,nx))
                    visited[ny][nx] = 1

    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)