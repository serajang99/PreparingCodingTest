import heapq
from collections import deque


def solution(jobs):
    answer = 0
    cur = 0
    n = len(jobs)
    jobs = deque(sorted(jobs, key=lambda x: x[0]))
    heap = []
    while jobs or heap:
        while jobs and jobs[0][0] <= cur:
            heapq.heappush(heap, jobs.popleft()[::-1])

        if len(heap) == 0:
            cur = jobs[0][0]
            continue

        time, start = heapq.heappop(heap)
        cur += time
        answer += cur - start

    return answer // n
