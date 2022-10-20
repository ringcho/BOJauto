import sys
hour_1, min_1 = map(int, sys.stdin.readline().split())

min_2 = int(sys.stdin.readline())

temp = hour_1*60 + min_1 + min_2

while temp >= 23*60 + 59:
    temp = temp - 24*60

hour = temp//60
min = temp - hour*60
print(f'{hour} {min}')