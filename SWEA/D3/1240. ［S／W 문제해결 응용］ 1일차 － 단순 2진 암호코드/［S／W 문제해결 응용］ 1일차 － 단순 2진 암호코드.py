def check_password(number):
    number = str(number)
    res = 0
    ans = 0
    for i, num in enumerate(number):
        if (i+1) % 2:
            res += 3*int(num)
        else:
            res += int(num)
        ans += int(num)
    if res % 10:
        return 0
    else:
        return ans

T =  int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split()) # 배열의 세로,가로
    arr = [0]*N
    password = ''
    pattern = [
        '0001101',
        '0011001',
        '0010011',
        '0111101',
        '0100011',
        '0110001',
        '0101111',
        '0111011',
        '0110111',
        '0001011',
    ]
    for i in range(N):
        arr[i] = input()
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                for k in range(8):
                    temp = arr[i][j-7*(k+1)+1:j-7*k+1]
                    password = str(pattern.index(temp)) + password
            if password:
                break
        if password:
            break
    print(f'#{tc} {check_password(password)}')
