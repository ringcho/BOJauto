from itertools import permutations as perm
def solution(k, dungeons):
    answer = -1
    dungeon_perm = perm(dungeons)
    for case in dungeon_perm:
        df = k
        cnt = 0
        # print(case)
        for dungeon in case:
            if df >= dungeon[0]:
                cnt += 1
                df -= dungeon[1]
            else:
                break
        answer = max(answer, cnt)
        # print(cnt)
    return answer