import sys
import collections

def binary_search(li: list, find_num: int):
    start = -1
    end = len(li)
    flag = False;
    while abs(start - end) > 1:
        idx = (start + end) // 2
        if li[idx] ==  find_num:
            flag = True
            break
        elif li[idx] < find_num:
            start = idx
        else:
            end = idx

    
    return flag

input = sys.stdin.readline

n = int(input())

li = sorted(list(map(int, input().split())))
counter = collections.Counter(li)

m = int(input())

result = []

target = list(map(int, input().split()))

for num in target:
    if binary_search(li, num):
        print(counter[num], end=' ')
    else:
        print(0, end=' ')
