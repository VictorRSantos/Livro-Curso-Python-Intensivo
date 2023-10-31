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
print()

print("===[Tabulações ou Quebra de linha]===")

print("Languages:\nPython\n\tC#\n\tJavascript")
print()

print("===[Removendo espaços em branco]===")

favorite_language = 'python '
favorite_language = favorite_language.rstrip()#rstrip - remove espaço em branco do lado direito
print(favorite_language)

favorite_language = ' python'
favorite_language = favorite_language.lstrip()#rstrip - remove espaço em branco do lado esquerdo
print(favorite_language)

favorite_language = ' python '
favorite_language = favorite_language.strip()#rstrip - remove espaço em ambos os lados
print(favorite_language)

print()
