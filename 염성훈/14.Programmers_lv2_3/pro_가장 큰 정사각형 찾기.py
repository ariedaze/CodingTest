# 완전 탐색으로 풀 경우에 2차원 배열을 전부 탐색해애햔다.
# 작은 정사각형을 하나씩 값을 쌓아가면서 해를 구하면 되기 때문에
# dp를 사용해야한다.

def solution(board):
    n = len(board) # 세로의 길이
    m = len(board[0]) # 가로의 길이

    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]
    # 2중 포문으로 연산
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j - 1]) + 1

    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)

    return answer ** 2

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
solution(board)