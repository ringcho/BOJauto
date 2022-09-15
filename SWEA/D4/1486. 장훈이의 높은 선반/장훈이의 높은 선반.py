T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split()) # 점원 수 , 탁상의 높이
    workers = list(map(int, input().split()))
    minH = sum(workers)
    for i in range(1<<N):
        height = 0
        for j in range(N):
            if i & (1<<j):
                height += workers[j]
        if height >= B and height < minH:
            minH = height
    print(f'#{tc} {minH-B}')
