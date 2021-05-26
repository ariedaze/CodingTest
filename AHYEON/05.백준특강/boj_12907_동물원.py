N = int(input())
animals = map(int, input().split())

check = [0] * 41
total = 2

for a in animals:
    check[a] += 1

result = True
for cnt in check:
    if cnt > total:
        result = False
        break
    total = cnt

if result:
    print(2 ** (check.count(2) + (1 if 1 in check else 0)))
else:
    print(0)