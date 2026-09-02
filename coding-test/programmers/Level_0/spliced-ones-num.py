def solution(num_list):
    result_1 = 1
    result_2 = 0
    
    for i in num_list :
        result_1 *= i
        result_2 += i
        
    return 1 if result_1 < result_2 ** 2 else 0