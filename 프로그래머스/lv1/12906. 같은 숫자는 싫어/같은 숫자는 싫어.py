def solution(arr):
    return [arr[a] for a in range(len(arr)-1) if arr[a]!=arr[a+1]] + [arr[len(arr)-1]]