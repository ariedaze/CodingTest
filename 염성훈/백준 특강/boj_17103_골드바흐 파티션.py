import sys
sys.stdin = open("input.txt","r")

T = int(input()) # 테스트 케이스를 담고
nums = [int(input()) for _ in range(T)]
m = 1000000
prime = [False, False] + [True] * (m-1)

for i in range(2,int(m**0.5)+1):
    if prime[i]:
        for j in range(i+i,m + 1,i): #i의 배수를 찾기 위한 반복문
            if prime[j]:
                prime[j] = False

for num in nums:
    cnt = 0
    for i in range((num//2) + 1):
        # prime[i] 와 prime[num-i]를 검사하는 이유는 둘을 더한 값은 반드시 num의 값이고 둘다 소수이면 정답 값을 만족하기 떄문이다.
        if prime[i] and prime[num - i]:
            cnt += 1
    print(cnt)



