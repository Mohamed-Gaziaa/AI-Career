# -------------------------------------------------------------------------------
# ------------------------- Dictionary -------------------------
# -------------------------------------------------------------------------------
# [1] Dict items are enclosed in curly braces. "{}"
# [2] Dict items are contains key : value.
# [3] Dict key need to be immutable => (Number, String, Tuple) list not allowed.
# [4] Dict value can have any data types.
# [5] Dict key need to be unique.
# [6] Dict is not ordered you access its element with key.
# -------------------------------------------------------------------------------

# Dictionary

user = {
  "name": "Mohamed",
  "age": 22,
  "country": "Egypt",
  "skills": ["Python", "Git&Github ", "Pandas"],
  "rating": 7.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

print("-" * 79)

# Two-Dimensional Dictionary

languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

print("-" * 79)

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

print("-" * 79)

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)