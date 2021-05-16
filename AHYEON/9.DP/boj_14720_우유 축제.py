n = int(input())
store = list(map(int, input().split()))

count = 0
for i in range(n):
    if store[i] == count % 3:
        count = count + 1

print(count)
