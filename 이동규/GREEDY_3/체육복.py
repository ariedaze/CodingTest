# import sys
# sys.stdin = open('input/체육복.txt', 'r')

def solution(n, lost, reserve):
    lost = sorted(lost)
    reserve = sorted(reserve)
    check = [True for _ in range(n)]
    check2 = [True for _ in range(n)]

    for i in lost: # 잃어버린 친구들
        check[i-1] = False

    for i in lost:
        for j in reserve:
            if i == j:
                check[i-1] = True
                check2[i-1] = False

    for i in lost:
        for j in reserve:
            if check[i-1] == False and check2[j-1] == True and (i == j - 1 or i == j + 1):
                if i == j - 1:
                    check2[j - 1] = False
                else:
                    check2[j + 1] = False
                check[i-1] = True

    return check.count(True)