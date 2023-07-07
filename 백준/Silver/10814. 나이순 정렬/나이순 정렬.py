import sys

n = int(input())

persons = [list(input().split()) for _ in range(n)]

persons.sort(key=lambda x: (int(x[0])))

for person in persons:
    print(person[0], person[1])