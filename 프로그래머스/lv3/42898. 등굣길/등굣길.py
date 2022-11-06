def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]

    for puddle in puddles:
        puddle[0] -= 1
        puddle[1] -= 1
        arr[puddle[1]][puddle[0]] = -1

    arr[0][0] = 1
    for i in range(n):
        for j in range(m):
            if i + j == 0:
                continue
            elif arr[i][j] == -1:
                continue
            else:
                if arr[i-1][j] < 0 or arr[i][j-1] < 0:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
    answer = arr[n-1][m-1]
    return answer%1000000007