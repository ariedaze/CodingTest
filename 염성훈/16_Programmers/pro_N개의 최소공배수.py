from math import gcd

def solution(arr):
    answer = arr[0]

    for num in arr:
        # 먼저 answer에 num을 곱해 최소 공배수를 구하고 구한 최소 공배수를 다시한번 구해준다.
        # 이떄 최소 공배수는 두수의 곱과 최대공약수의 나눔으로 구할 수 있다.
        answer = answer * num // gcd(answer, num)

    return answer