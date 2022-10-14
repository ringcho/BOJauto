import copy

T = int(input())

def find(cnt, connect, length, arr):
    global max_core, ans
    if cnt == len(cores_cord):
        if connect > max_core:
            max_core = connect
            ans = length
        elif connect == max_core:
            ans = min(length, ans)
        return
    elif max_core > connect + len(cores_cord) - cnt:
        return
    i, j = cores_cord[cnt]
    for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
        darr = copy.deepcopy(arr)
        ni = i + di
        nj = j + dj
        moves = 0
        while 0 <= ni < N and 0 <= nj < N:
            if darr[ni][nj] == 1:
                moves = 0
                break
            else:
                darr[ni][nj] = 1
                moves += 1
                ni = ni + di
                nj = nj + dj
        if moves == 0:
            continue
        else:
            find(cnt+1, connect+1, length+moves, darr)
    find(cnt+1, connect, length, arr)

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cores_cord = []

    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] == 1:
              cores_cord.append((i, j))

    max_core, ans = 0, 0

    find(0, 0, 0, arr)

    print(f'#{tc} {ans}')
