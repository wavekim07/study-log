def solution(num_list):
    last = num_list[-1]
    second_last = num_list[-2]
    
    if last > second_last :
        num_list.append(last - second_last)
    else :
        num_list.append(last * 2)
        
    return num_list