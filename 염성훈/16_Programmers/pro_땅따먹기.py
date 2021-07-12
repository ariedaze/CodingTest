def solution(land):
    answer = 0
    N = len(land) # 행의 갯수
    for i in range(0, N - 1):
        # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
        # N-1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다
        # 기존에 있는 값에 위의 해당열을 제외한 값에 +를 더해주는게 핵심이다.
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])
    answer = max(land[N - 1])  # 마지막 행의 최댓값을 구해주면 답이 된다.
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
solution(land)
