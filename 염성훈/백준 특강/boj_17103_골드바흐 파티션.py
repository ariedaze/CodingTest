import sys
sys.stdin = open("input.txt","r")
from itertools import combinations

# 에라토스테네스의 체를 활용한다. 모르겠다.

def prime_list(n):
    sieve = [True] * n

    # n의 최대 약수는 제곱근 이하이다.
    m = int(n ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True: # i가 소수이면
            for j in range(i+i, n, i): # i이후 i의 배수들을 False판정한다.
                sieve[j] = False
    #소수 목록을 산출한다.
    return [i for i in range(1,n) if sieve[i] == True]

# 메모리초과가 난다.
T = int(input())

for t in range(1,T + 1):
    cnt = 0
    target = int(input())
    prime_numbers = prime_list(target)
    c_list = list(combinations(prime_numbers,2))

    for item in c_list:
        if sum(item) == target:
            cnt += 1

    print(cnt)

