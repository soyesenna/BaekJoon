import sys

input = sys.stdin.readline

x,y,z = map(int, input().split())

s = input().rstrip()

caps = False

before = s[0]
res = 0
start = 0
for i in range(len(s)):
    if s[i] != before:
        tmp = []
        if before == 'A':
            if caps:
                tmp.append(x * len(s[start:i]))
                tmp.append(z + (len(s[start:i]) * y))
                if tmp[0] >= tmp[1]:
                    res += tmp[1]
                    caps = not caps
                else:
                    res += tmp[0]
            else:
                tmp.append(y * len(s[start:i]))
                tmp.append(z + (len(s[start:i]) * x))
                if tmp[0] >= tmp[1]:
                    res += tmp[1]
                    caps = not caps
                else:
                    res += tmp[0]
        else:
            if not caps:
                tmp.append(x * len(s[start:i]))
                tmp.append(z + (len(s[start:i]) * y))
                if tmp[0] >= tmp[1]:
                    res += tmp[1]
                    caps = not caps
                else:
                    res += tmp[0]
            else:
                tmp.append(y * len(s[start:i]))
                tmp.append(z + (len(s[start:i]) * x))
                if tmp[0] >= tmp[1]:
                    res += tmp[1]
                    caps = not caps
                else:
                    res += tmp[0]
        start = i

    before = s[i]

tmp = []
if s[start] == 'A':
    if caps:
        tmp.append(x * len(s[start:]))
        tmp.append(z + (len(s[start:]) * y))
        res += min(tmp)
    else:
        tmp.append(z + (len(s[start:]) * x))
        tmp.append(y * len(s[start:]))
        res += min(tmp)
else:
    if not caps:
        tmp.append(x * len(s[start:]))
        tmp.append(z + (len(s[start:]) * y))
        res += min(tmp)
    else:
        tmp.append(z + (len(s[start:]) * x))
        tmp.append(y * len(s[start:]))
        res += min(tmp)
            
print(res)