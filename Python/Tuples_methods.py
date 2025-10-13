# -------------------------------------------------------------------------------
# ------------------------- Tuples methods -------------------------
# -------------------------------------------------------------------------------

# Tuple with one element

Tuple1 = ("Mohamed",)
Tuple2 = "Mohamed",

print(Tuple1)
print(Tuple2)

print(type(Tuple1))
print(type(Tuple2))

print(len(Tuple1))
print(len(Tuple2))

print("-------------------------------------------------------------------------------")

# Tuple Concatenation

Tuple3 = (1, 2, 3, 4)
Tuple4 = (5, 6)

Tuple5 = Tuple3 + Tuple4
Tuple6 = Tuple3 + ("A", "B", True) + Tuple4

print(Tuple5)
print(Tuple6)

print("-------------------------------------------------------------------------------")

# Tuple, List, String Repeat (*)

aString = "Mohamed"
aList = [1, 2]
aTuple = ("A", "B")

print(aString * 6)
print(aList * 6)
print(aTuple * 6)

print("-------------------------------------------------------------------------------")

# Methods => count()

print("count() method")

Tuple7 = (1, 8, 7, 8, 2, 6, 5, 8)
print(Tuple7.count(8))

print("-------------------------------------------------------------------------------")

# Methods => index()

print("index() method")

Tuple8 = (1, 3, 7, 8, 2, 6, 5)
print("The position of index is: {:d}".format(Tuple8.index(7)))
print(f"The position of index is: {Tuple8.index(2)}")

print("-------------------------------------------------------------------------------")

# Tuple Destruct

Tuple9 = ("A", "B", 4, "C")

x, y, _, z = Tuple9 # number of objects = number of elements in tuple (_ means skip 4)

print(f"The tuple elements: {x}, {y}, {z}")

Tuple10 = ("A", "B", "C", "D", 5, 10)

_, x, _, y, z, a = Tuple10 # _ means skip A and C

print(f"The tuple elements: {x}, {y}, {z}, {a}")