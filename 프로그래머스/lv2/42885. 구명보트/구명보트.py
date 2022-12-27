def solution(people, limit):
    people.sort(reverse=True)
    l = 0
    r = 1
    cnt_boat = 0
    while l <len(people)-r:
        if people[l] + people[-r] <= limit:
            cnt_boat += 1
            r += 1
            l += 1
        else:
            l += 1
    answer = len(people) - cnt_boat
    return answer