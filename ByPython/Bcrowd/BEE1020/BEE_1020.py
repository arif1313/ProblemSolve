import math
x=int(input());
year=math.floor(x/365);
days=x-(year*365)
month= math.floor(days/30);
remind= days-(month*30);
print(year,"ano(s)")
print(month,"mes(es)")
print(remind,"dia(s)")