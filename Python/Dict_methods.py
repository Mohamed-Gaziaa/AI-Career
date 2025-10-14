# -------------------------------------------------------------------------------
# ------------------------- Dictionary methods -------------------------
# -------------------------------------------------------------------------------

# clear() => Removes all items from the dictionary, leaving it empty.

print("clear() method")

user = {
  "name": "Mohamed"
}
print(user)
user.clear()
print(f"The dict after clear methode: {user}")

print("=" * 50)

# update() => Adds key-value pairs from another dictionary or an iterable of key-value pairs to the current dictionary, updating existing keys if they already exist.

print("update() method")

member = {
  "name": "Mohamed"
}
print(member)
member["age"] = 22
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

# copy() => Returns a shallow copy of the dictionary.

print("copy() method")

main = {
  "name": "Mohamed"
}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

print("=" * 50)

# keys() => Returns a view object that displays a list of all the keys in the dictionary. 
# values() => Returns a view object that displays a list of all the values in the dictionary.

print("keys() and values() methods")

main = {
  "name": "Mohamed",
  "skills": "Fighting"
}

print(main.keys())
print(main.values())

print("=" * 50)

# setdefault() => Returns the value of a specified key. If the key does not exist, it inserts the key with a specified default value and returns that value.

print("setdefault() method")

user = {
  "name": "Mohamed"
}
print(user)
print(user.setdefault("age", 22))
print(user)

print("=" * 50)

# popitem() => Removes and returns the last inserted key-value pair from the dictionary as a tuple.

print("popitem() method")

member = {
  "name": "Mohamed",
  "skill": "PS4"
}
print(member)
member.update({"age": 22})
print(member.popitem())

print("=" * 50)

# items() => Returns a view object that displays a list of the dictionary’s key-value pairs as tuples.

print("items() method")

view = {
  "name": "Mohamed",
  "skill": "XBox"
}

allItems = view.items()
print(view)
view["age"] = 22

print(allItems)

print("=" * 50)

# fromkeys() => Creates a new dictionary with keys from an iterable and assigns all of them a specified value.

print("fromkeys() method")

a = ('MyKeyOne', 'MyKeyTwo', 'MyKeyThree')
b = ("X", "Y")

print(dict.fromkeys(a, b))

print("=" * 50)
