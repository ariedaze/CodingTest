import sys
sys.stdin = open('input/boj_1911_흙길 보수하기.txt', 'r')

N, L = map(int, input().split())

p = [[int(x) for x in input().split()] for i in range(N)]

p.sort()

res, s = 0, 0

for i in range(N):
    # 이전에 널빤지로 덮었던 부분이 다음 구멍난 부분에 영향을 미쳤는지 판단!
    s = max(p[i][0], s)

    diff = p[i][1] - s
    # 최소 필요한 널빤지의 갯수
    count = (diff + L - 1) // L

    res += count
    # 다음 시작하는곳은 널빤지로 덮은 곳의 마지막 지점
    s += count * L

print(res)
