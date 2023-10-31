"""
FAÇA VOCÊ MESMO
----------------
2.3 – Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa.
Sua mensagem deve ser simples, como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.

2.4 - Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma pessoa em uma variável e então apresente o nome dessa pessoa em letras minúsculas,
em e somente com a primeira letra maiúscula.

2.5 – Citação famosa: Encontre uma citação de uma pessoa famosa que você admire. Exiba a citação e o nome do autor. Sua saída deverá ter a aparência
a seguir, incluindo as aspas: Albert Einstein certa vez disse: “Uma pessoa que nunca cometeu um erro jamais tentou nada novo.”

2.6 – Citação famosa 2: Repita o Exercício 2.5, porém, desta vez, armazene o nome da pessoa famosa em uma variável chamada famous_person.
Em seguida, componha sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua mensagem.

2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma
pessoa e inclua alguns caracteres em branco no início e no final do nome.
Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três
funções de remoção de espaços: lstrip(), rstrip() e strip().

"""

print("===[2.3 - Mensagem pessoal]===")

nome = "Eric"
print("Alô " + nome + ", você gostaria de aprender um pouco de Python hoje?")

print()

print("===[2.4 - Letras maiúsculas e minúsculas em nomes]===")

nome = "eric"
print("Letras maiúscula =", nome.upper())
print("Somente a primeira Letra maiúscula =", nome.title())

print()

print("===[2.5 - Citação famosa]===")

nome_autor = "Albert Einstein"
citacao = "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."
print(nome_autor + " certa vez disse: " + citacao)
print()

print("===[2.6 - Citação famosa 2]===")

famous_person = "Albert Einstein"
citacao = "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."
message = famous_person + " certa vez disse: " + citacao
print(message)
print()


print("===[2.7 - Removendo caracteres em branco de nomes]===")

nome1 = " Pedro"
nome2 = "Antonio "
nome3 = " Jessica "

print("Nomes : " + nome1 + ", " + nome2 + " e " + nome3)
print("Nomes \n\t"  + nome1.lstrip() + "\n\t" + nome2.rstrip() + "\n\t" + nome3.strip())
print()