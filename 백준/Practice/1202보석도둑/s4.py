import sys

input = sys.stdin.readline

n, k = map(int, input().split())

jew = [list(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]

