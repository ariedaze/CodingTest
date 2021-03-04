import sys; sys.stdin = open('input_data/13458.txt')

classroom = int(input())
students = list(map(int, input().split()))
chief, sous = map(int, input().split())
total = classroom
for student in students:
    student -= chief
    if student > 0:
        total += student//sous
        student -= student//sous * sous
        if student:
            total += 1
print(total)