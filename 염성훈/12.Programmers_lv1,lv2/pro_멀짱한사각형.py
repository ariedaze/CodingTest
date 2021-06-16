#x,y의 최대공약수를 구하는 방법은 유클리드 호제법을 쓰면된다.
#두개의 값이 같아 질때 까지 해당 큰값에서 작은 값을 계속 뺴주면 최대공약수를 구할 수 있다.

def solution(w,h):
    w1 = w
    h1 = h
    while w1 != h1:
        if w1 > h1:
            w1 -= h1
        else:
            h1 -= w1
    answer = w*h - (w+h - h1)
    return answer

w = 8
h = 12
print(solution(w,h))