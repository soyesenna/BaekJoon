import sys
import collections

s = list(sys.stdin.readline().rstrip().split(' '))

result = []

for i in range(1, len(s)):
    tmp = s[0]
    deq = collections.deque(s[i])
    before_alpha = False
    for j in range(len(deq)):
        last = deq.pop()
        if last != ',' and last != ';':
            if last == '[':
                tmp += ']'
            elif last == ']':
                tmp += '['
            else:
                if before_alpha and not ('a' <= last <= 'z' or 'A' <= last <= 'Z'):
                    tmp += ' '
                if 'a' <= last <= 'z' or 'A' <= last <= 'Z':
                    before_alpha = True
                tmp += last
        
    tmp += ';'
    result.append(tmp)
    
print(result)