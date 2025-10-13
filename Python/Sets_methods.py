# -------------------------------------------------------------------------------
# ------------------------- Sets methods -------------------------
# -------------------------------------------------------------------------------

# clear() => Removes all elements from the set, leaving it empty.

print("clear() method")

set_1 = {1, 2, 3}
set_1.clear()
print(set_1)

print("-------------------------------------------------------------------------------")

# union() => Returns a new set containing all unique elements from the given sets

print("union() method")

set_2 = {"One", "Two", "Three"}
set_3 = {"1", "2", "3"}
set_4 = {"Zero", "Cool"}

print(set_2 | set_3)
print(set_2.union(set_3, set_4))

print("-------------------------------------------------------------------------------")

# add() => Adds a specified element to the set.

print("add() method")

set_5 = {1, 2, 3, 4}
set_5.add(5)
set_5.add(6)
print(set_5)

print("-------------------------------------------------------------------------------")

# copy() => Returns a shallow copy of the set.

print("copy() method")

set_6 = {1, 2, 3, 4}
set_7 = set_6.copy()

print(set_6)
print(set_7)

set_6.add(6)

print(set_6)
print(set_7)

print("-------------------------------------------------------------------------------")

# remove() => Removes the specified element from the set. Raises an error if the element is not found.

print("remove() method")

set_8 = {1, 2, 3, 4}
set_8.remove(1)
# set_8.remove(7)
print(set_8)

print("-------------------------------------------------------------------------------")

# discard() => Removes the specified element from the set if it exists, and does nothing if the element is not found.

print("discard() method")

set_9 = {1, 2, 3, 4}
set_9.discard(1)
set_9.discard(7)
print(set_9)

print("-------------------------------------------------------------------------------")

# pop() => Removes and returns an arbitrary element from the set. Raises an error if the set is empty.

print("pop() method")

set_10 = {"A", True, 1, 2, 3, 4, 5}
print(set_10.pop())

print("-------------------------------------------------------------------------------")

# update() => Adds all elements from another set or iterable to the current set.

print("update() method")

set_11 = {1, 2, 3}
set_12 = {1, "A", "B", 2}
set_11.update(['Html', "Css"])
set_11.update(set_12)

print(set_11)

print("-------------------------------------------------------------------------------")

# difference() => Returns a new set containing elements that are in the first set but not in the others.

print("difference() method")

set_12 = {1, 2, 3, 4}
set_13 = {1, 2, 3, "Osama", "Ahmed"}
print(set_12)
print(set_12.difference(set_13))  # set_12 - set_13
print(set_12)

print("-------------------------------------------------------------------------------")

# difference_update() => Removes all elements from the current set that are also present in the specified set or sets.

print("difference_update() method")

set_14 = {1, 2, 3, 4}
set_15 = {1, 2, "Osama", "Ahmed"}
print(set_14)
set_14.difference_update(set_15)  # set_14 - set_15
print(set_14)

print("-------------------------------------------------------------------------------")

# intersection() => Returns a new set containing elements that are common to all specified sets.

print("intersection() method")

set_16 = {1, 2, 3, 4, "X", "Osama"}
set_17 = {"Osama", "X", 2}
print(set_16)
print(set_16.intersection(set_17))  # set_16 & set_17
print(set_16)

print("-------------------------------------------------------------------------------")

# intersection_update() => Updates the current set to keep only the elements that are common to all specified sets.

print("intersection_update() method")

set_18 = {1, 2, 3, 4, "X", "Osama"}
set_19 = {"Osama", "X", 2}
print(set_18)
set_18.intersection_update(set_19)  # set_18 & set_19
print(set_18)

print("-------------------------------------------------------------------------------")

# symmetric_difference() => Returns a new set containing elements that are in either of the sets, but not in both.

print("symmetric_difference() method")

set_20 = {1, 2, 3, 4, 5, "X"}
set_21 = {"Osama", "Zero", 1, 2, 4, "X"}
print(set_20)
print(set_20.symmetric_difference(set_21))  # set_20 ^ set_21
print(set_20)

print("-------------------------------------------------------------------------------")

# symmetric_difference_update() => Updates the current set to contain elements that are in either of the sets, but not in both.

print("symmetric_difference_update() method")

set_22 = {1, 2, 3, 4, 5, "X"}
set_23 = {"Osama", "Zero", 1, 2, 4, "X"}
print(set_22)
set_22.symmetric_difference_update(set_23)  # set_22 ^ set_23
print(set_22)

print("-------------------------------------------------------------------------------")

# issuperset() => Returns True if the set contains all elements of the specified set, otherwise returns False.

print("issuperset() method")

set_24 = {1, 2, 3, 4}
set_25 = {1, 2, 3}
set_26 = {1, 2, 3, 4, 5}

print(set_24.issuperset(set_25))  # True
print(set_24.issuperset(set_26))  # False

print("-------------------------------------------------------------------------------")

# issubset() => Returns True if all elements of the set are present in the specified set, otherwise returns False.

print("issuperset() method")

set_27 = {1, 2, 3, 4}
set_28 = {1, 2, 3}
set_29 = {1, 2, 3, 4, 5}

print(set_27.issubset(set_28))  # False
print(set_27.issubset(set_29))  # True

print("-------------------------------------------------------------------------------")

# isdisjoint() => Returns True if the two sets have no elements in common, otherwise returns False.

print("isdisjoint() method")

set_30 = {1, 2, 3, 4}
set_31 = {1, 2, 3}
set_32 = {10, 11, 12}

print(set_30.isdisjoint(set_31))  # False
print(set_30.isdisjoint(set_32))  # True