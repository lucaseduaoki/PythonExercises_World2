soma = 0
for c in range(0,6):
    num = float(input("Digite um valor a ser somado: "))
    if num % 2 == 0:
        soma += num
print(f"A soma dos números pares foram {soma}")
