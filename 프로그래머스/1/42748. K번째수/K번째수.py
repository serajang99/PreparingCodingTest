def solution(array, commands):
    answer = []
    for i, j, k in commands:
        new_arr = array[i-1:j]
        new_arr = sorted(new_arr)
        answer.append(new_arr[k-1])
        
    return answer