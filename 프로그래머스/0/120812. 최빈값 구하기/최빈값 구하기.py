from collections import defaultdict

def solution(array):
    freq = defaultdict(int)
    for elem in array: freq[elem] += 1 #딕셔너리로 문자,개수저장됨
    
    sorted_arr = sorted(set(array), key= lambda elem: -freq[elem]) #가장 많은 애부터 리스트로 정렬
    if len(sorted_arr)<2:
        return sorted_arr[0]
    elif freq[sorted_arr[0]]!=freq[sorted_arr[1]]:
        return sorted_arr[0]
    else:
        return -1