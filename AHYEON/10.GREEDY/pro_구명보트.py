def solution(people, limit):
    people.sort()
    cnt = 0

    slim = 0
    fat = len(people) - 1

    while slim <= fat:
        cnt += 1
        if people[slim]+people[fat] <= limit:
            slim += 1
        fat -= 1

    return cnt