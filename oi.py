x = 3
while True:
    try:
        print(10/x)
        x -= 1
    except ZeroDivisionError:
        print('dividiu por zero')
        break

