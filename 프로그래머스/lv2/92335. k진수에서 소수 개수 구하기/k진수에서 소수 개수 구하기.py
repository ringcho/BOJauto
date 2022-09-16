def solution(n, k):
    answer = 0
    
    def check_prime(N):
        if N == 1:
            return False

        for i in range(2, round(N**(1/2))+1):
            if N % i == 0:
                return False
                break
        return True

    change_k = ''
    while n > 0:
        change_k = str(n%k) + change_k
        n = n//k
    arr = change_k.split('0')
    nums = []
    for num in arr:
        if num.isdigit():
            nums.append(int(num))
    for num in nums:
        if check_prime(num):
            answer += 1
    return answer