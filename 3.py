def sieve(lst):
    q = []
    [q.append(item) for item in reversed(lst) if item not in q]
    return tuple(q)
print(sieve([1, 2, 3, 4, 2,6]))
print(sieve([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))
print(sieve((1, 2, 3, 4, 5, 6, 7, 8, 9, 9.5)))
