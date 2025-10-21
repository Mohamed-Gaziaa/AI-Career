# -------------------------------------------------------------------------------
# -------------------------  Boolean -------------------------
# -------------------------------------------------------------------------------
# [1] In programming you need to know if your code output is True Or False.
# [2] Boolean values are the two constant objects False + True.
# -------------------------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True values

print(bool("Mohamed"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False values (Empty data)

print(bool(0))
print(bool(""))
print(bool(''))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))

# -------------------------------------------------------------------------------
# -------------------------  Boolean operators -------------------------
# -------------------------------------------------------------------------------
# and
# or
# not
# -------------------------------------------------------------------------------

age = 22
country = "Egypt"
rank = 7

print("=" * 50)

print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print("=" * 50)

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

print("=" * 50)

print(age > 16)  # True
print(not age > 16)  # Not True = False