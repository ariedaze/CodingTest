import sys
eq = list(sys.stdin.readline().rstrip())

minus = False
cal = '0'
# 0+50-40-25+40-125+40+50-30-20-30+40+50
# minus 변수로 -가 한번이라도 나오면 그 뒤의 모든 +는 -처리
for i in range(len(eq)):
    if eq[i] == '-':
        if not minus:
            minus = True
    elif eq[i] == '+' and minus:
        eq[i] = '-'

    # 0 중복처리
    if (cal[-1] == '-' or cal[-1] == '+') and eq[i] == '0':
        continue
    else:
        cal += eq[i]
print(eval(cal.lstrip('0')))

