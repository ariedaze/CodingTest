T = int(input())
testcases = [int(input()) for _ in range(T)]
max_num = max(testcases)

prime = [1] * (max_num+1)
prime[0], prime[1] = 0, 0
for i in range(2, int(max_num**0.5)+1):
    if prime[i]:
        for j in range(i*2, max_num+1, i):
            if prime[j]:
                prime[j] = 0


for tc in testcases:
    cnt = 0
    for t in range((tc//2)+1):
        if prime[t] and prime[tc-t]:
            cnt += 1
    print(cnt)