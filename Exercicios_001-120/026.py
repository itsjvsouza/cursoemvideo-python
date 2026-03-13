#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Digite uma frase sem acentos: ').strip().lower()

print(f'\nO nome "{frase}" tem {frase.count('a')} letras "A"')
print(f'\nA primeira letra "A" aparece na posição: {frase.find('a')}')
print(f'\nA última letra "A" aparece na posição: {frase.rfind('a')}')
