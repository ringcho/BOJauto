

def change(arr,n):
    global max_v
    if n == count:
        new = "".join(arr)
        if new > max_v:
            max_v = new
        return
    else:
        for i in range(len(arr) - 1):
            for j in range(i + 1, (len(arr))):
                arr[i], arr[j] = arr[j], arr[i]
                now = "".join(arr)
                if now not in visited[n]:
                    visited[n].append(now)
                    change(arr,n + 1)
                arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1,T+1):
    num, count = input().split()
    count = int(count)
    arr = list(num)
    max_v = '0'
    visited = [[] for _ in range(10)]
    change(arr, 0)
    print(f'#{tc} {max_v}')