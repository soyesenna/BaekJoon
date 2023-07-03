import sys
import collections

input = sys.stdin.readline

n = int(input())
m = int(input())

li = list(map(int, input().split()))

#번호, 추천 수, 시간
pictures = [[0, 0, 0] for _ in range(n)]

for now in li:
    num = list(map(lambda x: x[0], pictures))
    if now in num:
        pictures[num.index(now)][1] += 1
    elif [0, 0, 0] in pictures:
        pictures[pictures.index([0, 0, 0])] = [now, 0, 0]
    else:
        scores = list(map(lambda x: x[1], pictures))
        score_count = collections.Counter(scores)
        min_score = min(scores)
        if score_count[min_score] == 1:
            pictures[scores.index(min_score)] = [now, 0, 0]
        else:
            max_time_picture = [0,0,0]
            for i in range(len(pictures)):
                if pictures[i][1] == min_score:
                    if max_time_picture[2] < pictures[i][2]:
                        max_time_picture = pictures[i]
            pictures[pictures.index(max_time_picture)] = [now, 0, 0]
    for i in range(len(pictures)):
        pictures[i][2] += 1

final = list(filter(lambda x: x != 0, map(lambda x: x[0], pictures)))
final.sort()
for f in final:
    print(f, end=' ')
