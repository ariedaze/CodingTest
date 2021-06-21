import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)

    while heap[0] < K:

        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        val = x + y * 2
        heapq.heappush(heap, val)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer