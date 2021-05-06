import sys; sys.stdin = open('input_data/6603.txt')
from itertools import combinations
while True:
    try:
        data = list(map(int,input().split()))
        if len(data) == 1:
            break
        else:
            length = data[0]
            numbers = data[1:]
            for in_Data in list(combinations(numbers,6)):
                print(*sorted(in_Data))
            print()
    except:
        break