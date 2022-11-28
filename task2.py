HowManyNum = 3
xyz = ["X", "Y", "Z"]
num = [0, 0, 0]
for i in range(HowManyNum):
    num[i] = (input(f"Введите значение {xyz[i]}: "))
left = not (num[0] or num[1] or num[2])
right = not num[0] and not num[1] and not num[2]
if left == right:
    print("True")
else:
    print("False")