soma = count = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c % 2 != 0:
            soma += c
            count += 1
print(f"A soma de todos os {count} valores solicitados é {soma}")
