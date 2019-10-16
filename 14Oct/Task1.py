def func(a, b):
    return a // b

a = int(input("Enter first values - "))
if a <= 0:
    print("Делить на нуль нельзя ")
else:
    b = int(input("Enter second values - "))
if b <= 0:
    print("Делить на нуль нельзя ")
else:
    print(func(a, b))
