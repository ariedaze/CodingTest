def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) #Kruskal 알고리즘을 사용해서 네트워크의 정점을 최소 비용으로 연결해야한다.
    connect = [costs[0][0]] #가장 cost가 작은 노드(섬)을 넣어준다.
    #노드들을 하나씩 확인하고 이미 두 노드가 connect리스트에 존재하면 다음 노드로 넘어간다.
    while len(connect) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connect) and (cost[1] in connect):
                continue
            if (cost[0] in connect) or (cost[1] in connect):
                answer += cost[2]
                connect.append(cost[0])
                connect.append(cost[1])
                # 중복되는 것을 방지하기 위해서 아래와 같이 처리한다. set으로 집합처리를 한다.
                connect = list(set(connect))
                # 처리된 비용은 리스트에서 제거한다.
                costs.pop(i)
                break

    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n, costs))