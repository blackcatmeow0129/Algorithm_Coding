def solution(hp):
    count=0
    count+=hp//5
    hp=hp%5
    count+=hp//3
    hp=hp%3
    count+=hp
    hp=0
    return count