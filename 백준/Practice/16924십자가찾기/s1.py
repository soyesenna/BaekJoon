import sys

input = sys.stdin.readline
n, m = map(int, input().split())

li = []
for _ in range(n):
    li.append(list(input()))

def find(a):
    global n, m
    global li
    for i in range(a, n - a - 1):
        for j in range(a, m - a- 1):
            if li[i][j] == '*' or li[i][j] == 'O':
                for z in range(1, a + 1):
                    if li[i + z][j] == '.' or li[i - z][j] == '.':
                        pass



