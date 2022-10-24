import sys
def perm(i, M):
    if i == M:
        print(*p)
        return
    for j in range(N):
        p[i] = arr[j]
        perm(i+1,M)
N, M = map(int, sys.stdin.readline().split())
arr = [x for x in range(1, N+1)]
p = [0]*M
used = [0]*N
perm(0, M)
