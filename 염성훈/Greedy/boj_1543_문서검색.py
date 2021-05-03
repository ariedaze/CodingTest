import sys
sys.stdin = open("input.txt","r")

source = input()
search = input()

count = 0
i = 0

# source문자열이 찾는 문자열의 길이보다 커지면 안됨
while len(source) - i >= len(search):
    if source[i:i+len(search)] == search:
        count += 1
        i += len(search)
    else:
        i += 1

print(count)
