N = int(input())
score = [int(input()) for _ in range(N)]

score_plus = []
score_minus = []

for i in score:
    if i > 0:
        score_plus.append(i)
    else:
        score_minus.append(i)

answer = 0

score_plus.sort()
score_minus.sort(reverse=True)

while score_plus:
    a = score_plus.pop()
    if score_plus:
        b = score_plus.pop()
        if b == 1:
            answer += a+b
        else:
            answer += a*b
    else:
        answer += a

while score_minus:
    a = score_minus.pop()
    if score_minus:
        b = score_minus.pop()
        answer += a*b
    else:
        answer += a



print(answer)
