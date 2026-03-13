#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('\nDigite o segundo número: '))
n3 = float(input('\nDigite o terceiro número: '))

if n1 > n2 and n1 > n3:
    
    if n2 < n3:
        print(f'O maior é {n1} e o menor é {n2}.')
    
    else:
        print(f'O maior é {n1} e o menor é {n3}.')

elif n2 > n1 and n2 > n3:

    if n1 < n3:
        print(f'O maior é {n2} e o menor é {n1}.')

    else:
        print(f'O maior é {n2} e o menor é {n3}.')

else:

    if n1 < n2:
        print(f'O maior é {n3} e o menor é {n1}.')

    else:
        print(f'O maior é {n3} e o menor é {n2}.')
