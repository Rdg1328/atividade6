menu = '''
Menu
0- Finalizar
1- Cadastrar 
2- Imprimir

Escolha: '''

registros = {}


def cadastrar():
    while True:
        try:
            nome = str(input("Digitar o nome do aluno: "))
            if len(nome) == 0:
                input("Digite um nome válido.")
            else:
                nota1 = float(input("Digite a nota 1: "))
                nota2 = float(input("Digite a nota 2: "))
                media = (nota1 + nota2) / 2
                registros[nome] = str(media)
                return ()
        except:
            input("Erro ocorreu.")
            break


def imprimir():
    print("Nome           Média")
    for nome, media in registros.items():
        print(f"{nome.ljust(13)}  {media.ljust(1)}")


escolha = 0
while True:
    escolha = input(menu)
    if escolha == '0':
        break
    elif escolha == '1':
        cadastrar()
    elif escolha == '2':
        imprimir()
    else:
        input('Opção inválida! [Enter]')
