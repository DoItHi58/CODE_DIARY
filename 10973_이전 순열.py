N=int(input())
x=list(map(int,input().split()))
check=N

for i in range(N-1,-1,-1):
    if x[i-1]>x[i]:
        check=i-1
        break

if x==[i for i in range(1,N+1)]:
    print(-1)
else:
    for i in range(N-1,0,-1):
        if x[i]<x[check]:
            x[i],x[check]=x[check],x[i]
            break
    x=x[:check+1]+sorted(x[check+1:],reverse=True)

    for i in x:
        print(i,end=" ")