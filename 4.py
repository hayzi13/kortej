def del_from_tuple(tpl, q):
    lst = list(tpl)
    if q in tpl:
        lst.remove(q)
    return tuple(lst)
print(del_from_tuple((1, 2, 3), 1))
print(del_from_tuple((1, 2, 3, 4, 5), 3))
print(del_from_tuple((2, 4, 6, 6.6, 3, 1), 6.6))
