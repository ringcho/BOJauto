def queen(i,n,arr):
    global res
    temp = [x for x in arr]
    if i == n:
        res += 1
    def is_promising(i):
        for x in range(i):
            if abs(i - x) == abs(temp[i] - temp[x]) or temp[i] == temp[x]:
                return False
        return True
    for j in range(N):
        temp.append(j)
        if is_promising(i):
            queen(i+1, n, temp)
        temp.pop()

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = []
    #[0, 1, 2, 3]
    res = 0
    queen(0, N, arr)
    print(f'#{tc} {res}')