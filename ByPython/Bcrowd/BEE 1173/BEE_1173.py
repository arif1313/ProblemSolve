def arrymake(a):
   arry=[0]*10
   for i in range(10):
      arry[i]=a
      a*=2
      print(f"N[{i}] = {arry[i]}")
      
a=int(input())
arrymake(a);
      