#플로이드 - 와샬 알고리즘을 활용한다.
def solution(N, road, K):
    answer = 0
    #무한대로 집과 집사이에 걸리는 시간을 2차원 배열로 만들어준다.
    roads = [[0xfffff for _ in range(N)] for _ in range(N)]

    #걸리는 시간을 2차원 배열로 넣어준다.
    for r in road:
        if roads[r[1] - 1][r[0] - 1] > r[2]:
            roads[r[1] - 1][r[0] - 1] = r[2]
            roads[r[0] - 1][r[1] - 1] = r[2]

    for i in range(N):
        roads[i][i] = 0

    #길이 더 짧은 길이 있다면 변경해주기 위해
    for path in range(N):
        for i in range(N):
            for j in range(N):
                if roads[i][j] > roads[i][path] + roads[path][j]:
                    roads[i][j] = roads[i][path] + roads[path][j]

    #1번 집에서 걸리는 시간을 구해야하므로 roads[0]의 값들을 탐색해서 K보다 작으면 값을 한개씩 더해주면된다.
    for i in range(N):
        if roads[0][i] <= K:
            answer += 1

    return answer

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N, road, K)