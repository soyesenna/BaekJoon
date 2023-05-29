import sys

input = sys.stdin.readline

x,y,z = map(int, input().split())

s = input().rstrip()

caps = False

def count(s):
    global x, y, z, caps
    now_str = ''
    for i in range(len(s)):
        if s[0] != s[i]:
            now_str = s[:i]
            break
    if now_str == '':
        tmp = []
        if s[0] == 'A':
            if caps:
                tmp.append(len(s) * x)
                tmp.append(z + (len(s) * y))
            else:
                tmp.append((len(s) * y))
                tmp.append(z + (len(s) * x))
        else:
            if not caps:
                tmp.append(len(s) * x)
                tmp.append(z + (len(s) * y))
            else:
                tmp.append(y * len(s))
                tmp.append(z + (len(s) * y))
        return min(tmp)
    
    tmp = []
    if now_str[0] == 'A':
        if caps:
            tmp.append(len(now_str) * x)
            tmp[-1] += count(s[i:])
            tmp.append(z + (len(now_str) * y))
            caps = not caps
            tmp[-1] += count(s[i:])
            caps = not caps
        else:
            tmp.append((len(now_str) * y))
            tmp[-1] += count(s[i:])
            tmp.append(z + (len(now_str) * x))
            caps = not caps
            tmp[-1] += count(s[i:])
            caps = not caps
    else:
        if not caps:
            tmp.append(len(now_str) * x)
            tmp[-1] += count(s[i:])
            tmp.append(z + (len(now_str) * y))
            caps = not caps
            tmp[-1] += count(s[i:])
            caps = not caps
        else:
            tmp.append(y * len(now_str))
            tmp[-1] += count(s[i])
            tmp.append(z + (len(now_str) * y))
            caps = not caps
            tmp[-1] += count(s[i:])
            caps = not caps
    return min(tmp)

print(count(s))