x = int(input())
y = int(input())
if x > y:
    x, y = y, x
for item in range(x+1, y):
    reminder = item % 5
    if reminder == 2 or reminder == 3:
        print(item)
