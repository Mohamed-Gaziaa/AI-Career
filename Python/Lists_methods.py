# -------------------------------------------------------------------------------
# ------------------------- Lists methods -------------------------
# -------------------------------------------------------------------------------

# append() => method used to add a single element to the end of the list. It modifies the original list (it doesn’t return a new one).

print("append() method")

names_1 = ["Mohamed", "Ahmed", "Ibrahim"]
nums = [1, 2, 3]

print(f"This is a list of names: {names_1}")
print(f"This is a list of numbers: {nums}")

names_1.append("Alaa")
names_1.append(100)
names_1.append(150.20)
names_1.append(True)
names_1.append(nums)

print(f"This is the list after changes: {names_1}")
print(names_1[2])
print(names_1[6])
print(names_1[7])
print(names_1[7][2])

print("-------------------------------------------------------------------------------")

# extend() => method used to add multiple elements (from another iterable like a list, tuple, or string) to the end of the current list.

print("extend() method")

list_1 = [1, 2, 3, 4]
list_2 = ["A", "B", "C"]
list_3 = ["One", "Two"]

list_1.extend(list_2)
list_1.extend(list_3)

print(list_1)

print("-------------------------------------------------------------------------------")

# remove() => method used to delete the first occurrence of a specific value from a list.

print("remove() method")

list_4= [1, 2, 3, "Mohamed", True, "Mohamed", "Mohamed"]
list_4.remove("Mohamed")
print(list_4)

print("-------------------------------------------------------------------------------")

# sort() => method used to arrange the elements of a list in ascending or descending order.

print("sort() method")

list_5 = [1, 2, 100, 120, -10, 17, 29]
list_5.sort()
print(list_5)

list_6 = ["A", "Z", "C"]
list_6.sort(reverse=True)
print(list_6)

list_7 = ["Python", "AI", "Machine", "Data"]
list_7.sort(key=len)
print(list_7)

print("-------------------------------------------------------------------------------")

# reverse() => method is used to reverse the order of the elements in a list.

print("reverse() method")

list_8 = [10, 9, 80, 100, "Mohamed", 100]
list_8.reverse()
print(list_8)

print("-------------------------------------------------------------------------------")

# clear() => method is used to remove all items from a list, making it empty.

print("clear() method")

list_9 = [1, 2, 3, 4]
list_9.clear()
print(list_9)

print("-------------------------------------------------------------------------------")

# copy() => method creates a shallow copy of a list, that means it makes a new list with the same elements as the original.

print("copy() method")

list_10 = [1, 2, 3, 4]
list_11 = list_10.copy()

print(f"This is the main list: {list_10}")
print(f"This is a copy of main list: {list_11}")

list_10.append(5)

print(f"This is the main list: {list_10}")
print(f"This is a copy of main list: {list_11}")

print("-------------------------------------------------------------------------------")

# count() => method returns the number of times a specified value appears in a list.

print("count() method")

list_12 = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(list_12.count(1))

print("-------------------------------------------------------------------------------")

# index() => method returns the position (index number) of the first occurrence of a specified value in a list.

print("index() method")

list_13 = ["Osama", "Ahmed", "Sayed", "Ramy", "Ahmed", "Ramy"]
print(list_13.index("Ramy")) # 3 => The index of the first Ramy.

list_14 = [10, 20, 30, 20, 40, 20]
print(list_14.index(20, 2, 5)) # 3
# print(list_14.index(20, 4, 5)) # Error
print(list_14.index(20, 4, )) # 5

print("-------------------------------------------------------------------------------")

# insert() => method is used to add an element to a specific position (index) in a list.

print("insert() method")

list_15 = [1, 2, 3, 4, 5, "A", "B"]
list_15.insert(0, "Mohamed")
list_15.insert(-1, "Ibrahim")

print(list_15)

print("-------------------------------------------------------------------------------")

# pop() => method is used to remove and return an element from a specific index in a list.

print("pop() method")

list_16 = [1, 2, 3, 4, 5, "A", "B"]
print(list_16.pop(-3))
print(list_16)

print(list_16.pop(5))
print(list_16)