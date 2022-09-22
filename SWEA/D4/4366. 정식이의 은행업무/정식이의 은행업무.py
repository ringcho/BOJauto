def dectotr(i):
    i = int(i)
    res = ''
    while i>0:
        res = str(i%3) + res
        i = i//3
    return res

def one_diff_in_string(string1, string2):
    cnt = 0
    if len(string1) != len(string2):
        return False
    else:
        for x in range(len(string1)):
            if string1[x] != string2[x]:
                cnt += 1
            if cnt > 1:
                return False
    if cnt == 1:
        return True

T = int(input())

for tc in range(1,T+1):
    bit2 = list(input())
    bit3 = input()
    len3 = len(bit3)
    len2 = len(bit2)
    i = 1
    while i < len(bit2):
        if bit2[i] == '0':
            bit2[i] = '1'
        elif bit2[i] == '1':
            bit2[i] = '0'
        new = int(''.join(bit2), 2)
        bit2_to_bit3 = dectotr(new)
        if one_diff_in_string(bit2_to_bit3,bit3):
            print(f'#{tc} {new}')
            break
        if bit2[i] == '0':
            bit2[i] = '1'
        elif bit2[i] == '1':
            bit2[i] = '0'
        i += 1