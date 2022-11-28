day = int(input('Enter day of week: '))
if day == 6 or day == 7:
    print("It's weekend")
elif day > 0 and day < 6:
    print("It's not weekend")
else:
    print("It's not day of week")
