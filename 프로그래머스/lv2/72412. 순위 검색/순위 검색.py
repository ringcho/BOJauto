from itertools import product
import bisect
def solution(info, query):
    N = len(info)
    M = len(query)
    answer = [0]*M
    candi = {}
    for i in range(N):
        temp = info[i].split()
        key_candi = [(temp[0],'-'),(temp[1],'-'),(temp[2],'-'),(temp[3],'-')]
        keys = product(*key_candi)
        for key in keys:
            if key not in candi:
                candi[key] = [int(temp[4])]
            else:
                candi[key].append(int(temp[4]))
    for value in candi.values():
        value.sort()
        
    for j in range(M):
        query[j] = query[j].replace('and', "")
        condition, price = tuple(query[j].split()[:4]), int(query[j].split()[4])
        if condition in candi:
            res = len(candi[condition])-bisect.bisect_left(candi[condition], price)
            # print(candi[condition],price)
            answer[j] = res
    # print(answer)
    return answer