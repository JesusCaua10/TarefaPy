login = input("Seu login: ")
senha = input("Sua senha: ")
if login == "admin" and senha == "123" :
    print(f"Olá {login},seja bem-vindo")
else:
    print("login ou senha incorretos,tente novamente")