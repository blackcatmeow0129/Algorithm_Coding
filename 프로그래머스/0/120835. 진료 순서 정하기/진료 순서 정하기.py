result={}
def solution(emergency):
    emergency_with_order = sorted(emergency, key=lambda x: -x)
    for n,i in enumerate(emergency_with_order, start=1): result[i]=n
    return [result[i] for i in emergency]