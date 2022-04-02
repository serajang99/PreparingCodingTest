def solution(dist):
    answer = []
    n = len(dist[0])
    line = [0, 1]
    cur = 2
    while cur < n:
        for i in range(len(line)-1):
            x1, x2 = line[i], line[i+1]
            xdist = dist[x1][x2]
            y1, y2 = dist[x1][cur], dist[x2][cur]
            # print(x1, x2, y1, y2)
            if xdist > y1:
                line = line[:i+1]+[cur]+line[i+1:]
                break
            else:
                if y1 < y2:
                    line = [cur]+line
                    break
                else:
                    # print("Test")
                    if i == len(line)-2:
                        # print("Test")
                        line = line+[cur]
                        break
                    else:
                        continue
            # print(line)
        cur += 1
    # print(line)
    if line[0] < line[-1]:
        answer.append(line)
        answer.append(line[::-1])
    else:
        answer.append(line[::-1])
        answer.append(line)
    return answer


dist = [[0, 2, 4, 3], [2, 0, 2, 1], [4, 2, 0, 1], [3, 1, 1, 0]]
print(solution(dist))
