base = [1,1,2,2,2,8]
given = list(map(int, input().split()))
res = []
for i in range(6):
    res.append(base[i]-given[i])
print(*res)