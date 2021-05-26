def solution(routes):
    answer = 0
    #나가는 순으로 정렬
    routes.sort(key=lambda x: x[1])
    camera = -30001
    for route in routes:
        # 진입루트보다 카메라의 위치가 작으면 해당 루트에 카메라가 없는거니까
        # 카메라 한대를 설치! answer에 하나 더해주고
        # 카메라의 위치를 나가는 위치로 동일하게 해준다.
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
solution(routes)