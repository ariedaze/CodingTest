import sys
sys.stdin = open("input.txt","r")

N = int(input())
numbers = list(map(int,input().split()))
numbers.sort(reverse=False)

result = 0
ans = 0
for number in numbers:
    result += number
    ans += result

print(ans)