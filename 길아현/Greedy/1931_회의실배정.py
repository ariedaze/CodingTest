N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x: [x[1], x[0]])

result = 0
start = 0

for m in meetings:
    if m[0] >= start:
        start = m[1]
        result += 1

print(result)