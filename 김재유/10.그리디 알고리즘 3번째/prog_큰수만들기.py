
number = '999'
k = 2
now = 0
first_max = number.index(max(number))
if first_max < k:
    number = number[first_max:]
    k -= first_max
while k:
    if now + 1 >= len(number) : break
    if number[now] < number[now+1]:
        number = number[:now] + number[now+1:]
        k -= 1
        if now:
            now -= 1
        continue
    else:
        now += 1
while k :
    min_num = number.index(min(number))
    number = number[:min_num] + number[min_num+1:]
    k -= 1
print(number)
