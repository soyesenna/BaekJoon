
import sys


n, k = map(int, sys.stdin.readline().split())

scroes = []
for i in range(n):
    scroes.append(float(sys.stdin.readline()))

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
    bojeong = sum(scroes) / len(scroes) 
    jeolsa = sum(scroes) / len(scroes)
print("%.2f"%(jeolsa + 1e-6))
print("%.2f"%(bojeong + 1e-6))