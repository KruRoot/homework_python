# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
#     *Пример:*
#
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import sys
sys.set_int_max_str_digits(0)

num = int(input("Input the number: "))
N = []
for i in range(1, num):
    if i == 1:
        N.append(i)
    else:
        N.append(i * N[i - 2])
print(N)