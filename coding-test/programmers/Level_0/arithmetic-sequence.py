def solution(a, d, included):
    result = a
    head = a
    for i in range(len(included)) :
        head += d
        if included[i] == 1 :
            result += head
            
    return result