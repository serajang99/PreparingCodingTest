def solution(citations):
    answer = 0
    citations = sorted(citations)
    lenc = len(citations)
    for i in range(lenc):
        h = citations[i]
        if lenc-i >= h and i <= h:
            answer = h
        else:
            for j in range(answer+1, h):
                if lenc-i >= j and i <= j:
                    answer = j
            break
    return answer