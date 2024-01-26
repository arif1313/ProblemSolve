times = int(input())
rabbits = 0
rats = 0
Sapos = 0
total_animal = 0
for i in range(0, times, 1):
    conity, symbol = map(str, input().split())
    animalInt = int(conity)
    if symbol == "C":
        rabbits = rabbits+animalInt
        total_animal = total_animal+animalInt
    elif symbol == "R":
        rats = rats+animalInt
        total_animal = total_animal+animalInt
    elif symbol == "S":
        Sapos = Sapos+animalInt
        total_animal = total_animal+animalInt

print(f"Total: {total_animal} cobaias");
print(f"Total de coelhos: {rabbits}")
print(f"Total de ratos: {rats}");
print(f"Total de sapos: {Sapos}");
print(f"Percentual de coelhos: {rabbits/total_animal*100:.2f} %")
print(f"Percentual de ratos: {rats/total_animal*100:.2f} %")
print(f"Percentual de sapos: {Sapos/total_animal*100:.2f} %")
