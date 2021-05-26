def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    conn = [costs[0][0]]
    while len(conn) != n:
        for i, cost in enumerate(costs):
            if cost[0] in conn and cost[1] in conn:
                continue
            if cost[0] in conn or cost[1] in conn:
                answer += cost[2]
                conn.append(cost[0])
                conn.append(cost[1])
                conn = list(set(conn))
                costs.pop(i)
                break

    return answer