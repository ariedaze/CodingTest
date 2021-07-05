# 접근을 인덱스로 접근해서 네모가 모든 같은 숫자이면 answer에 값을 더하는 방식으로 하는것이
# 효율적인 접근이다.

def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        init = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != init:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y, nn)
                    comp(x + nn, y + nn, nn)
                    return
        answer[init] += 1

    comp(0, 0, N)
    return answer

arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
solution(arr)