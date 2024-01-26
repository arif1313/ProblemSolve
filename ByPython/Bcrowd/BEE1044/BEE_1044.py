a, b = map(int, input().split())
moul=b%a;
moul1=a%b;
if moul==0 or moul1==0:
    print("Sao Multiplos");
else:
    print("Nao sao Multiplos")


