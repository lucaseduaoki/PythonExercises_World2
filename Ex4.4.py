print("=" * 10, end="")
print(" LOJAS AOKI ", end="")
print("=" * 10)
preco = 0
valor = float(input("Preço das compras: R$"))
print('FORMAS DE PAGAMENTO')
print("[ 1 ] à vista dinheiro ou cheque\n"
      "[ 2 ] à vista cartão\n"
      "[ 3 ] 2x no cartão\n"
      "[ 4 ] 3x ou mais no cartão\n")
opt = int(input("Qual a opção: "))


if opt == 1:
    preco = valor - (valor * 0.10)
    print(f"Sua compra será feita à vista no cartão/cheque no valor de R${valor:.2f} com desconto de 10%. ")
    print(f"Sua compra de R${valor:.2f} vai custar R${preco:.2f} no final.")
elif opt == 2:
    preco = valor - (valor * 0.05)
    print(f"Sua compra será feita à vista no cartão no valor de R${valor:.2f} com desconto de 5%. ")
    print(f"Sua compra de R${valor:.2f} vai custar R${preco:.2f} no final.")
elif opt == 3:
    print(f"Sua compra será parcelada em 2x de R${valor/2:.2f} sem juros.")
    print(f"Com essa opção o valor se mantém R${valor:.2f}.")
elif opt == 4:
    parcela = int(input("Quantas parcelas: "))
    preco = valor + (valor * 0.20)
    print(f"Sua compra será parcelada em {parcela}x de R${valor/parcela:.2f} COM JUROS.")
    print(f"Sua compra de R${valor:.2f} vai custar R${preco:.2f} no final.")

