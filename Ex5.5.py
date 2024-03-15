maior = 0
menor = 0
for c in range(1,6):
    peso = float(input(f'Qual o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f"\nO maior peso é {maior}Kg.")
print(f"\nO menor peso é {menor}Kg.")
