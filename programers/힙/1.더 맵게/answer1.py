import heapq

def solution(scoville, K):
    i = 0
    first = 0
    second = 0
    heapq.heapify(scoville)
    
    while len(scoville) != 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second*2))
        i += 1
        if scoville[0] > K:
            return i
        
    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))