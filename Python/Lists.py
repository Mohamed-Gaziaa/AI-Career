# -------------------------------------------------------------------------------
# ------------------------- Lists -------------------------
# -------------------------------------------------------------------------------
# [1] List items are enclosed in square brackets.
# [2] List are ordered, to use index to access item.
# [3] List are mutable => add, delete, edit.
# [4] List items is not unique.
# [5] List can have different data types.
# -------------------------------------------------------------------------------

myList = ["One", "Two", "One", 1, 100.5, True]

print(myList)  # Whole List
print(myList[1])  # "Two"
print(myList[-1])  # True
print(myList[-3])  # 1

print(myList[1:4])  # ['Two', 'One', 1]
print(myList[:4])  # ['One', 'Two', 'One', 1]
print(myList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myList[::2])  # ['One', 'One', 100.5]

print(myList)
# myList[1] = 2
# myList[-1] = False
myList[0:3] = ["A"]
print(myList)