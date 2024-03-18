while(1):
    a=input()
    a=a.lower()
    if(a=="#"):
        break
    else:
        b=a.count("a")+a.count("e")+a.count("i")+a.count("o")+a.count("u")
        print(b)