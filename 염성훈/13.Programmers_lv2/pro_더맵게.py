import heapq

def solution(scoville, K):
    answer = 0
    #heapify 함수를 힙으로 만들어준다. -> 완전이진트리로 만들어준다는 것
    #처음에는 sort()를 사용했지만 효율성검사에서 통과하지 못한다.
    #heapify를 사용하면 배열에서 첫번째 값이 노드의 최솟값을 갖게된다.0인덱스가
    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) > 1:
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
            answer += 1
        else :
            return -1

    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))