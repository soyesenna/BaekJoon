

n,m,d,s=map(int,input().split())
eat = [list(map(int, input().split())) for _ in range(d)]
apa = [list(map(int, input().split())) for _ in range(s)]
apchm=[]
cnt=1


for i in range(len(apa)):
    apch = tuple(map(lambda x: x[1], filter(lambda x: x[0] == apa[i][0] and apa[i][1] > x[2], eat)))
    apchm.append(apch)

japch = []
if len(apchm) == 1:
    for i in range(len(apchm[0])):
        japch.append(apchm[0][i])
else:
    for i in range(len(apchm[0])):
        for j in range(1,len(apchm)):
            if not apchm[0][i] in apchm[j]:
                break
            japch.append(apchm[0][i])

cnt = set()
for real_sick in japch:
    for i in range(d):
        if eat[i][1]==real_sick:
            cnt.add(eat[i][0])

print(len(cnt))