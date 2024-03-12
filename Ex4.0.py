n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1+n2)/2
print(f"Tirando {n1} e {n2}, sua média será {media}")

if media < 5.0:
    print("O aluno está REPROVADO")
if media >= 5.0 and media <= 6.9:
    print("O aluno está RECUPERAÇÃO")
if media >= 7:
    print("O aluno está APROVADO")
