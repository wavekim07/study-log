def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):           # s부터 e까지 (e 포함)
            if k != 0 and i % k == 0:       # 인덱스가 k의 배수이면
                arr[i] += 1
    return arr