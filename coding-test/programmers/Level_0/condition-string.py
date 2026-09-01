def solution(ineq, eq, n, m):
    if eq == '=' and n == m :
        return 1
    return 1 if (ineq == '<' and n < m) or (ineq == '>' and n > m) else 0