def l(x,y):
    return x**2 + y**2
def find_p(x):
    while x != p[x]:
        x = p[x]
    return x

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    islands_x = list(map(int, input().split()))
    islands_y = list(map(int, input().split()))
    E = float(input())
    island = [[] for _ in range(N)]
    for i in range(N):
        island[i] = [islands_x[i], islands_y[i]]
    adjlist = []
    p = [x for x in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            adjlist.append([i,j,l((island[i][0]-island[j][0]),(island[i][1]-island[j][1]))])
    adjlist.sort(key=lambda x:x[2])
    cnt, total = 0, 0
    for v, e, w in adjlist:
        if find_p(v) != find_p(e):
            cnt += 1
            total += w
            p[find_p(v)] = find_p(e)
            if cnt == N-1:
                break
    print(f'#{tc} {(total*E):.0f}')