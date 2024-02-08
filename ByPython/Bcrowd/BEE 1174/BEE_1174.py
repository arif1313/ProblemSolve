array=[0]*100
for i in range(len(array)):
   a=float(input())
   if a<=10:
      array[i]=a
      print(f"A[{i}] = {array[i]:.1f}")