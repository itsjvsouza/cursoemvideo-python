#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas
#- Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
nome_split = nome.split()

print('Nome com letras maiúsculas: ', nome.upper())
print('\nNome com letras maiúsculas: ', nome.lower())
print('\nQuantidade de letras no nome: ', len(nome) - nome.count(' '))
print('\nNúmero de letras no primeiro nome: ', len(nome_split[0]))
