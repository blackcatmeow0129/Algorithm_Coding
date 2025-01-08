def solution(angle):
    arange={89:1,90:2,179:3,180:4}
    for radian in arange.keys():
        if angle <= radian:
            return arange[radian]