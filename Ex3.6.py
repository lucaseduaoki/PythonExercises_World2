print('-=-' * 10)
print('EMPRÉSTIMOS BANCÁRIOS BRASIL')
print('-=-' * 10)
name = str(input('Informe seu nome por favor: '))
valor = float(input(f'{name}, qual o valor da casa que você deseja comprar? R$'))
sal = float(input('O(A) senhor(a) poderia nos informar o valor de sua renda mensal: R$'))
tempo = int(input('Em quantos anos o(a) senhor(a) pretende quitar o financiamento: '))

prestacao = valor/(tempo*12)

print('Para pagar uma casa de R${:.2f} em {} anos, a prestação seria de R${:.2f}'.format(valor, tempo, prestacao))

if prestacao > sal*0.3:
    print(f'Infelizmente, o valor da prestação excedeu 30% do seu salário\nEMPRÉSTIMO NEGADO!')
elif prestacao < sal*0.3:
    print(f'O valor da prestação não excedeu 30% do seu salário\nPARABÉNS, EMPRÉSTIMO APROVADO!')
