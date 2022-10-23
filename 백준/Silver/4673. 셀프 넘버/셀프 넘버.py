def d(N):
    temp = N
    while N > 0:
        temp += N%10
        N = N//10
    return temp
arr = []
for i in range(1,10000):
    f = d(i)
    arr.append(f)
for i in range(1,10001):
    if i not in arr:
        print(i)