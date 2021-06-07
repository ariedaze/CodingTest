import sys; sys.stdin = open('input_data/10451.txt')
sys.setrecursionlimit(100000)

def find_circle(x, friends):
    if dots[x] in friends:
        friends.append(x)
        for friend in friends:
            circle[friend] = 1
        return
    friends.append(x)
    find_circle(dots[x], friends)

for t in range(int(input())):
    N = int(input())
    dots = [0] + list(map(int, sys.stdin.readline().split()))
    result = 0
    circle = [0]*(N+1)
    for i in range(1, N+1):
        if not circle[i]:
            result += 1
            find_circle(i, [])
    print(result)