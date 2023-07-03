import sys

shortcut = []

def first(word):
    global shortcut
    if word[0].upper() not in shortcut:
        shortcut.append(word[0].upper())
        return True
    return False


def second(word):
    global shortcut
    for i in range(len(word)):
        if word[i].upper() not in shortcut:
            shortcut.append(word[i].upper())
            return word[i]
    return ''

input = sys.stdin.readline

n = int(input())

result = []
for _ in range(n):
    s = list(input().split())
    tmp_result = []
    flag = False
    for word in s:
        tmp = list(word)
        if not flag and first(word):
            tmp.insert(0, '[')
            tmp.insert(2, ']')
            flag = True
        tmp_result.append(tmp)
    if not flag:
        for word in tmp_result:
            res = second(word)
            if res != '':
                index = word.index(res)
                word.insert(index, '[')
                word.insert(index + 2, ']')
                break
    
    result_s = ''
    for word in tmp_result:
        result_s += ''.join(word)
        result_s += ' '
    print(result_s)

