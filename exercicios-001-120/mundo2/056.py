soma = 0
mulheres_menos_20 = 0
idade_mais_velho = 0
mais_velho = ""

for i in range(4):
    nome = input(f"Digite o nome da {i + 1}° pessoa: ")
    sexo = input(f"Digite o sexo da {i + 1}° pessoa (M/F): ").lower()
    idade = int(input(f"Digite a idade da {i + 1}° pessoa: "))

    soma += idade

    if sexo == "f" and idade < 20:
        mulheres_menos_20 += 1

    if sexo == "m" and idade > idade_mais_velho:
        idade_mais_velho = idade
        mais_velho = nome

media = soma / 4

print(f"\nA média de idade do grupo é: {media:.0f}")
print(f"O homem mais velho do grupo é: {mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")
