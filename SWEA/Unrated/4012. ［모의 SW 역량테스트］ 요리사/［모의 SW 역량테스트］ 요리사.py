def nCr(n,r,ans,res,arr):
    if n == len(arr):
        if len(ans) == r:
            temp = [i for i in ans]
            res.append(temp)
        return
    ans.append(arr[n])
    nCr(n+1,r,ans,res,arr)
    ans.pop()
    nCr(n+1,r,ans,res,arr)

T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 행렬의 크기
    # 행렬을 N/2로 2개로 나누고 nCn/2
    # 각각의 값에 대해 모두 sum -> 차이를 구한 후 -> minV와 비교
    taste_arr = [[] for _ in range(N)]
    combs = []
    nums = list(range(N))
    res = []
    for i in range(N):
        taste_arr[i] = list(map(int, input().split()))
    nCr(0, N/2, [], combs, nums)
    for i in range(len(combs)//2):
        taste_a, taste_b = 0, 0
        ingredient_a = combs[i]
        ingredient_b = combs[-(i+1)]
        synergy_of_a = []
        synergy_of_b = []
        nCr(0,2,[],synergy_of_a,ingredient_a)
        nCr(0,2,[],synergy_of_b,ingredient_b)
        for i,j in synergy_of_a:
            taste_a = taste_a + taste_arr[i][j] + taste_arr[j][i]
        for i, j in synergy_of_b:
            taste_b = taste_b + taste_arr[i][j] + taste_arr[j][i]
        res.append(abs(taste_a-taste_b))
    print(f'#{tc} {min(res)}')
