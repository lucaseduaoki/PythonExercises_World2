import random
import time
print("Olá jogador!")
print("Vamos começar a brincar?")
print("Suas opções:")
print('''[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
escolha = int(input("É a sua vez, qual a sua escolha? "))
if escolha not in [0, 1, 2]:
    print("Opção invalida, tente entre os números entre 0, 1, e 2")
else:
    opcoes = ["pedra", "papel", "tesoura"]
    computador = random.randint(0, 2)
print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ")
print("=" *40)
print(f"Computador escolheu {opcoes[computador]}")
print(f"Você escolheu {opcoes[escolha]}")
print("="*40)
if (escolha == 0 and computador == 2) or (escolha == 1 and computador == 0) or (escolha == 2 and computador == 1):
    print("Você venceu o computador!")
elif escolha == computador:
    print("Vocês ficaram empatados!")
else:
    print("Você perdeu para o computador, seja mais esperto da próxima!")
