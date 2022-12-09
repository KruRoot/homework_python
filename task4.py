# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

N = int(input("Input the N: "))
file = open('file.txt', 'w')
for i in range(N):
    file.write(str(random.uniform(-N, N + 1)))
    file.write('\n')
file.close()

positions = [int(input("Input the first position: ")), int(input("Input the second position: "))]
current_line = 1
num1 = 0
num2 = 0
file = open('file.txt', 'r')
for line in file:
    if current_line == positions[0]:
        num1 = line
    elif current_line == positions[1]:
        num2 = line
    current_line += 1
file.close()

print(format(float(num1) * float(num2), '.2f'))