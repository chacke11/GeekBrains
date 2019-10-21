lst = [input("Введите значения начального листа - ")]
def nodpl(lst):
    for x in lst:
        if lst.count(x) == 1:
            yield x

res = [x for x in nodpl(lst)]
print(res)