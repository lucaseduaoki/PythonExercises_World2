sex = str(input("Informe o seu sexo (M/F): ")).strip().lower()[0]
while sex not in "MmFf":
    print("\nOpção inválida!!!")
    sex = str(input("Tente novamente (M/F): ")).strip().lower()[0]
if sex == "m":
    print("\nVocê é do sexo masculino")
elif sex == "f":
    print("\nVocê é do sexo feminino")
