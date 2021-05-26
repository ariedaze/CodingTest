from pprint import pprint

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

Ground = [[0]*n for _ in range(n)]
visit = [0]*n
for cost in costs:
    Ground[cost[0]][cost[1]] = cost[2]
    Ground[cost[1]][cost[0]] = cost[2]
