import sys; sys.stdin = open('input_data/1931.txt')


meeting_num = int(input())
ending_table = []
for _ in range(meeting_num):
    time = list(map(int, input().split()))
    ending_table.append(time[::-1])

ending_table.sort()
ending = ending_table[0][0]
ending_table.pop(0)
result = 1
for meeting in ending_table:
    if ending <= meeting[1]:
        result += 1
        ending = meeting[0]
print(result)
