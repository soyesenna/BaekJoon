import sys

colors = {'black':0, 'brown':1, 'red':2, 'orange':3, 'yellow':4, 'green':5, 'blue':6, 'violet':7, 'grey':8, 'white':9}

result = ''
for _ in range(2):
    a = sys.stdin.readline().rstrip()
    result += str(colors[a])

a = sys.stdin.readline().rstrip()
result += str(10**colors[a])[1:]

print(int(result))