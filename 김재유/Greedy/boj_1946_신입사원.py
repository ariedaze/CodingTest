# 시간초과 ㅠ.ㅠ

import sys; sys.stdin = open('input_data/1946.txt')

for t in range(int(input())):
    employee_num = int(input())
    employees = []
    can_hire = [1] * employee_num
    for i in range(employee_num):
        employees.append(list(map(int, input().split())))
    employees.sort()
    for i in range(employee_num):
        now = employees[i]
        for j in range(i+1, employee_num):
            next_employee = employees[j]
            if now[0] < next_employee[0] and now[1] < next_employee[1]:
                can_hire[j] = 0
        if now[1] == 1:
            break
    print(sum(can_hire))




