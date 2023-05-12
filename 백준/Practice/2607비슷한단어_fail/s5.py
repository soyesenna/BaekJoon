from re import I
import sys
import collections

def is_same(s, target):
    counter_s = collections.Counter(s)
    counter_t = collections.Counter(target)
    for key in list(counter_s.keys()):
        if counter_s[key] != counter_t[key]:
            return False
    return True

def plus_minus(s, target: str):
    if len(s) < len(target):
        tmp = list(s)
        for i in range(len(target)):
            tmp.append(target[i])
            if is_same(tmp, target):
                return True
            tmp.pop()
    elif len(s) > len(target):
        tmp = list(target)  
        for i in range(len(s)):
            tmp.append(s[i])
            if is_same(s, tmp):
                return True
            tmp.pop()
    else:
        if is_same(s, target):
            return True
    
    return False

def change(s, target):
    s_li = (list(s))
    t_li = (list(target))
    tmp = s_li[:]
    for i in tmp:
        if i in t_li:
            s_li.remove(i)
            t_li.remove(i)
    if len(s_li) == 1 and len(t_li) == 1:
        return True
    else:
        return False 


n = int(sys.stdin.readline())

pre_s = ''
targets = []
for i in range(n):
    if i == 0:
        pre_s = sys.stdin.readline().rstrip()
    else:
        targets.append(sys.stdin.readline().rstrip())


result = 0
for target in targets:
    if len(pre_s) == len(target):
        if change(pre_s, target) or plus_minus(pre_s, target):
            print(target)
            result += 1
    else:
        if plus_minus(pre_s, target):
            print(target)
            result += 1
print(result)