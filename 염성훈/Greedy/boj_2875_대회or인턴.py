import sys
sys.stdin = open("input.txt","r")

N, M, K = map(int,input().split()) #N: 여학생 수, M : 남학생 수, K: 인턴쉽에 참여해야하는 학생의 수
result = 0

while N >= 2 and M >= 1 and M+N >= K+3:
    N -= 2
    M -= 1
    result += 1

print(result)

