import sys; sys.stdin = open('input_data/4796.txt')

t = 0
while True:
    can, total, vacation = map(int, input().split())
    if vacation == 0:
        break
    t += 1
    result = vacation//total*can + min(vacation%total, can)
    print("Case {}: {}".format(t, result))