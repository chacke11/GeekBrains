def fctr(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fctr(n - 1)

lst = [x for x in range(15)]

def fibo_gen(itrs):
    for el in itrs:
        yield(fctr(el))

print(list(fibo_gen(lst)))