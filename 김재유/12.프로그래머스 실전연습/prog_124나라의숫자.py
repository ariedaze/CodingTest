from itertools import product

def solution(n):
    my_num = [1, 2, 4]
    my_list = []
    i = 1
    sumnum = 0
    while sumnum < n:
        sumnum += 3**i
        i += 1

    for i in range(1, i):
        my_list += list(map(list, product(my_num, repeat=i)))
    return ''.join(map(str,my_list[n-1]))

print(solution(10))