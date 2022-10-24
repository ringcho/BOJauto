def perm(i,M):
    if i==M:
        print(*p)
        return
    for j in range(N):
        if not used[j]:
            if i >= 1:
                if nums[j] >= p[i-1]:
                    p[i] = nums[j]
                    perm(i+1, M)
            else:
                p[i] = nums[j]
                perm(i + 1, M)
import sys
N, M = map(int, sys.stdin.readline().split())
nums = [x for x in range(1, N+1)]
p = [0]*M
used = [0]*N
perm(0,M)