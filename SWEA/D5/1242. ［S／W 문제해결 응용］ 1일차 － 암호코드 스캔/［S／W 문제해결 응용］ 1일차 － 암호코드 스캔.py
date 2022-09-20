pw_pattern = [
    [3, 2, 1, 1],
    [2, 2, 2, 1],
    [2, 1, 2, 2],
    [1, 4, 1, 1],
    [1, 1, 3, 2],
    [1, 2, 3, 1],
    [1, 1, 1, 4],
    [1, 3, 1, 2],
    [1, 2, 1, 3],
    [3, 1, 1, 2],
]
pattern = {
    '0': [0,0,0,0],
    '1': [0,0,0,1],
    '2': [0,0,1,0],
    '3': [0,0,1,1],
    '4': [0,1,0,0],
    '5': [0,1,0,1],
    '6': [0,1,1,0],
    '7': [0,1,1,1],
    '8': [1,0,0,0],
    '9': [1,0,0,1],
    'A': [1,0,1,0],
    'B': [1,0,1,1],
    'C': [1,1,0,0],
    'D': [1,1,0,1],
    'E': [1,1,1,0],
    'F': [1,1,1,1],
}
def check_pw(word):
    '''
    :param password:
    :return 0 or 함수의 값:
    password를 받아 조건에 맞는지 아닌지 확인 해주는 함수
    '''
    res, ans = int(word[-1]), int(word[-1])
    for i in range(7):
        if (i+1) % 2:
            res += 3 *int(word[i])
        else:
            res += int(word[i])
        ans += int(word[i])
    if not res%10:
        return ans
    else:
        return 0

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split()) #세로, 가로
    pw_index = [[0] for _ in range(N)]
    bit = [[] for _ in range(N)]
    password = []
    for i in range(N):
        tmp = input()
        for j in range(M):
            bit[i] += pattern[tmp[j]]
    '''
    문자열로 사용할 경우 방문처리가 어려워 배열로 다시 만듬
    '''
    pw_index = [[] for _ in range(N)]
    password = []
    cnt = 1
    ans = 0
    for i in range(N):
        for j in range(4*M-1,-1,-1):
            if bit[i][j] == 1:
                pw_index[i].append(j)
        '''
        행에서 역순으로 돌다가 1을 만나면 그 줄에 있는 1의 좌표를 모두 추가 해준다.
        '''
        cnt = 1
        cnt_i = 1
        pw_dec = ''
        if pw_index[i]:
            while True:
                patterns = [[] for _ in range(10)]
                for j in range(10):
                    for k in range(4):
                        if not k % 2:
                            for _ in range(cnt * pw_pattern[j][k]):
                                patterns[j].append(0)
                        else:
                            for _ in range(cnt * pw_pattern[j][k]):
                                patterns[j].append(1)
                '''
                patterns 는 password_pattern의 길이에 따른 변화를 나타내기 위한 배열
                '''
                temp = bit[i][pw_index[i][0]+1-cnt*7:pw_index[i][0]+1]
                '''
                가장 오른쪽 1의 좌표에서 7*cnt칸의 문자열과 패턴을 비교해서
                '''
                if temp in patterns:
                    '''
                    있다면 cnt를 더 이상 증가 시키지 않고, pw_dec 10진수로된 숫자를 반환
                    '''
                    for m in range(pw_index[i][0]+1-cnt*56, pw_index[i][0]+1, cnt*7):
                        num = []
                        for n in range(7*cnt):
                            num.append(bit[i][m+n])
                        if num in patterns:
                            pw_dec = pw_dec + str(patterns.index(num))
                    break

                else:
                    cnt += 1
                    '''
                    없다면 cnt를 증가시켜 패턴의 길이를 7, 14, 21 과 같이 계속 늘려감
                    '''
            if pw_dec:
                '''
                방문처리
                '''
                password.append(pw_dec)
                while i+cnt_i < N:
                    temp1 = bit[i][pw_index[i][0]+1-cnt*7:pw_index[i][0]+1]
                    temp2 = bit[i+cnt_i][pw_index[i][0]+1-cnt*7:pw_index[i][0]+1]
                    if temp1 != temp2:
                        break
                    else:
                        for m in range(pw_index[i][0] + 1 - cnt * 56, pw_index[i][0] + 1):
                            bit[i+cnt_i][m] = 0
                        cnt_i += 1
    for pw in password:
        ans += check_pw(pw)
    print(f'#{tc} {ans}')
