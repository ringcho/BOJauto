import sys
num = int(sys.stdin.readline())
cnt = 1
temp = (num//10 + num%10)%10 + num%10*10

while num != temp:
    cnt += 1
    temp = (temp//10 + temp%10)%10 + temp%10*10
print(cnt)