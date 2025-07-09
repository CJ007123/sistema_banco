from datetime import datetime
import json
from usuario import *

usuarios = {}


def salvar_dados(dados):
    """
    Salva os dados de usuários em um arquivo JSON.

    Parâmetros:
        dados (dict): Dicionário contendo os dados dos usuários.

    Retorno:
        None
    """
    with open('usuario.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print('Os dados do usuário foram salvos com sucesso!')


def carregar_dados():
    """
    Carrega os dados de usuários a partir de um arquivo JSON.

    Retorno:
        dict: Dicionário com os dados dos usuários carregados do arquivo.
    """
    try:
        with open('usuario.json', 'r', encoding='utf-8') as arquivo:
            usuario = json.load(arquivo) 
            for dados in usuario.values():
                print(f"Nome: {dados['Nome']}")
                print(f"CPF: {dados['CPF']}")
                print(f"Data de nascimento: {dados['Data_de_nascimento']}")
                print(f"Logradouro: {dados['Logradouro']}")
                print(f"Número: {dados['Número']}")
                print(f"Bairro: {dados['Bairro']}")
                print(f"Estado: {dados['Estado']}\n")
            return usuario
    except FileNotFoundError:
        print('Arquivo não foi encontrado')
        return {}


def menu_usuarios():
    """
    Exibe o menu interativo para gerenciar usuários do sistema.

    Funcionalidades disponíveis:
        1 - Criar usuário
        2 - Exibir informações dos usuários
        3 - Atualizar nome
        4 - Atualizar logradouro
        5 - Atualizar número da residência
        6 - Atualizar bairro
        7 - Atualizar estado
        8 - Atualizar data de nascimento
        9 - Excluir conta
       10 - Carregar dados de um arquivo JSON
        0 - Salvar e sair
    """

    while True:
        print("\n=== MENU DE USUÁRIOS ===")
        print("1 - Criar usuário")
        print("2 - Exibir informações dos usuários")
        print("3 - Atualizar nome do usuário")
        print("4 - Atualizar logradouro")
        print("5 - Atualizar número da residência")
        print("6 - Atualizar bairro")
        print("7 - Atualizar estado")
        print("8 - Atualizar data de nascimento")
        print("9 - Excluir conta")
        print("10 - Carregar dados salvos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                nome = input("Nome completo: ")
                cpf = input("CPF: ")
                data = input("Data de nascimento (DD-MM-AAAA): ")
                logradouro = input("Logradouro: ")
                numero = input("Número: ")
                bairro = input("Bairro: ")
                estado = input("Estado (sigla): ")
                criar_usuario(nome, cpf, data, logradouro, numero, bairro, estado)

            elif opcao == "2":
                exbir_informações_do_usuario()

            elif opcao == "3":
                cpf = input("Digite o CPF: ")
                novo_nome = input("Novo nome completo: ")
                atualizar_nome_usuario(cpf, novo_nome)

            elif opcao == "4":
                cpf = input("Digite o CPF: ")
                novo_logradouro = input("Novo logradouro: ")
                atualizar_logradouro_usuario(cpf, novo_logradouro)

            elif opcao == "5":
                cpf = input("Digite o CPF: ")
                novo_numero = input("Novo número da residência: ")
                atualizar_numero_usuario(cpf, novo_numero)

            elif opcao == "6":
                cpf = input("Digite o CPF: ")
                novo_bairro = input("Novo bairro: ")
                atualizar_bairro_usuario(cpf, novo_bairro)

            elif opcao == "7":
                cpf = input("Digite o CPF: ")
                novo_estado = input("Novo estado (sigla): ")
                atualizar_estado_usuario(cpf, novo_estado)

            elif opcao == "8":
                cpf = input("Digite o CPF: ")
                nova_data = input("Nova data de nascimento (DD-MM-AAAA): ")
                atualizar_data_nascimento_usuario(cpf, nova_data)

            elif opcao == "9":
                cpf = input("Digite o CPF: ")
                excluir_conta(cpf)

            elif opcao == "10":
                global usuarios
                usuarios = carregar_dados()

            elif opcao == "0":
                salvar_dados(usuarios)
                print("Encerrando o menu de usuários...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except Exception as erro:
            print(f"Erro: {erro}")


if __name__ == '__main__':...
