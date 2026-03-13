# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite o nome completo: ').split()
#qnt_n = len(nome)

print(f'\nO primeiro nome é: {nome[0]}')
print(f'\nO último nome é: {nome[len(nome) - 1]}')
