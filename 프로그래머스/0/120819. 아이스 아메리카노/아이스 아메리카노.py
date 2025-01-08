def solution(money):
    count = money//5500
    leftm = money%5500
    return [count,leftm] if leftm>0 else [count,0]