a,b=map(int,input().split())
e=list(map(int,input().split()))
d=[]
for i in e:
    if i<b:
        d.append(i)
for i in d:
    print(i,end=" ")
    
