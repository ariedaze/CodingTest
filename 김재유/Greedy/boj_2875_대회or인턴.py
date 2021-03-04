import sys; sys.stdin = open("input_data/2875.txt")

girl, boy, intern = map(int, input().split())
if girl >= boy * 2:
    max_team = boy
else:
    max_team = girl//2
residue = girl + boy - max_team * 3
while residue < intern:
    max_team -= 1
    residue += 3
print(max_team)