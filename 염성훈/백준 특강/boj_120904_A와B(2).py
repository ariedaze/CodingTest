import sys
sys.stdin = open("input.txt","r")

def perm(k, n, source, target):
    global flag
    if k == n:
        if source == target:
            flag = False
            return
        else:
            return
    else:
        source.append("A")
        perm(k+1, n, source, target)
        source.pop()
        source.reverse()
        source.append("B")
        perm(k+1, n, source, target)
        source.pop()
        source.reverse()

S = list(input())
T = list(input())
n = len(T) - 1
flag = True

perm(0, n, S, T)

if flag:
    print(0)
else:
    print(1)