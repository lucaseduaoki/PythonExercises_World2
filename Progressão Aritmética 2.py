print("Gerador de PA")
print("=-=-" *4)

pri = int(input("Primeiro Termo: "))
raz = int(input("Razão da PA: "))

c = 0
while c < 11:
    pri = pri + raz
    print(f"{pri}", end=" → ")
    c += 1
print("PAUSA")
termos = int(input("Quantos termos quer mostrar mais"))
