def solution(x):
    div = 0
    for i in range(len(str(x))):
        div += int(str(x)[i])
    if x%div == 0:
        return True
    return False