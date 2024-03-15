frase = str(input("Digite uma frase: ")).upper()
palavras = frase.split()
junto = "".join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print(frase)
print(inverso)
if junto == inverso:
    print('TEMOS UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
