nome = input("Seu nome: ")
disc = input("Qual disciplina: ")
nota = float(input("Qual nota: "))
if nota >= 0 and nota <= 10:
    if nota >= 6 :
        print(f"{nome} está aprovado na disciplina de {disc} com nota {nota}")
    if nota < 6 and nota >= 5.5 :
        print(f"{nome} está aprovado na disciplina de {disc} com nota 6")
    if nota < 5.5 :
        print(f"{nome} está reprovado na disciplina de {disc} com nota {nota}")
else:
    print("nota invalida")
