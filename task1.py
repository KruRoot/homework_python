# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
#     *Пример:*
#
#     - 6782 -> 23
#     - 0.56 -> 11

def sumNumbers(num):
    sum = 0
    for i in range(len(num)):
        if num[i] != '.':
            sum += int(num[i])
        else:
            i += 1
    return sum

number = input("Input the number:  ")
print(f"The sum of the numbers is: {sumNumbers(number)})