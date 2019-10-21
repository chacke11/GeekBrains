
list=input("Введите числа - ").split()
for i in range(1, len(list)):
   if int(list[i])>int(list[i-1]):
       list2 = list[i]
       print(list2)
