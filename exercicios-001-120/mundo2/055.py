maior_peso = 0
menor_peso = 1000

for i in range(5):
    peso = int(input(f"Digite o peso da {i + 1}° pessoa: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso

print(f"\nO maior peso foi de {maior_peso}kg.")
print(f"O menor peso foi de {menor_peso}kg.")
