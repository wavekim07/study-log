def solution(a, b):
    ab = str(a) + str(b)
    mul = 2 * a * b
    
    return int(ab) if int(ab) >= mul else mul