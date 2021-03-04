N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

ans = rope[-1] * N
idx = 0
while idx < N - 1:
    if rope[idx] != rope[idx+1]:
        if ans < rope[idx] * (idx + 1):
            ans = rope[idx] * (idx + 1)
    idx += 1

print(ans)
