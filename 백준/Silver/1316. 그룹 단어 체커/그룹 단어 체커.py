import sys
N = int(sys.stdin.readline())
res = 0
for _ in range(N):
    string = sys.stdin.readline().strip()
    arr = []
    for i,char in enumerate(string):
        if char not in arr:
            arr.append(char)
        elif char in arr and arr[-1] == char:
            pass
        elif char in arr and arr[-1] != char:
            break
        if i == len(string)-1:
            res += 1

print(res)