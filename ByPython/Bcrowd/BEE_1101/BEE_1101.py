while True:
    x, y = map(int, input().split())
    if x <= 0 or y <= 0:
        break

    total = 0
    if x > y:
        x, y = y, x
    for item in range(x, y+1):
        total = total+item
    # if reminder==2 or reminder ==3:
        print(item, end=" ")

    print(f"Sum={total}")
