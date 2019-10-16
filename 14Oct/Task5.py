s = 0


try:

    while True:

        for n in map(int, input("Введите значения - ").split()):
            s += n
        print(s)
except ValueError:
    print('Сумма - ', s)
