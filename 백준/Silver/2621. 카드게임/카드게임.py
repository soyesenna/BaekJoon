from doctest import FAIL_FAST
from itertools import count
import sys
import collections

def first(card_color, card_number):
    counter_color = collections.Counter(card_color)
    if len(list(counter_color.keys())) != 1:
        return False
    card_number = sorted(card_number)
    if card_number[0] + card_number[4] != card_number[2] * 2 or card_number[1] + card_number[3] != card_number[2] * 2 or card_number[0] + card_number[4] != card_number[1] + card_number[3]:
        return False
    return True

def second(card_number):
    counter = collections.Counter(card_number)
    for key in list(counter.keys()):
        if counter[key] == 4:
            return key, True
    return 0, False

def third(card_number):
    counter = collections.Counter(card_number)
    counter_li = list(counter.keys())
    tmp = []
    for key in counter_li:
        if counter[key] == 2:
            tmp.append([2,key])
        else:
            tmp.append([3,key])
    if len(tmp) == 2:
        return tmp, True
    else:
        return 0, False

def four(card_color):
    counter = collections.Counter(card_color)
    if len(list(counter.keys())) == 1:
        return True
    return False

def five(card_number):
    card_number = sorted(card_number)
    if card_number[0] + card_number[4] != card_number[2] * 2 or card_number[1] + card_number[3] != card_number[2] * 2 or card_number[0] + card_number[4] != card_number[1] + card_number[3]:
        return False
    return True

def six(card_number):
    counter = collections.Counter(card_number)
    counter_keys = list(counter.keys())
    for key in counter_keys:
        if counter[key] == 3:
            return key, True

    return 0, False

def seven(card_number):
    counter = collections.Counter(card_number)
    counter_keys = list(counter.keys())

    nums = []
    for key in counter_keys:
        if counter[key] == 2:
            if len(nums) == 1:
                nums.append(key)
                return nums, True
            else:
                nums.append(key)
    return [0,0], False

def eight(card_number):
    counter = collections.Counter(card_number)
    counter_keys = list(counter.keys())

    for key in counter_keys:
        if counter[key] == 2:
            return key, True
    return 0, False
    


card_color= []
card_number = []
for _ in range(5):
    tmp = sys.stdin.readline().rstrip().split()
    card_color.append(tmp[0])
    card_number.append(int(tmp[1]))


if first(card_color, card_number):
    print(max(card_number)  + 900)
    sys.exit()

second_num, flag = second(card_number)
if flag:
    print(second_num + 800)
    sys.exit()

third_li, flag = third(card_number)
if flag:
    third_li = sorted(third_li, key=lambda x:x[0])
    print(third_li[1][1] * 10 + third_li[0][1] + 700)
    sys.exit()

if four(card_color):
    print(max(card_number) + 600)
    sys.exit()


if five(card_number):
    print(max(card_number) + 500)
    sys.exit()

six_num, flag = six(card_number)
if flag:
    print(six_num + 400)
    sys.exit()

seven_nums, flag = seven(card_number)
if flag:
    print(max(seven_nums) * 10 + min(seven_nums) + 300)
    sys.exit()

eight_num, flag = eight(card_number)
if flag:
    print(eight_num + 200)
    sys.exit()

print(max(card_number) + 100)