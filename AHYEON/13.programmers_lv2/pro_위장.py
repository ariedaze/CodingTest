def solution(clothes):
    answer = 1
    categories = {}
    for _, category in clothes:
        if category in categories:
            categories[category] += 1
        else:
            categories[category] = 1

    for i in categories.values():
        answer *= i + 1

    # 안입는 경우 제외
    return answer - 1