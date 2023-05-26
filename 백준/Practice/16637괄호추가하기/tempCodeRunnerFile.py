import sys

def calculate(li):
    result = int(li[0])
    for i in range(1, len(li), 2):
        if li[i] == '+':
            result += int(li[i+1])
        elif li[i] == '*':
            result *= int(li[i+1])
        elif li[i] == '-':
            result -= int(li[i+1])
    return result

input = sys.stdin.readline

n = int(input())

s = list(input().rstrip())

result = []
for i in range(0, len(s)-1, 2):
    if s[i+1] == '+':
        tmp = s[:i] + [str(int(s[i]) + int(s[i + 2]))] + s[i+3:]
    elif s[i+1] == '*':
        tmp = s[:i] + [str(int(s[i]) * int(s[i + 2]))] + s[i+3:]
    elif s[i+1] == '-':
        tmp = s[:i] + [str(int(s[i]) - int(s[i + 2]))] + s[i+3:]
    result.append(calculate(tmp))

print(max(result))