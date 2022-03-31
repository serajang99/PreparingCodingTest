import heapq
from collections import deque


def solution(jobs):
    answer = 0
    cur = 0
    n = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: x[1]))
    heap = []
    while len(jobs) != 0 or len(heap) != 0:
        while len(jobs) != 0 and jobs[0][0] <= cur:
            heapq.heappush(heap, jobs.popleft()[::-1])

        if len(heap) == 0:
            cur = jobs[0][0]
            continue

        process = heapq.heappop(heap)
        cur += process[0]
        answer += cur - process[1]

    return answer // n
