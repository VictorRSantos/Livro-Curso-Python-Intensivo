"""
Métodos

title() = input: ada lovelace - output: Ada Lovelace
upper() = input: ada lovelace - output: ADA LOVELACE
lower() = input: ADA Lovelace - output: ada lovelace

"""

print("===[String]===")

name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())
print()

print("===[Combinado ou Concatenando strings]===")

first_name = "Chimbinha"
last_name = "da silva"
full_name = first_name + " " + last_name
message = "Hello, " + full_name.title() + "!"
print(message)