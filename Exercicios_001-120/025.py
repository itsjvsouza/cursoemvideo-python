#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite o nome: ').strip()

print(f'O nome "{nome}" tem Silva? {'SILVA' in nome.upper()}')
