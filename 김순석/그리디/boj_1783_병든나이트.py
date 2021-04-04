N, M = map(int, input().split())
if N == 1 or M == 1:
    move = 0

elif N <= 2 and M <= 2:
    move = 0

elif N == 2 and M < 5:
    move = 1
elif N == 2 and M < 7:
    move = 2
elif N == 2 and M >= 7:
    move = 3


elif N >= 3:
    if M <= 2:
        move = 1
    elif M <= 3:
        move = 2
    elif M <= 6:
        move = 3
    elif M <= 7:
        move = 4
    else:
        move = M - 7 + 4

print(move + 1)
