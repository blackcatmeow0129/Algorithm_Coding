from functools import reduce
def solution(my_string, n):
    return (my_string[0]*(n-1)+reduce(lambda x,y:x+y*n,my_string))