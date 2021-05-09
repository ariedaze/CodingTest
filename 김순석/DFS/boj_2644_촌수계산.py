N = int(input())  # 사람 수
s, e = map(int, input().split())  # 구해야하는 촌 수
E = int(input())  # 간선 수

# P[a] = b : a의 부모 b
P = [0] * (N + 1)
s_lst = []
e_lst = []
cnt = 0
for _ in range(E):
    # 부모, 자식
    x, y = map(int, input().split())
    P[y] += x
if P[s] == e or P[e] == s:
    print(1)
    exit()
if s == e:
    print(0)
    exit()

while P[s] != 0:
    s = P[s]
    s_lst.append(s)

while P[e] != 0:
    e = P[e]
    e_lst.append(e)

for node in s_lst:
    if node in e_lst:
        cnt += e_lst.index(node) + 1
        cnt += s_lst.index(node) + 1
        print(cnt)
        exit()
else:
    if s in e_lst:
        cnt += e_lst.index(s) + 1
        print(cnt)
    elif e in s_lst:
        cnt += s_lst.index(e) + 1
        print(cnt)
    else:
        print(-1)