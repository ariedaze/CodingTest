import sys
sys.stdin = open("input.txt","r")

N, K, M = map(int,input().split()) #M번 학생이 언제 퇴장하는가?

# 원형큐로 풀려고하다가 안됨..
# 시작점
front = 0
M -= 1  # 동호의 인덱스

for i in range(1, N + 1):
    # 제거할 인덱스를 구한다. 시작점 + 탈출할 인덱스를 전체 N으로 나눠서 계산
    removed = (front + K - 1) % N
    # 제거인덱스가 M과 동일하면 출력하고 나간다.
    if removed == M:
        print(i)
        break
        #동호의 위치가 더 크면 1을 줄여서 다시계산
    if removed < M:
        M -= 1
    else:
        pass
    # 시작점을 제거한 인덱스에 할당하고 전체 길이를 하나 줄인다.
    front = removed
    N -= 1






