def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    camera = -987654321

    for r in routes:
        if camera < r[0]:
            answer += 1
            camera = r[1]
    return answer