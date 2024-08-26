op = "1"
while op != "0" :
    print('''
 ---Escolha uma opção---
    1--Soma
    2-Subtração
    3-Multiplicação
    4-Divisão
    5-Elevar ao quadrado
    0-Sair
    ''')
    op = input("Escolha um opção: ")
    if op == "1" :
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero 2: "))
        print(f"{n1} + {n2} = {n1+n2}")
    elif op == "2" :
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero 2: "))
        print(f"{n1} - {n2} = {n1-n2}")
    elif op == "3" :
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero 2: "))
        print(f"{n1} x {n2} = {n1*n2}")
    elif op == "4" :
        n1 = int(input("Digite um numero: "))
        n2 = int(input("Digite um numero 2: "))
        if n2 == 0:
            print("Não exite divisão é por 0")
        print(f"{n1} : {n2} = {n1/n2}")
    elif op == "5" :
        n1 = int(input("Digite um numero: "))
        print(f"{n1} x {n1} = {n1*n1}")
    elif op != "0":
        print("Dados inválidos")