from itertools import product
def solution(word):
    candi = ['A','E','I','O','U']
    arr1 = candi[:]
    # li1 = ["AAAAE", "AAAE", "EIO"]
    for i in range(2, 6):
        temp = product(candi, repeat=i)
        for _ in temp:
            arr1.append(''.join(_))
    # arr2 = product(candi, repeat=2)
    # for _ in arr2:
    #     candi.append(''.join(_))
    arr1.sort()
    # print(arr1)
    answer = arr1.index(word) + 1
    return answer
