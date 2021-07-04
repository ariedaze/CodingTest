def solution(N, road, K):
    Ground = [[0]*(N+1) for _ in range(N+1)]
    distance = [500001]*(N+1)
    for way in road:
        if Ground[way[0]][way[1]]:
            if Ground[way[0]][way[1]] > way[2]:
                Ground[way[0]][way[1]] = way[2]
                Ground[way[1]][way[0]] = way[2]
        else:
            Ground[way[0]][way[1]] = way[2]
            Ground[way[1]][way[0]] = way[2]
    print(Ground)
    Q = [1]
    distance[1] = 0
    while Q:
        now = Q.pop(0)
        for i in range(N+1):
            if Ground[now][i] and Ground[now][i] + distance[now] < distance[i]:
                distance[i] = Ground[now][i] + distance[now]
                Q.append(i)

    return len([i for i in distance if i <= K])