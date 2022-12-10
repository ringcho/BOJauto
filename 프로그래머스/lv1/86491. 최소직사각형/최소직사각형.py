def solution(sizes):
    w, h = 0, 0
    for card in sizes:
        if card[0] > card[1]:
            w = max(w, card[0])
            h = max(h, card[1])
        else:
            w = max(w, card[1])
            h = max(h, card[0])
        
    answer = w * h
    return answer