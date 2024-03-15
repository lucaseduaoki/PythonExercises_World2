import time

print("-=-" * 10)
print(5*" ", "CALCULADORA MÁGICA")
print("-=-" * 10)

n1 = float(input("\nInforme um valor: "))
n2 = float(input("Informe outro valor: "))

option = 0

while option != 5:
    print("\nMENU DE FUNÇÕES")
    print("""[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior e Menor número
[ 4 ] Novos números
[ 5 ] SAIR""")
    option = int(input("\nQual opção deseja: "))
    if option == 1:
        print(f"\nA soma dos dois números é {n1 + n2}")
    elif option == 2:
        print(f"\nO produto dos dois números é {n1 * n2}")
    elif option == 3:
        if n1 > n2:
            print(f"O maior número é o {n1} e o menor é o {n2}")
        else:
            print(f"O maior número é o {n2} e o menor é o {n1}")
    elif option == 4:
        n1 = float(input("\nInforme o novo valor: "))
        n2 = float(input("Informe outro novo valor: "))
    elif option <= 0 or option > 5:
        print("Opção inválida. Tente novamente!")
    elif option == 5:
        print("Saindo...")
        time.sleep(3)
    print("-=-" * 10)
print("FIM DO PROGRAMA")
