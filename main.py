# from pathlib import Path

# file = Path("./files/Sample.txt")
# if file.exists():
#     print(file.read_text())
# else:
#     file.write_text("Hello, World!")
# ------------------------------------------------------------------

# from functools import singledispatch

# @singledispatch
# def show(data):
#     print("Called by String : ", data)

# @show.register
# def _show(data: int):
#     print("Called by Integer : ", data)

# @show.register
# def _show(data: list):
#     print("Called by List : ", data)

# show([1, 2, 3])

# -------------------------------------------------------------------

# import timeit
# def fun():
#     return [i for i in range(1000)]
# def fun1():
#     return list(range(1000))

# print(timeit.timeit(fun, number=10000))
# print(timeit.timeit(fun1, number=10000))

# --------------------------------------------------------------------

# from dataclasses import dataclass

# @dataclass
# class Book:
#     title: str
#     author: str
#     year: int
# b = Book("STM", "George Orwell", 1949)
# print(b.title)

# ---------------------------------------------------------------------

# lst = [("apple", 2), ("banana", 3), ("apple", 4)]
# group = {}
# for i in lst:
#     if group.get(i[0]):
#         group[i[0]].append(i[1])
#     else:
#         group[i[0]] = [i[1]]
# print(group)

# -----------BY using the `collections.defaultdict`--------------
# from collections import defaultdict
# lst = [("apple", 2), ("banana", 3), ("apple", 4)]
# group = defaultdict(list)
# for k, v in lst:
#     group[k].append(v)
# print(dict(group))

# ----------------------------------------------------------------------
# from functools import lru_cache
# import time
# for i in range(10):
#     @lru_cache(maxsize=2)
#     def fun(a,b):
#         time.sleep(3)
#         return a + b
#     print(fun(1, 2))
# ----------------------------------OR------------------------------------

# @lru_cache(maxsize=100)
# def feb(n):
#     if n < 2:
#         return n
#     else:
#         return feb(n-1) + feb(n-2)
# print(feb(30))

# ----------------------------------------------------------------------
