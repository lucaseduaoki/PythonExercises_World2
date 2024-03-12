idade = int(input("Informe sua idade: "))
print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Classificação: MIRIM")
if idade >= 10 and idade <= 14:
    print("Classificação: INFANTIL")
if idade >= 15 and idade <= 19:
    print("Classificação: JÚNIOR")
if idade >= 20 and idade <= 25:
    print("Classificação: SÊNIOR")
if idade > 25:
    print("Classificação: MASTER")
