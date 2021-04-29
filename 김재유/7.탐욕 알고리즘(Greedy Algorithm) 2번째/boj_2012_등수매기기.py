import sys; sys.stdin = open('input_data/2012.txt')

num = int(input())
num_list = [0]
for _ in range(num):
    num_list.append(int(input()))
num_list.sort()
result = 0
for i in range(1, num+1):
    result += abs(i- num_list[i])

print(result)

