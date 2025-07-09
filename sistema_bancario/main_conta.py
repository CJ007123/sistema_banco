from conta import *
from usuario import *
import json


def salvando_conta(dados):
    """
    Salva os dados das contas em um arquivo JSON.

    Parâmetros:
        dados (dict): Dicionário com os dados das contas.

    Retorno:
        None
    """
    with open('conta.json', 'w', encoding='utf-8') as arquivos:
        json.dump(dados, arquivos, indent=4, ensure_ascii=False)
        print('Conta salva com sucesso')


def carregar_conta():
    """
    Carrega os dados das contas de um arquivo JSON, exibindo os dados carregados.

    Retorno:
        dict: Dicionário com os dados das contas.
    """
    try:
        with open('conta.json', 'r', encoding='utf-8') as arquivos:
            carregar = json.load(arquivos)
            for conta in carregar.values():
                print(f'Agência: {conta["agencia"]}')
                print(f'Número: {conta["numero"]}')
                print(f'CPF: {conta["cpf"]}')
                print(f'Saldo: R${conta["saldo"]:.2f}\n')    
            return carregar  
    except FileNotFoundError:
        print('Conta não foi encontrada no arquivo')
        return {}


def menu_contas():
    """
    Exibe o menu interativo para gerenciamento de contas bancárias.

    Funcionalidades disponíveis:
        1 - Criar conta concorrente
        2 - Depositar em conta
        3 - Exibir dados da conta
        4 - Sacar de conta
        5 - Transferir entre contas
        6 - Exibir extrato
        7 - Carregar contas de arquivo
        0 - Salvar e sair
    """
    global contas

    while True:
        print("\n=== MENU DE CONTAS ===")
        print("1 - Criar conta concorrente")
        print("2 - Depositar em conta")
        print("3 - Exibir dados da conta")
        print("4 - Sacar de conta")
        print("5 - Transferir entre contas")
        print("6 - Exibir extrato")
        print("7 - Carregar contas salvas")
        print("0 - Voltar para o menu principal")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                cpf = input("Digite o CPF vinculado à conta: ")
                conta_concorrente(cpf)

            elif opcao == "2":
                conta_numero = input("Número da conta: ")
                valor = float(input("Valor do depósito: "))
                depositar_em_conta_concorrente(conta_numero, valor)

            elif opcao == "3":
                exibir_dados_da_conta()

            elif opcao == "4":
                conta_numero = input("Número da conta: ")
                valor = float(input("Valor do saque: "))
                saque_em_conta_concorrente(conta_numero, valor)

            elif opcao == "5":
                origem = input("Conta de origem: ")
                destino = input("Conta de destino: ")
                valor = float(input("Valor da transferência: "))
                transferencia(origem, destino, valor)

            elif opcao == "6":
                conta_numero = input("Número da conta: ")
                exibir_extrato(conta_numero)

            elif opcao == "7":
                contas = carregar_conta()

            elif opcao == "0":
                salvando_conta(contas)
                print("Voltando ao menu principal...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as erro:
            print(f"Erro: {erro}")

if __name__ == '__main__':
    menu_contas()