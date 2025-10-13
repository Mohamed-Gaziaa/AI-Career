# -------------------------------------------------------------------------------
# ------------------------- Strings formatting new way -------------------------
# -------------------------------------------------------------------------------

name = "Mohamed"
age = 22
rank = 7

print("My name is: {}".format("Mohamed"))
print("My name is: {}".format(name))
print("My name is: {} my age: {}".format(name, age))
print("My name is: {:s} age: {:d} & rank is: {:f}".format(name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

name = "Mohamed"
language = "Python"
years = 7

print("My name is {} I am {} developer with {:d} years exp".format(name, language, years))

# Control Floating Point Number

num = 10
print("Number is: {:d}".format(num))
print("Number is: {:f}".format(num))
print("Number is: {:.2f}".format(num))

# Truncate String

LongString = "Hello, My name is Mohamed Ibrahim Abdelzaher Gazia"
print("Message is {}".format(LongString))
print("Message is {:.5s}".format(LongString))
print("Message is {:.14s}".format(LongString))

# Format Money

myMoney = 500162350198

print("My money in Bank is: {:d}".format(myMoney))
print("My money in Bank is: {:_d}".format(myMoney))
print("My money in Bank is: {:,d}".format(myMoney))

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z))

# Format in Version 3.6+

myName = "Mohamed"
myAge = 22

print("My name is : {myName} and my age is : {myAge}")
print(f"My name is : {myName} and my age is : {myAge}")