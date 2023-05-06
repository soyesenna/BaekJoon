import sys

x, y, w, h = map(int, sys.stdin.readline().split())

result = [x, y, w - x, h - y]

print(min(result))