def rangeinquarter(quar):
    if quar > 0 and quar < 5:
        if quar == 1:
            print('+x, +y')
        elif quar == 2:
            print('-x, +y')
        elif quar == 3:
            print('-x, -y')
        elif quar == 4:
            print('+x, -y')
    else:
        print("Quarter isn't exist!")

quarter = int(input("Input the number of quarter: "))
rangeinquarter(quarter)