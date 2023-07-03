import sys

n = int(sys.stdin.readline())

cnt = 0
num = 666 

while cnt != n:
    if '666' in str(num):
        cnt += 1
    num += 1
print(num - 1)