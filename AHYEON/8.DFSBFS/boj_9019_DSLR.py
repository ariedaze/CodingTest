from collections import deque


for tc in range(int(input())):
    A, B = map(int, input().split())
    visited = [0]*10000
    answer = ''

    Q = deque([(A, '')])
    visited[A] = 1

    while Q:
        v, cmd = Q.popleft()

        if v == B:
            answer = cmd
            break

        # 1. 2*n mod 10000
        w = (2*v) % 10000
        if not visited[w]:
            visited[w] = 1
            Q.append((w, cmd+'D'))

        # 2. n-1 > 0이면 9999
        w = (v-1) % 10000
        if not visited[w]:
            visited[w] = 1
            Q.append((w, cmd+'S'))

        len_v = len(str(v))
        # 3. 왼쪽 회전
        if len_v == 4:
            w, d = divmod(v, 10**(len_v-1))
            w += (d*10)
        else:
            w = v*10
        if not visited[w]:
            visited[w] = 1
            Q.append((w, cmd+'L'))

        # 4. 오른쪽 회전
        if len_v == 1:
            w = v*1000
        else:
            w, d = divmod(v, 10)
            w += (d*1000)
        if not visited[w]:
            visited[w] = 1
            Q.append((w, cmd+'R'))

    print(answer)