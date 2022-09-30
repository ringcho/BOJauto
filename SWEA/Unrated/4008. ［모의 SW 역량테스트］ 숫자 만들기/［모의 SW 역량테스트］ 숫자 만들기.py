operator = {
    0: '+',
    1: '-',
    2: '*',
    3: '/',
}

def perm(i):

    if i == N-1:
        temp = [x for x in p]
        arr.append(temp)

    for j in range(4):
        if used[j] != oper_count[j]:
            used[j] += 1
            p.append(operator[j])
            perm(i+1)
            used[j] -= 1
            p.pop()

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    oper_count = list(map(int, input().split()))
    num = list(map(int, input().split()))
    p = []
    arr = []
    caled = []
    used = [0] * (4)
    perm(0)
    for opers in arr:
        temp = num[0]
        for i in range(N-1):
            if opers[i] == '+':
                temp = temp + num[i+1]
            elif opers[i] == '-':
                temp = temp - num[i + 1]
            elif opers[i] == '*':
                temp = temp * num[i + 1]
            elif opers[i] == '/':
                temp = int(temp / num[i + 1])
        caled.append(temp)
    res = max(caled) - min(caled)
    print(f'#{tc} {res}')