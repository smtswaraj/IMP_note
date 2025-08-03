# from pathlib import Path

# file = Path("Sample.txt")
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

