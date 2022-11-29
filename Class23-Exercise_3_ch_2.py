# Take 2 comma seperated inputs from user.
# 1.) user's name
# 2.) asingle character

# Output 2 print Lines
# 1.) user's name length
# 2.) count the character that user inputs (Bonus case insensitive counts.)

# SOLUTIONS:-

name, character = input("enter your name and character").split(",")
print(f"length of your name is {len(name)}")
print(f"Character count is : {name.lower().count(character.lower())}")