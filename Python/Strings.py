# -------------------------------------------------------------------------------
# ------------------------- Strings -------------------------
# -------------------------------------------------------------------------------
# String => Any sequence of characters (Any thing print between '' or "")
# -------------------------------------------------------------------------------
# Strings indexing & slicing
# [1] All data in python is object
# [2] Object contain elements
# [3] Every element has its own index
# [4] Python use zero based indexing ( Index start from zero )
# [5] Use square brackets to access element
# [6] Enable accessing parts of strings, tuples or lists
# -------------------------------------------------------------------------------

StringOne = 'Single Quote'
StringTwo = "Double Quotes"

print(StringOne)
print(StringTwo)

StringThree = 'Single Quote "Double Quote"'
StringFour = "Double Quotes 'Single Quote'"

print(StringThree)
print(StringFour)

# To print multiple lines we use ''' ''' and """ """
StringFive = '''First
Second 'Single Quote' "Double Quote"
Third'''

StringSix = """First
Second "Double Quote" \\\ 'Single Quote'
Third"""

print(StringFive)
print(StringSix)

print("-------------------------------------------------------------------------------")

# Indexing ( Access single item )

myString = "I Love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First character from end
print(myString[-6])  # Index -6 => 6th character from end

# Slicing ( Access multiple sequence items )
# [Start:End] End not included
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If start is not assigned, it will start from 0 (I Love Pyt)
print(myString[5:])  # If end is not assigned, it will go to the end (e Python)
print(myString[:])  # Full data

print(myString[0::1])  # Full data
print(myString[::1])  # Full data 

print(myString[::2])  # (ILv yhn)
print(myString[::3])  # (Io tn)

print("-------------------------------------------------------------------------------")

# -------------------------------------------------------------------------------
# --------------------------- Strings Methods ---------------------------
# -------------------------------------------------------------------------------

# len() => It is a function used to get the number of items in an object.

name = "My name is mohamed"
print(len(name))

print("-------------------------------------------------------------------------------")

# strip() => method used to remove whitespace (or specific characters) from both ends of a string.
# rstrip() => method used to remove whitespace (or specific characters) from the right end.
# lstrip() => method used to remove whitespace (or specific characters) from the left end.

print("strip(), rstrip() and lstrip() methods")

name = "    My name is mohamed    "
print(name.strip())
print(name.rstrip())
print(name.lstrip())

name = "#####My name is mohamed####"
print(name.strip("#"))
print(name.rstrip("#"))
print(name.lstrip("#"))

name = "@#@#@#My name is mohamed@#@#@#"
print(name.strip("@#"))
print(name.rstrip("@#"))
print(name.lstrip("@#"))

print("-------------------------------------------------------------------------------")

# title() => method used to capitalize the first letter of every word in a string.

print("title() method")

b = "I love lInear alGebra And Calculas and python"
print(b.title())

print("-------------------------------------------------------------------------------")

# capitalize() => method used to make the first character of a string uppercase and the rest lowercase.

print("capitalize() method")


b = "I Love Linear Algebra and Calculas and Python"
print(b.capitalize())

print("-------------------------------------------------------------------------------")

# zfill() => method used to pad a string with zeros (0) on the left until it reaches a specified length.

print("zfill() method")

c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

print("-------------------------------------------------------------------------------")

# upper() => method used to convert all lowercase letters in a string to uppercase.

print("upper() method")

g = "mohamed"

print(g.upper())

print("-------------------------------------------------------------------------------")

# lower() => method used to convert all uppercase letters in a string to lowercase.

print("lower() method")

h = "mohamed"

print(h.lower())

print("-------------------------------------------------------------------------------")

# split() => method splits a string from the left (the beginning) into a list of substrings. 
# rsplit() => method works exactly like split(), but it splits from the right side.

print("split() and rsplit() methods")

a = "I Love Linear Algebra and Calculas and python"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3))

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 2))
print(d.rsplit("-", 3))

print("-------------------------------------------------------------------------------")

# center() => method used to align a string in the center of a given width by padding it with spaces (or another character) on both sides.

print("center() method")

e = "mohamed"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

print("-------------------------------------------------------------------------------")

# count() => method used to count how many times a specific substring or character appears in a string.

print("count() method")

f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25))  # Only One PHP Word

print("-------------------------------------------------------------------------------")

# swapcase() => method used to swap the case of every letter in a string

print("swapcase() method")

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

print("-------------------------------------------------------------------------------")

# startswith() => method used to check whether a string begins with a specific substring. (Returns boolean value)

print("startswith() method")

i = "My name is Mohamed"
print(i.startswith("M"))
print(i.startswith("My"))
print(i.startswith("my"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

print("-------------------------------------------------------------------------------")

# endswith() => method used to check whether a string ends with a specific substring. (Returns boolean value)

print("endswith() method")

j = "My name is Mohamed"
print(j.endswith("d"))
print(j.endswith("Mohamed"))
print(j.endswith("mohamed"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

print("-------------------------------------------------------------------------------")

# index(SubString, Start, End) => method is used to find the position (index) of the first occurrence of a given substring inside a string.
# If the substring is not found, it raises Error.

# find(SubString, Start, End) => method is used to search for a substring within a string and return the index of its first occurrence.
# If the substring is not found, it returns -1.

print("index() method")

name = "My name is Mohamed"
# print(name.index("M"))  # Index Number 11
# print(name.index("i", 0, 10))  # Index Number 8
# print(name.index("M", 0, 5))  # Error

print("index() method")

name = "My name is Mohamed"
print(name.find("M"))  # Index Number 11
print(name.find("i", 0, 10))  # Index Number 8
print(name.find("M", 0, 5))  # -1

print("-------------------------------------------------------------------------------")

# rjust(Width, Fill char) => method is used to right-align a string in a field of a specified width, padding it on the left with a chosen character (default is a space).
# ljust(Width, Fill char) => method is used to left-align a string within a specified width, padding it on the right with a chosen character (default is a space).

print("rjust() and ljust() method")

name = "Mohamed"
print(name.rjust(10))
print(name.rjust(10, "#"))

name = "Mohamed"
print(name.ljust(10))
print(name.ljust(10, "#"))

print("-------------------------------------------------------------------------------")

# splitlines() => method is used to split a string into a list of lines, breaking at line boundaries (like \n).

print("splitlines() method")

lines = """First Line
Second Line
Third Line"""

print(lines.splitlines())

lines = "First Line\nSecond Line\nThird Line"

print(lines.splitlines())

print("-------------------------------------------------------------------------------")

# expandtabs() => method replaces tab characters (\t) in a string with spaces. You can also specify how many spaces each tab should represent.
print("expandtabs() method")

g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(5))

print("-------------------------------------------------------------------------------")

# Methods that start with is are boolean-check methods, they return either True or False depending on some condition.

print("is before methods")

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(three.isspace())
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

u = "AaaaaBbbbbb"
z = "AaaaaBbbbbb111"
print(u.isalnum())
print(z.isalnum())

print("-------------------------------------------------------------------------------")

# replace(Old Value, New Value, Count) => method returns a new string where all occurrences of a specified substring are replaced with another substring.

print("replace() method")

a = "Hello One Two Three One One"
print(a.replace("One", "1"))
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

print("-------------------------------------------------------------------------------")

# join(Iterable) => method is used to combine (concatenate) elements of an iterable (like a list or tuple) into a single string, with a specific separator between each element.

print("join() method")

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(", ".join(myList)))

print("-------------------------------------------------------------------------------")
