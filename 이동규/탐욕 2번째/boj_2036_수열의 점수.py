import sys
sys.stdin = open('input/boj_2036_수열의 점수.txt', 'r')


N = int(input())

neg, pos = [], []

result = 0

for _ in range(N):
    num = int(input())
    if num <= 0:
        neg.append(num)
    else:
        pos.append(num)

neg.sort()
pos.sort(reverse=True)

for i in range(0, len(neg), 2):
    if len(neg) == i+1:
        result += neg[i]
    else:
        result += neg[i] * neg[i + 1]

for j in range(0, len(pos), 2):
    if len(pos) == j+1:
        result += pos[j]
    else:
        if pos[j] == 1 or pos[j+1] == 1:
            result += pos[j] + pos[j+1]
        else:
            result += pos[j] * pos[j+1]

print(result)




