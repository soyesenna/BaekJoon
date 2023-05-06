import sys

n = int(sys.stdin.readline())

if n < 10:
    n_str = '0' + str(n)
else:
    n_str = str(n//10) + str(n - ((n//10) * 10))

cnt = 0
while True:
    a = str(int(n_str[0]) + int(n_str[1]))
    n_str = n_str[1] + a[-1]
    cnt += 1

    if int(n_str) == n:
        break
    
print(cnt)