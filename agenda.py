import datetime
AGENDA = {} #Váriavel maiscula para declarar como global

def mostrarContato():
    for contato in AGENDA:
        buscarContato(contato)
        print("----------------------")

def buscarContato(contato):
    try:
        print("contato: ", contato)
        print("Setor: ", AGENDA[contato]['setor'])
        print("Ramal: ", AGENDA[contato]['ramal'])
        print("Tempo: ", AGENDA[contato]['tempo'])
        print("IP: ", AGENDA[contato]['ipMaquina'])
        print("Descrição: ", AGENDA[contato]['descProblema'])
    except KeyError as error:
        print("Contato inexistente")
        print(error)



def inserirContato(contato,ramal,setor,tempo,ipMaquina,descProblema):
    AGENDA[contato] = {
        'ramal': ramal,
        'tempo': tempo,
        'setor': setor,
        'ipMaquina': ipMaquina,
        'descProblema': descProblema,
    }
    print()
    print("Contato {} Incluido com sucesso".format(contato))

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(linha.split(','))
    except FileNotFoundError:
        print("Arquivo não encontrado")

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print('Contato {} excluido com sucesso'.format(contato))
    except KeyError:
        print("Contato não encontrado")
    except Exception as error:
        print("Um erro ocorreu")
        print(error)
    except(FileNotFoundError):
        print('Arquivo não encontrado')

def main():
    print("1 - Mostrar Contato ")
    print("2 - Buscar Contato ")
    print("3 - Inserir Contato ")
    print("0 - Para fechar o Programa")

while True:
    main()
    opcao = input("Digite uma opcao " )

    if(opcao == "1"):
        mostrarContato()

    elif(opcao == "2"):
        try:
            contato = input("Digite o contato do usuário: ")
            buscarContato(contato)

        except Exception as error:
            print("Erro ao consultar o usuário")
            print(error)
    elif(opcao == "3"):

        contato = input("Digite o nome do usuário: ")
        ramal = input("Ramal do usuário: ")
        setor = input("Setor: ")
        tempo = input("Tempo estimado em minutos: ")
        ipMaquina = input("IP da máquina: ")
        descProblema = input("Descrição do problema: ")
        inserirContato(contato,ramal,setor,tempo,ipMaquina,descProblema)
        try:
            current_date = datetime.date.today()
            str_current_datetime = str(current_date)
            file_name = str_current_datetime +".csv"
            with open(file_name, "a") as arquivo:
                 for contato in AGENDA:
                     ramal = AGENDA[contato]['ramal']
                     setor = AGENDA[contato]['setor']
                     tempo = AGENDA[contato]['tempo']
                     ipMaquina = AGENDA[contato]['ipMaquina']
                     descProblema = AGENDA[contato]['descProblema']
                     arquivo.write("{},{},{},{},{},{}\n".format(contato,ramal,setor,tempo,ipMaquina,descProblema))
        except Exception as error:
             print("Erro ao exportar os contatos")
             print(error)

    elif(opcao == "0"):
        print("Fechando o programa")
        break
    else:
        ("Opção inexistente")
