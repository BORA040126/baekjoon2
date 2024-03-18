a=int(input())
b=[]
for i in range(a):
    b.append(input())
b=list(set(b))
b.sort()
b.sort(key=len)
for i in b:
    print(i)