def solution(n, times):
    answer = 0
    start, end = 1, max(times)*(n-1)

    while start <= end:
        mid = (start + end) // 2
        summ = 0
        for time in times:
            summ += mid//time

        if summ < n:
            start = mid+1
        else:
            answer = mid
            end = mid-1

    return answer
