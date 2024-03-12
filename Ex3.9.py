import datetime
ano = int(input("Em que ano você nasceu: "))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade < 18:
    print(f"Ainda faltam {18 - idade} anos para seu alistamento")
    print(f"Seu alistamento será feito em {ano + 18}")
elif idade == 18:
    print(f"Você já está na idade exata para se alistar")
elif idade > 18:
    print(f"Quem nasceu em {ano} tem {idade} em {ano_atual}")
    print(f"Você já devia ter se alistado há {idade - 18} ano(s).")
    print(f"Seu alistamento foi em {ano + 18 }")
