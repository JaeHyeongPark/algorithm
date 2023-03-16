# n: 4~10000
import sys
# import math

# def eratosthenes(n : int):
#     prime_list = [True for i in range(n+1)] # 0 ~ 10000 까지 미리 소수 리스트 만들기
#     prime_list[0] = False
#     prime_list[1] = False

#     for j in range(2, int(math.sqrt(n))+1):
#         i=2
#         while j*i <= n:
#             prime_list[j*i] = False
#             i += 1
#     return prime_list

# prime_list = eratosthenes(10000)

# T = int(sys.stdin.readline()) #test case

# for i in range(T):
#     test_num = int(sys.stdin.readline())
#     small = 0
#     big = 0
#     for j in range(2, int(test_num/2)+1):
#         if j == 2 or j % 2 == 1:
#             if prime_list[j] and prime_list[test_num-j]:
#                 small = j
#                 big = test_num-j
#     print(small, big)

#다른 사람 풀이

def is_prime(n:int):
    if n==1:
        return False
    for i in range(2, int(n**(0.5)) + 1):
        if n%i==0:
            return False
    return True

T = int(sys.stdin.readline()) #test case

for _ in range(T):
    test_num = int(sys.stdin.readline())
    a, b = int(test_num/2),int(test_num/2)

    while a > 1:
        if is_prime(a) and is_prime(b):
            print(a, b)
        else:
            a -= 1
            b += 1
