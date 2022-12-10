def solution(answers):
    cnt = [0,0,0]
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    for i, value in enumerate(answers):
        idx1 = i%5
        idx2 = i%8
        idx3 = i%10
        if pattern1[idx1] == value:
            cnt[0] += 1
        if pattern2[idx2] == value:
            cnt[1] += 1
        if pattern3[idx3] == value:
            cnt[2] += 1
    answer = []
    res = max(cnt)
    for i,count in enumerate(cnt):
        if count == res:
            answer.append(i+1)
    
    return answer