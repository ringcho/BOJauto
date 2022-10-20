import sys
A, B, C = map(int, sys.stdin.readline().split())

if A == B == C:
    res = 10000 + A * 1000
elif A == B or B == C or A == C:
    if A == B or B == C:
        res = 1000 + B*100
    else:
        res = 1000 + A*100
else:
    res = max(A, B, C)*100

print(res)