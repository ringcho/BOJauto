# triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
import sys
N = int(sys.stdin.readline())
triangle = []
# N = len(triangle)
for _ in range(N):
    triangle.append(list(map(int, sys.stdin.readline().split())))
for i in range(N-2, -1, -1):
    for j in range(i+1):
        triangle[i][j] = triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1])

print(triangle[0][0])
