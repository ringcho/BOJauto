def find_p(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x,y):
    p[find_p(y)] = p[find_p(x)]

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    p = [x for x in range(N+1)]
    adjlist = [list(map(int, input().split())) for _ in range(M)]
    for x, y in adjlist:
        union(x,y)
    for i in range(1,N+1):
        p[i] = find_p(p[i])
    p.pop(0)
    print(f'#{tc} {len(set(p))}')