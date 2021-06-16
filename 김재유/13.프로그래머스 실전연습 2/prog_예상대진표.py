from math import log

N = 8
A = 4
B = 7
if A > B:
    A, B = B, A
high = N
low = 1
exep = int(log(N, 2))

keep_going = True
count = 0
while keep_going:
    a_portion = [low, (high+low)//2]
    b_portion = [(high+low)//2 + 1, high]
    if a_portion[0] <= A <= a_portion[1] and b_portion[0] <= B <= b_portion[1]:
        keep_going = False
    else:
        count += 1
        if a_portion[0] <= A <= a_portion[1]:
            high = (high+low)//2
        else:
            low = (high+low)//2 + 1
print(exep-count)