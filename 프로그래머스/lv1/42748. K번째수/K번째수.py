def solution(a, c):
    answer = []
    new = []
    for i in c:
        new = sorted(a[(i[0]-1):i[1]])
        answer += [new[i[2]-1]]
    return answer