def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 0
    camera_position = -30001
    for start, end in routes:
        if camera_position < start:
            camera_position = end
            answer += 1
        
    return answer