N,G=map(str,input().split())

check={}
game={'Y':1,'F':2,'O':3}
waiting=[]
answer=0
for i in range(int(N)):
    name=input()
    if name in check:continue
    else:
        check[name]=1
        waiting.append(name)
        if len(waiting)==game[G]:
            answer+=1
            waiting.clear()
print(answer)