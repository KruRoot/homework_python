def inputNumbers(HowManyNum):
    xy = ["X", "Y"]
    numbers = []
    for i in range(HowManyNum):
        intnumber = int(input(f"Input the value {xy[i]}: "))
        numbers.append(intnumber)
    return numbers


def calculateDistance(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return distance

HowManyNum = 2
print("Input the coordinates of А")
coordinatesA = inputNumbers(HowManyNum)
print("Input the coordinates of B")
coordinatesB = inputNumbers(HowManyNum)
print(f"Distance between A and B: {format(calculateDistance(coordinatesA, coordinatesB), '.2f')}")