nome = input("seu nome: ")
idade = int(input("sua idade: "))
if idade < 16:
    i = "você não esta apto a votar"
else :
    i = "você esta apto a votar"
print(f"{nome} {i}")