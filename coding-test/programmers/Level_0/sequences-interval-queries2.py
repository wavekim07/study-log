def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        m = -1                              # 못 찾으면 -1
        for i in range(s, e + 1):           # s부터 e까지 (e 포함)
            if arr[i] > k and (m == -1 or arr[i] < m):
                m = arr[i]                  # k보다 크면서 더 작은 값으로 갱신
        answer.append(m)
    return answer