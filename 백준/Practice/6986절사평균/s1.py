
import sys

n, k = map(int, sys.stdin.readline().split())

scroes = []
for i in range(n):
    scroes.append(float(sys.stdin.readline()) * 1e+6)

if k != 0:
    scroes.sort()
    scroes = scroes[k:-k]

    jeolsa = sum(scroes) / len(scroes)
    min = scroes[0]
    max = scroes[-1]
    for _ in range(k):
        scroes.append(min)
        scroes.append(max)

    bojeong = sum(scroes) / len(scroes)
else:
    bojeong, jeolsa = sum(scroes) / len(scroes)

bojeong = list(str((bojeong / 1e+6)))
jeolsa = list(str(jeolsa / 1e+6))

if len(bojeong) > 4:
    if bojeong[bojeong.index('.') + 3] >= '5':
        a = bojeong.index('.') + 2
        bojeong[a] = int(bojeong[a]) + 1
if len(jeolsa) > 4:
    if jeolsa[jeolsa.index('.') + 3] >= '5':
        a = jeolsa.index('.') + 2
        jeolsa[a] = int(jeolsa[a]) + 1

while len(bojeong) <= 4:
    bojeong.append(0)
while len(jeolsa) <= 4:
    jeolsa.append(0)

for i in range(4):
    print(jeolsa[i], end='')
print()
for i in range(4):
    print(bojeong[i], end='')