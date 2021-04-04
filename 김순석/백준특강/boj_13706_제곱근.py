import sys
ln = sys.stdin.readline

N = int(ln())

def b_search(start, end):
    target = end
    while True:
        mid = (start + end) // 2
        if mid ** 2 == target:
            return mid

        if mid ** 2 > target:
            end = mid

        elif mid ** 2 < target:
            start = mid


print(b_search(0, N))