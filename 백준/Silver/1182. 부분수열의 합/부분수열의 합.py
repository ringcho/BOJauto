def find_s(i, S, total):
    global cnt
    if i == N:
        if total == S:
            if 1 in used:
                cnt += 1
        return
    else:
        used[i] = 1
        find_s(i+1, S, total+nums[i])
        used[i] = 0
        find_s(i+1, S, total)



N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
used = [0]*N
find_s(0, S, 0)
print(cnt)