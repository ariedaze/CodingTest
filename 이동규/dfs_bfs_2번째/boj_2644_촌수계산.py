import sys
sys.stdin = open('input/boj_2644_촌수계산.txt', 'r')

def bfs():
    queue = []
    queue.append(I - 1)
    V[I - 1] = 1

    while queue:
        node = queue.pop(0)

        for i in range(N):
            if M[node][i] == 1 and V[i] == 0:
                V[i] = V[node] + 1
                queue.append(i)
                if i == Y - 1:
                    return V[i] - 1

    return -1

N = int(input()) # Node의 수
I, Y = list(map(int, input().split())) # I, You 사이의 촌수를 계산 할 것임
E = int(input()) # Edge의 수
M = [[0 for _ in range(N)] for _ in range(N)] # Matix
V = [0 for _ in range(N)] # Visit

for _ in range(E):
    f, t = list(map(int, input().split()))
    M[f-1][t-1] = 1
    M[t-1][f-1] = 1

print(bfs())