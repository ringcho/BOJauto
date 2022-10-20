import sys
arr = [0, 0]
for i in range(2):
   arr[i] = int(sys.stdin.readline())

a = arr[1] % 10
b = (arr[1] % 100 - a) // 10
c = arr[1] // 100
print(arr[0]*a)
print(arr[0]*b)
print(arr[0]*c)
print(arr[0]*arr[1])