import sys

input = sys.stdin.readline

n = int(input())

s = input().rstrip()

length = 1

while length < n:
    flag = True
    for i in range(n-length+1):
        now = s[i:i+length]
        for j in range(n - length+1):
            if i == j:
                continue
            if now == s[j:j+length]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(length)
        sys.exit()
    length += 1
print(length)