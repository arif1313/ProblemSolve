n=int(input())

while n!=0:
    N=int(input());
    isEven=N%2;
    
    if N<0:
       
        if isEven==0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")
    elif N>0:
        if isEven==0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else:
        print("NULL")
    n-=1








