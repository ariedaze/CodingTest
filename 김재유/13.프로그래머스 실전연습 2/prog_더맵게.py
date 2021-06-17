import heapq
def solution(scoville, k):
    result = 0
    heapq.heapify(scoville)
    while scoville[0] < k:
        if len(scoville) == 1:
            if scoville[0] < k:
                return - 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
        result += 1

    return result