def solution(clothes):
    answer = {}

    #입을수 있는 옷의 갯수는 종류 * 종류 이다 따라서 종류의 갯수를 저장하고
    for i in clothes:
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1

    #저장된 value에 1을 더해서 전체를 곱해주면 값을 구할 수 있다.
    cnt = 1
    for i in answer.values():
        cnt = cnt*(i+1)

    return cnt - 1
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))