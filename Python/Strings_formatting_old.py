# -------------------------------------------------------------------------------
# ------------------------- Strings formatting old way -------------------------
# -------------------------------------------------------------------------------

name = "Mohamed"
age = 22
rank = 7

print("My name is: " + name)
# print("My name is: " + name + " and my age is: " + age)  # Type Error (Cannot concatinate string with number)

print("My name is: %s" % "Mohamed")
print("My name is: %s" % name)
print("My name is: %s and my age is: %d" % (name, age))
print("My name is: %s and my age is: %d and my rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

name = "Mohamed"
language = "Python"
years = 7

print("My name is %s I am %s developer with %d years exp" % (name, language, years))

# Control floating point number

num = 10.9832
print("Number is: %d" % num)
print("Number is: %f" % num)
print("Number is: %.2f" % num)

# Truncate String

LongString = "Hello, My name is Mohamed Ibrahim Abdelzaher Gazia"
print("Message is: %s" % LongString)
print("Message is: %.5s" % LongString)