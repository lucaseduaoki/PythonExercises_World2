somaidade = 0
media = 0
count = 0
maior = 0
nomevelho = ' '

for c in range(1,5):
    print('--' * 3, f'{c}ª PESSOA','--' * 3)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    somaidade += idade
    if idade < 20 and sexo == "f":
        count += 1
    if c == 1 and sexo == "m":
        maior = idade
        nomevelho = nome
    else:
        if idade > maior and sexo == "m":
            maior = idade
            nomevelho = nome

media = somaidade / 4

print(f'\nA média de idade do grupo é {media} ')
print(f'A idade do homem mais velho é {maior} e seu nome é {nomevelho}.')
print(f'Ao todo são {count} mulheres com menos de 20 anos.')
