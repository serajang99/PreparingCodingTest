import heapq


def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        # print(scoville)
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+b*2)
        answer += 1
        # print(scoville, answer)

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))
