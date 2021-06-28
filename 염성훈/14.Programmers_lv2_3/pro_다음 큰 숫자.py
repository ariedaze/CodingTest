def solution(n):

    #이진법으로 바꾸고 1의 갯수를 샌다.
    c = bin(n).count('1')

    #n이후 값들에서 가장 먼저 1의 count값과 같은 값이 나오면 m을 리턴한다.
    for m in range(n + 1 , 1000001):
        if bin(m).count('1') == c:
            return m

n = 78
print(solution(n))