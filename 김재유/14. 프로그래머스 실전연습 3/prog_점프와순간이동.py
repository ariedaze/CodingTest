def solution(N):
    result = 1
    while N != 1:
        if N%2:
            N -=1
            result += 1
        else:
            N /= 2
    return result