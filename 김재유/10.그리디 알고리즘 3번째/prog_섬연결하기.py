
#### Union by rank 기법!!
parent = {}
rank = {}
# 초기화, 각 정점을 독립된 집합으로 생성
def make_set(i):
    parent[i] = i
    rank[i] = 0

def find(i):
    # 초기화 상태와 같지 않다면! ( 다른곳에 소속됐다면)
    if parent[i] != i:
        # 부모님 찾아보기
        parent[i] = find(parent[i])
    return parent[i]

# 두 정점 연결쓰~
def union(i, j):
    root1 = find(i)
    root2 = find(j)
    if root1 != root2:
        # 더 짧은것을 연결하는 것이 좋다
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


n = 4
costs = [[0, 1, 5], [1, 2, 3], [2, 3, 3], [1, 3, 2], [0, 3, 4]]
costs.sort(key=lambda x: x[2])

result = 0
for i in range(n):
    make_set(i)

for cost in costs:
    i, j, in_cost = cost

    if find(i) != find(j):
        union(i, j)
        result += in_cost
print(result)
