# -------------------------------------------------------------------------------
# ------------------------- Escape Sequences Characters -------------------------
# -------------------------------------------------------------------------------
# \b => Back space
# \newline => Escape new line + \
# \\ => Escape back slash.
# \' => Escape single quotes.
# \" => Escape double quotes.
# \n => Line feed.
# \r => Carriage return.
# \t => Horizontal tab.
# \xhh => Character Hex Value (Depend on ASCII table).
# -------------------------------------------------------------------------------

# Back space
print("Hello\bWorld")  # Will Remove o

# Escape new line + \
print("Hello \
I Love \
Python")

# Escape back slash
print("I Love Back Slash \\")

# Escape single quote
print('I Love Single Quote \'Test\' ')

# Escape double quotes
print("I Love Double Quotes \"Test\" ")

# Line feed
print("Hello World\nSecond Line")

# Carriage return
print("123456\rAbcde")
print("Abcdef\r12345")

# Horizontal tab
print("Hello\tPython")

# Character hex value
print("\x4F\x73")
print("\x4D\x6F")