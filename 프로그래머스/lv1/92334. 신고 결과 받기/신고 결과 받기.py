def solution(id_list, report, k):
    dict_report = {}
    count_report = {}
    banned = []
    answer = [0]*len(id_list)
    for atob in report:
        a, b = atob.split()
        if id_list.index(a) not in dict_report:
            dict_report[id_list.index(a)] = [b]
        else:
            if b not in dict_report[id_list.index(a)]:
                dict_report[id_list.index(a)].append(b)
                
    for user in dict_report:
        for reported in dict_report[user]:
            if reported not in count_report:
                count_report[reported] = 1
            else:
                count_report[reported] += 1

    for user in count_report:
        if count_report[user] >= k:
            banned.append(user)
    for user in dict_report:
        for reported in dict_report[user]:
            if reported in banned:
                answer[user] += 1
    return answer