# -------------------------------------------------------------------------------
# ------------------------- Tuples -------------------------
# -------------------------------------------------------------------------------
# [1] Tuple items are enclosed in parentheses. "()"
# [2] You can remove the parentheses if you want.
# [3] Tuple are ordered, To use index to access item.
# [4] Tuple are immutable => You cant add or delete.
# [5] Tuple items is not unique.
# [6] Tuple can have different data types.
# [7] Operators used in strings and lists available in tuples.
# -------------------------------------------------------------------------------

# Tuple syntax & type test

Tuple_1 = ("Mohamed", "Ibrahim")
Tuple_2 = "Mohamed", "Ibrahim"

print(Tuple_1)
print(Tuple_2)

print(type(Tuple_1))
print(type(Tuple_2))

print("-------------------------------------------------------------------------------")

# Tuple Indexing

Tuple_3 = (1, 2, 3, 4, 5)
print(Tuple_3[0])
print(Tuple_3[-1])
print(Tuple_3[-3])

# print("-------------------------------------------------------------------------------")

# Tuple Assign Values

Tuple_4 = (1, 2, 3, 4, 5)
# Tuple_4[2] = "Three"
# print(Tuple_4)  # 'tuple' object does not support item assignment

print("-------------------------------------------------------------------------------")

# Tuple Data

Tuple_5 = ("Mohamed", "Mohamed", 1, 2, 3, 100.5, True)
print(Tuple_5[1])
print(Tuple_5[-1])