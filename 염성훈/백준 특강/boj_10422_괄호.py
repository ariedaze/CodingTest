import sys
sys.stdin = open("input.txt")

#카탈란 수 알고리즘 : 괄호가 나오면 반드시 괄호가 나와야하는 알고리즘이다.
#이거는 특정 경우의 수에만 사용되는 거라 괄호 쌍을 갖는 문제에만 적용시킬 수 있음.
from math import factorial

#num에는 쌍을 이루는 문자 길이의 절반을 넣어주면된다.
def catalan(num):
    return factorial(2 * num) // (factorial(num) * factorial(num + 1))

T = int(input())
for t in range(1,T+1):
    n = int(input())
    #괄호는 무조건 짝이 있어야하므로 짝수가 아니면 그냥 넘긴다.
    if n % 2 != 0:
        print(0)
        continue

    print(catalan(n//2) % 1000000007)