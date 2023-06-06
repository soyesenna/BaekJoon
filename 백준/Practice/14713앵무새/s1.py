import sys
import collections

input = sys.stdin.readline

n = int(input())

s = [collections.deque(input().rstrip().split()) for _ in range(n)]

l = collections.deque(input().split())

while l:
    now_s = l.popleft()
    for i in range(n):
        if len(s[i]) != 0:
            now_word = s[i].popleft()
            if now_s == now_word:
                break
            else:
                s[i].appendleft(now_word)

        if i == n-1:
            print("Impossible")
            sys.exit()
if sum(map(lambda x: len(x), s)) == 0:
    print("Possible")
else:
    print("Impossible")