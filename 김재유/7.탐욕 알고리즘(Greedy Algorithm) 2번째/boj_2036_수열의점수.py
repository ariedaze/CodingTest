import sys; sys.stdin = open('input_data/2036.txt')
size = int(input())
plus_list = []
minus_list = []
zero = 0
result = 0
for _ in range(size):
    num = int(input())
    if num > 0:
        if num == 1:
            result += 1
        else:
            plus_list.append(num)
    elif num == 0:
        zero += 1
    else:
        minus_list.append(-num)
plus_list.sort()
minus_list.sort()

if len(plus_list)%2:
    result += plus_list.pop(0)
for i in range(len(plus_list)//2):
    result += plus_list[i*2]*plus_list[i*2+1]


if len(minus_list)%2:
    residue = minus_list.pop(0)
    if not zero:
        result -= residue



for i in range(len(minus_list)//2):
    result += minus_list[i*2]*minus_list[i*2+1]

print(result)