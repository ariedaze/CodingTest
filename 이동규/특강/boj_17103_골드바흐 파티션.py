import sys
sys.stdin = open('input/boj_17103_골드바흐 파티션.txt', 'r')

T = int(input())
inp_arr = [int(input()) for _ in range(T)]


def make_prime_arr(max_inp):
    visited = [0] * max_inp
    visited[0] = 1
    visited[1] = 1
    prime_arr = []

    for i in range(2, max_inp):
        if visited[i] == 0:
            prime_arr.append(i)
            for j in range(i + i, max_inp, i):
                visited[j] = 1
    return prime_arr, visited


prime_arr, visited = make_prime_arr(max(inp_arr) + 1)


def func(x, prime_arr, visited):
    cnt = 0
    for i in prime_arr:
        pair_i = x - i
        if pair_i < i:
            break
        if visited[pair_i] == 0:
            cnt += 1
    return cnt


for x in inp_arr:
    print(func(x, prime_arr, visited))