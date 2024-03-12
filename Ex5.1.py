print("=" * 35)
print(7 * " ", "10 TERMOS DE UMA PA")
print("=" * 35)

pri = int(input("Primeiro Termo: "))
raz = int(input("Razão: "))

print(f"{pri} ->", end=" ")
for c in range(0, 9):
    pri = pri + raz
    print(f"{pri}", end=" → ")
print("ACABOU")
