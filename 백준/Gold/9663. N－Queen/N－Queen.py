def queen(i,n,arr):
    global res
    if i == n:
        res += 1
        return
    for j in range(N):
        arr[i] = j
        for x in range(i):
            if abs(i - x) == abs(arr[i] - arr[x]) or arr[i] == arr[x]:
                break
        else:
            queen(i+1, n, arr)
        arr[i] = 0

N = int(input())
arr = [0]*N
res = 0
queen(0, N, arr)
print(res)