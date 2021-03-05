TC = int(input())

for tc in range(TC):
    N = int(input())
    # 서류, 면접
    recruits = [list(map(int, input().split())) for _ in range(N)]
    # 서류 1등부터 정렬
    recruits.sort(key=lambda x: x[0])
    cnt = 1
    # 1등의 면접점수
    interview = recruits[0][1]

    for i in range(1, N):
        # i 지원자보다 서류가 높은 애의 면접점수 비교
        if interview > recruits[i][1]:
            cnt += 1
            interview = recruits[i][1]

    print(cnt)