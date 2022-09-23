def earning(honey_1_2):
    global C, max_v
    res = 0
    for honeys in honey_1_2:
        if sum(honeys)>C:
            honey_max = []
            for i in range(1<<M):
                temp = 0
                x = 0
                for j in range(M):
                    if i & (1<<j):
                        temp += honeys[j]
                        if temp > C:
                            honey_max.append(x)
                        else:
                            x += honeys[j]**2
                honey_max.append(x)
            res += max(honey_max)
        else:
            for value in honeys:
                res += value ** 2
    if max_v < res:
        max_v = res
        return

T=int(input())

for tc in range(1,T+1):
    N, M, C = map(int,input().split())      #꿀통의 크기, 채취할 수 있는 크기, 한번에 가져갈 수 있는양
    arr = [list(map(int,input().split())) for _ in range(N)]
    '''
    어떻게 선택하지???
    i 쓰고, 남은 범위가 M보다 작으면 무조건 다음 i
    아니면 남은 범위에서 M 확인
    for 문으로 continue ?
    '''
    honeys = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            honeys[i].append(arr[i][j:j+M])

    max_v = 0
    for i in range(N-1):
        for j in range(i+1,N):
            for m in honeys[i]:
                for n in honeys[j]:
                    honey_total = [m, n]
                    earning(honey_total)

    print(f'#{tc} {max_v}')
