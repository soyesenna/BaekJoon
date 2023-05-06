import sys

mo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    s = sys.stdin.readline().rstrip()

    if s == '#':
        break

    cnt = 0
    for i in range(len(s)):
        if s[i] in mo:
            cnt += 1
    
    print(cnt)