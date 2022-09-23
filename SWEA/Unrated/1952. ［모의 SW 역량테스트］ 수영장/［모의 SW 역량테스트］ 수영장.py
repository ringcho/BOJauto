T = int(input())

# def dfs(i,n,ans,arr):
#     global min_v
#     temp = [x for x in arr]
#     if i >= n:
#         if ans < min_v:
#             min_v = ans
#     else:
#         fee_3 = sum(temp[i-2:i+1])
#         if fee_3 > month_3:
#             for j in range(3):
#                 if used[i-j] == 1:
#                     return
#                 else:
#                     used[i-j] = 1
#                     temp[i] = month_3
#                     temp[i-1], temp[i-2] = 0, 0
#                     ans_1 = sum(temp)
#                     dfs(i+1,n,ans_1,temp)
#                     used[i-j] = 0
#                     temp = [x for x in arr]
#                     dfs(i+1,n,ans,temp)

for tc in range(1,T+1):
    day, month, month_3, year = map(int, input().split()) #일일 이용권, 한달 이용권, 3달 이용권, 년간
    sc = list(map(int, input().split()))
    min_v = year
    month_3_fee = 12*3000
    res = [0 for _ in range(12)]
    for i,days in enumerate(sc):
        day_fee = res[i-1] + day * days
        month_fee = month + res[i-1]
        if i>=2:
            month_3_fee = month_3 + res[i-3]
        res[i] = min([day_fee,month_fee,month_3_fee])

    min_v = min(res[-1],min_v)
    print(f'#{tc} {min_v}')
