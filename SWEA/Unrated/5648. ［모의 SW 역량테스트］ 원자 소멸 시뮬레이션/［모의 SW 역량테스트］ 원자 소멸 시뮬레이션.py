dx = [0,0,-1,1]
dy = [1,-1,0,0]
tc = int(input())
for test in range(tc):
    N = int(input())
    arr =[list(map(int,input().split())) for _ in range(N)]
    crushed = [1] * N
    crush_time_list =[[] for _ in range(4010)]
    ans = 0 
    for i in range(N-1):
        for j in range(i+1,N):
            expect = abs(arr[i][0]-arr[j][0]) + abs(arr[i][1] -arr[j][1])
            if arr[i][0] + expect/2 * dx[arr[i][2]] == arr[j][0] + expect/2 * dx[arr[j][2]] and arr[i][1] + expect/2 * dy[arr[i][2]] == arr[j][1] + expect/2 * dy[arr[j][2]]:
                crush_time_list[expect].append(i)
                crush_time_list[expect].append(j)

    for i in range(4010):
        if crush_time_list[i]:
            temp = []
            for j in range(len(crush_time_list[i])//2):
                num1 = crush_time_list[i][2*j]
                num2 = crush_time_list[i][2*j+1]
                if crushed[num1] and crushed[num2]:
                    ans += arr[num2][3]
                    temp.append(num1)
                    temp.append(num2)
                    crushed[num2] = 0
            for num in temp:
                if crushed[num] != 0:
                    ans += arr[num][3]
                    crushed[num] = 0
    print(f'#{test+1} {ans}')
