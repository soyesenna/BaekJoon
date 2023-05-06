import sys
import collections

n, m = map(int, sys.stdin.readline().split())

girl_groups = dict()
for i in range(n):
    gruop_name = sys.stdin.readline().rstrip()
    n_mem = int(sys.stdin.readline())

    tmp = []
    for j in range(n_mem):
        tmp.append(sys.stdin.readline().rstrip())

    tmp.sort()
    girl_groups[gruop_name] = tmp


quiz = []
for i in range(m):
    quiz_ = sys.stdin.readline().rstrip()
    quiz_type = int(sys.stdin.readline())
    quiz.append([quiz_, quiz_type])


for i in range(len(quiz)):
    if quiz[i][1] == 1:
        answer = ''
        for j in girl_groups:
            if quiz[i][0] in girl_groups[j]:
                answer = j
                break
        print(answer)
    elif quiz[i][1] == 0:
        for j in girl_groups[quiz[i][0]]:
            print(j)


