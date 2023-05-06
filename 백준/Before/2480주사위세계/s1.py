import sys
import collections

dice = list(map(int, sys.stdin.readline().split()))

counter = collections.Counter(dice)

result = 0

if len(counter) == 3:
    result = max(dice) * 100
else:
    for key in counter:
        if counter[key] == 2:
            result = 1000 + (key * 100)
        elif counter[key] == 3:
            result = 10000 + (key * 1000)
print(result)