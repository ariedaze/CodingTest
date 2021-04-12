import sys
sys.stdin = open("input.txt","r")

S = list(input())
T = list(input())

flag = True

while T:
    # 끝이 A이면 뺸다.
    if T[-1] == 'A':
        T.pop()
    # 끝이 B이면 뺴주고 반전시켜준다.
    elif T[-1] == 'B':
        T.pop()
        T.reverse()
    if S == T:
        flag = False

if flag:
    print(0)
else :
    print(1)


