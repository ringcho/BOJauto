def find_max_pro(i, pro):
    global max_v
    if i == N:
        if pro > max_v:
            max_v = pro
        return
    elif pro < max_v:
        return
    else:
        for x in range(N):
            if x not in used and probability[i][x] != 0:
                used.append(x)
                temp = pro*probability[i][x]/100
                find_max_pro(i+1, temp)
                used.pop()


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    probability = [list(map(int, input().split())) for _ in range(N)]
    max_v = 100
    for i in range(N):
        max_v = max_v * min(probability[i])/100
    used = []
    find_max_pro(0,100)
    print(f'#{tc} {max_v:.6f}')