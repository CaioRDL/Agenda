AGENDA = {}

AGENDA['lucas'] = {
    "tel": "9825-6996",
    "email": 'lucas@gmail.com',
    "end": 'Av 1',
}

AGENDA['luana'] = {
    "tel": "9825-8596",
    "email": 'luana69@gmail.com',
    "end": 'Av 2',
}
def mostrarContatos():
    for contato in AGENDA:
        buscarContatos(contato)
        print("-------------")

def buscarContatos(contato):
    print("Nome: ", contato)
    print("Tel: ", AGENDA[contato]['tel'])
    print("Email:", AGENDA[contato]["email"])
    print("End: ", AGENDA[contato]['end'])
    print(AGENDA[contato])
    print("----------------------------------------")

def incluirEditarContatos(contato, tel,email,end):
    AGENDA[contato] = {
    "tel": tel,
    "email": email,
    "end": end,


    }
    print("Sucesso {} adicionado/editado com sucesso! ".format(contato) )
    print()
    # {} .formate() é para adicionar uma várivel
    #Dentro do local que você adicionou a chave
    #Será adicionado uma várivel, de acordo com as quantidade de chaves adicionada.
    #EX: Adicione a {} no texto do print e passe a função apos finalizar o fechamento das aspas
    # .format(var1),(var2),(var3)

def excluirContato(contato):

    AGENDA.pop(contato)
    print("Contato {} excluido com sucesso".format(contato))
    print()

def menu():
    print("----------------------------------------")
    print("1 - Mostrar todos os contatos na agenda")
    print("2 - Buscar todos os contatos na agenda")
    print("3 - Incluir editar contatos na agenda")
    print("4 - Editar contatos na agenda")
    print("5 - Excluir os contatos na agenda")
    print("0 - Fechar agenda")
    print("----------------------------------------")
while True:
    menu()

    opcao = input("Qual opção? ")
    if (opcao == "1"):
        mostrarContatos()
    elif (opcao == "2"):
        contato = input("Digite o nome do contato: ")
        buscarContatos(contato)
    elif (opcao == "3" or opcao == "4"):
        contato = input("Digite o nome do contato: ")
        tel = input("Digite o Telefone: ")
        email = input("Digite o email: ")
        end = input("Digite o endereço: ")
        incluirEditarContatos(contato, tel, email, end)
        mostrarContatos()
    elif (opcao == "5"):
        contato = input("Digite o nome do contato? ")
        excluirContato(contato)
    elif (opcao == "0"):
        print("Fechando o programa")
        break
    else:
        print("Opção {} invalida".format(opcao))