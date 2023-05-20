import sys

input=sys.stdin.readline

N,M=map(int,input().split())

result=0

trains=[[0 for _ in range(20)]for _ in range(N)]
test=[]

for _ in range(N):
    command=list(map(int,input().split()))
    trainIdx=command[1]
    if len(command)==3:
        chainIdx=command[2]
    if command[0]==1:
        trains[trainIdx-1][chainIdx-1]=1
    elif command[0]==2:
        trains[trainIdx-1][chainIdx-1]=0
    elif command[0]==3:
        trains[trainIdx-1].pop(-1)
        trains[trainIdx-1].insert(0,0)
    elif command[0]==4:
        trains[trainIdx-1].pop(0)
        trains.append(0)

for train in trains:
    if train in test:
        pass
    else:
        result+=1
        test.append(train)

print(result)