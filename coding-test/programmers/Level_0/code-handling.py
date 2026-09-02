def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)) :
        if code[i] == "1" :
            mode = 1 - mode
        else :
            if mode == 0 and i % 2 == 0 :
                ret += code[i]
            elif mode == 1 and i % 2 != 0 :
                ret += code[i]
            
    return 'EMPTY' if ret == '' else ret
    