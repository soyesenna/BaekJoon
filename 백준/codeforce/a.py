def finding(x,m):
    if(x<m):
        return(0)
    if(x==m):
        print("YES")
        return(1)
    return(finding(x/3,m) or finding(2*(x/3),m))
for _ in range(int(input())):
    n,m=map(int,input().strip().split())
    if(n==m):
        print("YES")
        continue
    if(n<m):
        print("NO")
        continue
    f=finding(n,m)
    if(f==0):
        print("NO")