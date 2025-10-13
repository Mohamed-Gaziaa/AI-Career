# -------------------------------------------------------------------------------
# ------------------------- Sets -------------------------
# -------------------------------------------------------------------------------
# [1] Set items are enclosed in curly braces. "{}"
# [2] Set items are not ordered and not indexed.
# [3] Set indexing and slicing cant be done.
# [4] Set has only immutable data types (Numbers, Strings, Tuples) list and dict are not.
# [5] Set items is unique
# -------------------------------------------------------------------------------

# Not ordered and not indexed

set_1 = {"Mohamed", "Ibrahim", 20}
print(set_1)
# print(set_1[0])

print("-------------------------------------------------------------------------------")

# Slicing cant be done

set_2 = {1, 2, 3, 4, 5, 6}
print(set_2)
# print(set_2[0:3])

print("-------------------------------------------------------------------------------")

# Has only immutable data types

# set_3 = {"Mohamed", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
set_3 = {"Mohamed", 100, 100.5, True, (1, 2, 3)}
print(set_3)

print("-------------------------------------------------------------------------------")

# Items is unique

set_4 = {1, 2, "Osama", "One", "Osama", 1}
print(set_4)