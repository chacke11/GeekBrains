def func(a,b):
    return int(a) + int(b)

a1 = input("Enter - ")
a2 = input("Enter - ")
a3 = input("Enter - ")


z = [a1,a2,a3]
z.sort()
z.pop(0)
a = z[0]
b = z[1]
print(func(a, b))




