def calculate(pa, pb,ga,gb):
    year = 0  # initial year = 0
    ga /= 100 # getting the actual parcentage value
    gb /= 100
    while pa <= pb: # when pa surpasses pb, break
        pa += pa * ga // 1 # pa = pa + int(pa * ga) - int as population can't be float value
        pb += pb * gb // 1 # pa = pb + int(pb * gb)
        year += 1
    if year > 100:
        print("Mais de 1 seculo.")
    else: # print the year
        print(f"{year} anos.")

t = int(input())

for i in range(t):

    pa,pb,ga,gb=map(float,input().split())
    calculate(int(pa),int(pb),ga,gb)