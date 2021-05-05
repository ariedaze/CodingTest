import sys
sys.stdin = open('input/boj_1543_문서 검색.txt', 'r')

T = list(input())
P = list(input())

count = 0

while T:
    flag = 0
    for i in P:
        if not T or T.pop(0) != i:
            flag = 0
            break
        else:
            flag = 1
    if flag:
        count += 1

print(count)


# print(T.count(P))
#

