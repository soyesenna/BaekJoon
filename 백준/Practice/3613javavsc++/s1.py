import sys
import collections

while True:
    s = sys.stdin.readline().rstrip()
    if s == '':
        break

    lang_flag = ''
    if len(s.split('_')) > 1:
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                lang_flag = 'notc'
                break
        if lang_flag != 'notc':
            lang_flag = 'c'
    elif len(s.split('_')) == 1:
        lang_flag = 'java'
    if s[0] == '_':
        lang_flag = 'non'
    if s[-1] == '_':
        lang_flag = 'non'
    if '__' in s:
        lang_flag = 'non'
    if 'A' <= s[0] <= 'Z':
        lang_flag = 'non'

    if lang_flag == 'c':
        char_list = []
        flag = False
        for i in range(len(s)):
            if s[i] =='_':
                flag = True
                continue
            if flag:
                char_list.append(chr(ord(s[i]) - 32))
                flag = False
                continue
            char_list.append(s[i])
        print(''.join(char_list))
    elif lang_flag == 'java':
        char_list = []
        #flag = False
        for i in range(len(s)):
            if 'A' <= s[i] <= 'Z':
                char_list.append('_')
                char_list.append(chr(ord(s[i]) + 32))
                continue
            char_list.append(s[i])
        print(''.join(char_list))
    else:
        print("Error!")