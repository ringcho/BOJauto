from itertools import permutations as p
def is_prime(N):
    if N < 2:
        return False
    if N == 2 or N == 3:
        return True
    for i in range(2, int(N**0.5)+1):
        if N%i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    chars = ' '.join(numbers).split()
    arr = []
    N = len(chars)
    for i in range(N+1):
        perm = p(chars, i)
        for _ in perm:
            number = ''.join(_)
            if number:
                if is_prime(int(number)):
                    arr.append(int(number))
    # print(set(arr))
    # for i in range(1<<N):
    #     number = ''
    #     for j in range(N):
    #         if i & (1<<j):
    #             number += chars[j]
    #             print(number)
    return len(set(arr))