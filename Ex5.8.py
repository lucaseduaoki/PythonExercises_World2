import random

print("-=-" * 10)
print(5*" ", "JOGO DA ADIVINHAÇÃO")
print("-=-" * 10)

Tentativas = 0
print("\nTente adivinhar o número que o computador está pensando...")
number = int(input("\nDigite um número de 0 a 10: "))
Tentativas += 1

sort = random.randint(0,10)

while number != sort:
    print(f"Ah, que pena, você errou. O computador pensou no {sort}.")
    number = int(input("\nInforme outro número de 0 a 10: "))
    Tentativas += 1
    sort = random.randint(0, 10)
print("Parabéns, você venceu o jogo!!!")
print(f"Foram necessárias {Tentativas} tentativas para acertar.")
