#TODO 파트7 시간초과

import sys;
from collections import deque
sys.stdin = open('input_data/1202.txt')
store_num, bag_num = map(int, input().split())
store_info = [list(map(int, sys.stdin.readline().split())) for _ in range(store_num)]
bag_info = [int(sys.stdin.readline()) for _ in range(bag_num)]
store_info.sort(key=lambda x: (-x[1], x[0]))
bag_info.sort()
result = 0
while bag_info:
    bag = bag_info.pop(0)
    for idx, store in enumerate(store_info):
        if bag >= store[0]:
            result += store[1]
            store_info.pop(idx)
            break
print(result)


