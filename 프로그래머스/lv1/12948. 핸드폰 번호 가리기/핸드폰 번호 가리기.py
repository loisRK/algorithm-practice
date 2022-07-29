def solution(p):
    return p.replace(p[:len(p)-4], "*"*(len(p)-4))