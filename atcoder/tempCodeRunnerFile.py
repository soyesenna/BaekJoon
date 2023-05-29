import sys



input = sys.stdin.readline

x,y,z = map(int, input().split())

s = input().rstrip()

caps = False

def count(s):
    global x, y, z, caps
    tmp = []
    for i in range(len(s)):
        if s[i] != s[0]:

            if s[0] == 'A':
                if caps:
                    tmp.append(len(s[:i]) * x)
                    tmp[-1] += count(s[i:])
                    tmp.append(z + (len(s[:i]) * y))
                    caps = not caps
                    tmp[-1] += count(s[i:])
                    caps = not caps
                else:
                    tmp.append((len(s[:i]) * y))
                    tmp[-1] += count(s[i:])
                    tmp.append(z + (len(s[:i]) * x))
                    caps = not caps
                    tmp[-1] += count(s[i:])
                    caps = not caps
            else:
                if not caps:
                    tmp.append(len(s[:i]) * x)
                    tmp[-1] += count(s[i:])
                    tmp.append(z + (len(s[:i]) * y))
                    caps = not caps
                    tmp[-1] += count(s[i:])
                    caps = not caps
                else:
                    tmp.append(y * len(s[:i]))
                    tmp[-1] += count(s[i])
                    tmp.append(z + (len(s[:i]) * y))
                    caps = not caps
                    tmp[-1] += count(s[i:])
                    caps = not caps

    if len(tmp) == 0:
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

result = count(s)
print(result)