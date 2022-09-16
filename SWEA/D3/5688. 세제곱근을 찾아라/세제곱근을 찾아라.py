T = int(input())
for tc in range(1,T+1):
    N = int(input())
    r = round(N**(1/3))
    if r**3 == N:
        print(f'#{tc} {r}')
    else:
        print(f'#{tc} {-1}')

