import sys
def han(N):
    global cnt
    if N <= 99:
        cnt += 1
        return
    flag = 0
    diff = (N//10)%10 - N%10
    N = N//10
    while N > 9:
        temp = (N//10)%10 - N%10
        N = N//10
        if diff == temp:
            flag = 1
        else:
            flag = 0
            break
    if flag:
        cnt += 1
        return 'good'
N = int(sys.stdin.readline())

cnt = 0

for i in range(1,N+1):
    han(i)
print(cnt)
