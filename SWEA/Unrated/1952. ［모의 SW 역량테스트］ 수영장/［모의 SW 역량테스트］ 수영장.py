T = int(input())

def dfs(i):
    global min_v
    if i >= 12:
        min_v = min(min_v, sum(res))
        return
    else:
        if sc[i]:
            res[i] = day * sc[i]
            dfs(i+1)
            res[i] = 0

            res[i] = month
            dfs(i+1)
            res[i] = 0

            res[i] = month_3
            dfs(i+3)
            res[i] = 0
        else:
            dfs(i+1)


for tc in range(1, T + 1):
    day, month, month_3, year = map(int, input().split())  # 일일 이용권, 한달 이용권, 3달 이용권, 년간
    sc = list(map(int, input().split()))
    min_v = year
    month_3_fee = 12 * 3000
    res = [0 for _ in range(12)]
    dfs(0)
    print(f'#{tc} {min_v}')
    
    # DP
    for i,days in enumerate(sc):
        day_fee = res[i-1] + day * days
        month_fee = month + res[i-1]
        if i>=2:
            month_3_fee = month_3 + res[i-3]
        res[i] = min([day_fee,month_fee,month_3_fee])

    min_v = min(res[-1],min_v)
    print(f'#{tc} {min_v}')
