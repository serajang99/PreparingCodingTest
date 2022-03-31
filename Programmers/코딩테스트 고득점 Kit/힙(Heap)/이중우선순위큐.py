import heapq


def solution(operations):
    answer = [0, 0]
    heap = []
    for operation in operations:
        opr, num = operation.split()
        num = int(num)
        if opr == "I":
            heapq.heappush(heap, num)
        elif opr == "D":
            if heap:
                if num == -1:
                    heapq.heappop(heap)
                elif num == 1:
                    maxx = heapq.nlargest(1, heap)[0]
                    heap.remove(maxx)

    if heap:
        answer = [heapq.nlargest(1, heap)[0], heap[0]]

    return answer
