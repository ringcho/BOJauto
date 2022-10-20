import sys
total = int(sys.stdin.readline())
N = int(sys.stdin.readline())
res = 0
for _ in range(N):
    fee, times = map(int, sys.stdin.readline().split())
    res += fee * times

if total == res:
    print('Yes')
else:
    print('No')