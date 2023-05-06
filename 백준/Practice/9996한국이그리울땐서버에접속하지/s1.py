import sys
import collections

n = int(sys.stdin.readline())

pattern = list(sys.stdin.readline().rstrip().split("*"))

result = []

for _ in range(n):
    s = sys.stdin.readline().rstrip()

    if len(s) < len(pattern[0]) + len(pattern[1]):
        result.append("NE")
        continue
    s_first = s[0:len(pattern[0])]

    first_flag = False
    if s_first == pattern[0]:
        first_flag = True
    
    last_flag = False
    s_last = s[-len(pattern[1]):]
    if s_last == pattern[1]:
        last_flag = True
    
    if first_flag and last_flag:
        result.append("DA")
    else:
        result.append("NE")

for i in result:
    print(i)
