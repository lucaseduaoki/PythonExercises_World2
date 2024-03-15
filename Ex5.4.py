import datetime
atual = datetime.date.today().year
count = 0
for c in range(1,8):
    nascimento = int(input(f"Em que ano a {c}ª pessoa nasceu: "))
    idade = atual - nascimento
    if idade >= 18:
        count += 1

print(f'\nAo todo tivemos {count} pessoas no grupo da maioridade.')
print(f'E também tivemos {c - count} pessoas menores de idade.')
