def solution(num_list):
    odd=0
    for i in num_list:
        if i%2: odd+=1
    return [len(num_list)-odd,odd]