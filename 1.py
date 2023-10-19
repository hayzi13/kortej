def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return ()
    return tuple(sorted(tpl))
print(tpl_sort((4, 8, 3, 1, 9)))
print(tpl_sort((4, 6, 2.1, 1, 7)))
