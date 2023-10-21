def solution(clothes):
    answer = 1
    clothes_dict = {}
    for clothes_name, clothes_kind in clothes:
        if clothes_kind in clothes_dict:
            clothes_dict[clothes_kind].append(clothes_name)
        else:
            clothes_dict[clothes_kind] = [clothes_name]
    
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key])+1)
        
    return answer-1