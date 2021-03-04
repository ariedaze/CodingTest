N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = N

for a in A:
    student = a - B
    if student > 0:
        result += student // C # 몫
        if student % C: # 나머지가 있다면
            result += 1

print(result)
