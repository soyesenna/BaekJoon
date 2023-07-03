import sys
import functools

input = sys.stdin.readline

num_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'Z':0}
num_dict_inv = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
num_dict_2 = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900, 'ZZ':0}
num_dict_2_inv = {4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}

s = [list(input().rstrip()) for _ in range(2)]

nums = []

for k in range(2):
    now_s = s[k]
    for i in range(len(now_s)-1):
        for key in num_dict_2.keys():
            if ''.join(now_s[i:i+2]) == key:
                nums.append(num_dict_2[key])
                for r in range(2):
                    now_s[i+r] = 'Z'
    for i in range(len(now_s)):
        for key in num_dict:
            if now_s[i] == key:
                nums.append(num_dict[key])
                now_s[i] = 'Z'

sum_num = str(sum(nums))[::-1]

result = []
for i in range(len(sum_num)):
    now = int(sum_num[i]) * (10 ** i)
    if now in num_dict_2_inv.keys():
        result.append(num_dict_2_inv[now])
    elif now in num_dict_inv.keys():
        result.append(num_dict_inv[now])
    else:
        now = [now // (5 * (10 ** i)), now % (5 % (10 ** i))]
        result.append(num_
print(''.join(result[::-1]))