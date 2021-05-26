N, M = map(int, input().split())

# 1. 2칸 위, 1칸 오른쪽
# 2. 1칸 위, 2칸 오른쪽
# 3. 1칸 아래, 2칸 오른쪽
# 4. 2칸 아래, 1칸 오른쪽

if N == 1:
    answer = 1
elif N == 2: # 위 아래로 한 칸씩 이동 가능 > 최대 3번 이동 & 가로로 이동 가능한 경
    answer = min(4, (M-1)//2+1)
elif M < 7:
    answer = min(4, M)
else:
    answer = (2 + (M-5)) + 1 # 2,3 이동 + 2,3이동으로 인한 5칸 제외 + 처음 있던

print(answer)
