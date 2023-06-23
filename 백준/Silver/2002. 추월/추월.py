import sys

L1,L2=[],[]
N=int(sys.stdin.readline())

for i in range(N):
    L1.append(sys.stdin.readline())
for i in range(N):
    L2.append(sys.stdin.readline())

ans=0

for l in L2:
    if L1.index(l) != 0:
        ans+=1
        L1.remove(l)
    else: L1.remove(l)        

print(ans)