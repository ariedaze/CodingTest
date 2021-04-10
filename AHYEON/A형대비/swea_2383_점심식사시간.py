def calc(stair_list, stair):
    pass

def dfs(idx):
    pass

for tc in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    peoples, stairs = [], []
    num, ans = 0, 987654321 # 사람수, 리턴시간
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                num += 1
                peoples.append([i, j])
            elif room[i][j] == 2:
                stairs.append([i, j])

    # 계단까지 거리 계산
    for i in range(num):
        d1 = abs(peoples[i][0]-stairs[0][0]) + abs(peoples[i][1]-stairs[0][1])
        d2 = abs(peoples[i][0]-stairs[1][0]) + abs(peoples[i][1]-stairs[1][1])
        peoples[i][0] = d1
        peoples[i][1] = d2
    visit_stair = [0]*num
    dfs(0)
    print('#{}'.format(tc))
