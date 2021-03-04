import sys; sys.stdin = open("input_data/1783.txt")

height, width = map(int, input().split())

if height >= 3:
    if width >= 7:
        print(width-2)
    elif 4 <= width < 7:
        print(4)
    else:
        print(width)
elif height == 2:
    if width >= 7:
        print(4)
    else:
        print((width + 1) // 2)
else:
    print(1)
