import sys
N = int(sys.stdin.readline())
for tc in range(1, N+1):
    a, b = map(int, sys.stdin.readline().split())
    print(f'Case #{tc}: {a} + {b} = {a+b}')