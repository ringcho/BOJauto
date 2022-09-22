T = int(input())

def find_string(i,j,str):
    if len(str) == 7:
        if str not in candi:
            candi.append(str)
    else:
        if 0<=i-1<N:
            find_string(i-1,j,str+arr[i-1][j])
        if 0<=i+1<N:
            find_string(i + 1, j, str + arr[i + 1][j])
        if 0<=j + 1<N:
            find_string(i,j+1,str+arr[i][j+1])
        if 0<=j - 1<N:
            find_string(i, j-1, str + arr[i][j-1])


for tc in range(1,T+1):
    N = 4
    arr = [input().split() for _ in range(4)]
    candi = []
    for i in range(N):
        for j in range(N):
            find_string(i,j,arr[i][j])
    print(f'#{tc} {len(candi)}')