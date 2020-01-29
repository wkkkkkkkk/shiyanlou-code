for a in range(1,101):
    if a % 7 == a or a % 10 == 7 or a // 10 == 7:
        continue
    print(a)
