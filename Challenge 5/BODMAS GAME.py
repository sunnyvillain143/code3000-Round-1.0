while(1):
    n=int(input())
    x=n%6
    y=n//6
    a=1
    z=1
    for i in range(y):
        z=z+1
        a=a**z
        z=z+1
        a=a/z
        z=z+1
        a=a*z
        z=z+1
        a=a+z
        z=z+1
        a=a-z
    if(x!=0):
        if(x==2):
            z=z+1
            a=a**z
        elif(x==3):
            z=z+1
            a=a**z
            z=z+1
            a=a/z
        elif(x==4):
            z=z+1
            a=a**z
            z=z+1
            a=a/z
            z=z+1
            a=a*z
        elif(x==5):
            z=z+1
            a=a**z
            z=z+1
            a=a/z
            z=z+1
            a=a*z
            z=z+1
            a=a+z
    print(n," ",round(a,6))
