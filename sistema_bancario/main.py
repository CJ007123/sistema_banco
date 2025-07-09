from main_conta import menu_contas
from main_usuario import menu_usuarios



def menu_principal():
    """
    Exibe o menu principal da aplicação, permitindo o acesso aos submenus
    de contas ou usuários.

    Opções:
        [1] -> Acessa o menu de contas (operações bancárias).
        [2] -> Acessa o menu de usuários (cadastro e edição de perfis).
        [0] -> Encerra o programa.

    Fluxo:
        A função permanece em loop até que o usuário escolha sair.
    """
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print('[1]-> Menu contas')
        print('[2]-> Menu usuario')
        print('[0]-> Sair')

        escolha = input('Escolha uma opção: ')
        if escolha == '1':
            menu_contas()
        elif escolha == '2':
            menu_usuarios()
        elif escolha == '0':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida')


if __name__ == '__main__':
    menu_principal()