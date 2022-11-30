def quarter(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            print('Quarter 1')
        if x < 0 and y < 0:
            print('Quarter 3')
        if x > 0 and y < 0:
            print('Quarter 4')
        if x < 0 and y > 0:
            print('Quarter 2')
    else:
        print('x or y = 0')

coordinatesX = float(input("Input the value of X: "))
coordinatesY = float(input("Input the value of Y: "))

quarter(coordinatesX, coordinatesY)