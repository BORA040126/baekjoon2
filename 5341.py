while(1):
    a=int(input())
    if(a==0):
        break
    else:
        b=0
        for i in range(1,a+1):
            b+=i
        print(b)