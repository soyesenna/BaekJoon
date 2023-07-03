import sys

input = sys.stdin.readline

n = int(input())

in_trucks = [input().rstrip() for _ in range(n)]
out_trucks = [input().rstrip() for _ in range(n)]

result = 0

for i in range(1, n):
    left_in = in_trucks[:i]
    right_out = out_trucks[out_trucks.index(in_trucks[i]) + 1:]
    for j in range(len(left_in)):
        if left_in[j] in right_out:
            result += 1
            break
print(result)

