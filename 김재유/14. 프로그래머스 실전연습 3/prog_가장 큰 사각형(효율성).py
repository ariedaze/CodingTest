def solution(board):
    height , width = len(board), len(board[0])
    for line in board :
        if 1 in line:
            result = 1
            break
    else:
        return 0
    for i in range(1, height):
        for j in range(1, width):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                if board[i][j] > result:
                    result = board[i][j]
    return result**2