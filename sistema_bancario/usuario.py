from validando_usuario import Validador
from datetime import datetime

usuarios = {}

def criar_usuario(nome: str, cpf: str, data_nascimento: datetime, logradouro: str, numero: str, bairro: str, estado: str):
    Validador.validar_nome(nome)
    Validador.validar_cpf(cpf)
    Validador.validando_data_nascimento(data_nascimento)
    Validador.validar_logradouro(logradouro)
    Validador.validar_numero_residencia(numero)
    Validador.validar_bairro(bairro)
    Validador.validar_estado(estado)

    if cpf in usuarios:
        raise ValueError('Essa conta já existe')
    else:
        usuarios[cpf] = {
            'Nome': nome,
            'CPF': cpf,
            'Data_de_nascimento': data_nascimento,
            'Logradouro': logradouro,
            'Número': numero,
            'Bairro': bairro,
            'Estado': estado
        }
        print('Sua conta foi adicionada com sucesso')














"""
    Cria um novo usuário no sistema após validar todos os dados fornecidos.

    Parâmetros:
        nome (str): Nome completo do usuário.
        cpf (str): CPF do usuário, usado como identificador único.
        data_nascimento (datetime): Data de nascimento do usuário.
        logradouro (str): Nome da rua ou avenida.
        numero (str): Número da residência.
        bairro (str): Bairro do usuário.
        estado (str): Estado onde o usuário reside.

    Levanta:
        ValueError: Se o CPF já estiver registrado ou os dados forem inválidos.
    """

def exbir_informações_do_usuario():
    """
    Exibe todas as informações dos usuários cadastrados no sistema.

    Levanta:
        ValueError: Se não houver usuários registrados.

    """
    if not usuarios:
        raise ValueError('Não há informações desse usúario no sistema')

    for info in usuarios.values():
        print(f"Nome: {info['Nome']}")
        print(f"CPF: {info['CPF']}")
        print(f"Data de nascimento: {info['Data_de_nascimento']}")
        print(f"Logradouro: {info['Logradouro']}")
        print(f"Número: {info['Número']}")
        print(f"Bairro: {info['Bairro']}")
        print(f"Estado: {info['Estado']}")


def atualizar_nome_usuario(cpf, novo_nome: str):
    """
    Atualiza o nome completo do usuário com base no CPF.

    Parâmetros:
        cpf (str): CPF do usuário.
        novo_nome (str): Novo nome completo.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validar_nome(novo_nome)
    atualizar_nome = usuarios.get(cpf)
    if atualizar_nome:
        res = usuarios[cpf]['Nome'] = novo_nome
        print(f'Nome do usuário foi atualizado para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def atualizar_logradouro_usuario(cpf: str, novo_logradouro: str):
    """
    Atualiza o logradouro do usuário.

    Parâmetros:
        cpf (str): CPF do usuário.
        novo_logradouro (str): Novo logradouro.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validar_logradouro(novo_logradouro)
    atualizar_logradouro = usuarios.get(cpf)
    if atualizar_logradouro:
        res = usuarios[cpf]['Logradouro'] = novo_logradouro
        print(f'Logradouro foi atualizado para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def atualizar_numero_usuario(cpf: str, novo_numero: str):
    """
    Atualiza o número da residência do usuário.

    Parâmetros:
        cpf (str): CPF do usuário.
        novo_numero (str): Novo número da residência.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validar_numero_residencia(novo_numero)
    atualizar_numero = usuarios.get(cpf)
    if atualizar_numero:
        res = usuarios[cpf]['Número'] = novo_numero
        print(f'Número da residência foi atualizado para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def atualizar_bairro_usuario(cpf: str, novo_bairro: str):
    """
    Atualiza o bairro do usuário.

    Parâmetros:
        cpf (str): CPF do usuário.
        novo_bairro (str): Novo bairro.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validar_bairro(novo_bairro)
    atualizar_bairro = usuarios.get(cpf)
    if atualizar_bairro:
        res = usuarios[cpf]['Bairro'] = novo_bairro
        print(f'Bairro foi atualizado para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def atualizar_estado_usuario(cpf: str, novo_estado: str):
    """
    Atualiza o estado onde o usuário reside.

    Parâmetros:
        cpf (str): CPF do usuário.
        novo_estado (str): Novo estado.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validar_estado(novo_estado)
    atualizar_estado = usuarios.get(cpf)
    if atualizar_estado:
        res = usuarios[cpf]['Estado'] = novo_estado
        print(f'Estado foi atualizado para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def atualizar_data_nascimento_usuario(cpf: str, nova_data: str):
    """
    Atualiza a data de nascimento do usuário.

    Parâmetros:
        cpf (str): CPF do usuário.
        nova_data (str): Nova data no formato válido.

    Levanta:
        ValueError: Se o CPF não for encontrado.
    """
    Validador.validando_data_nascimento(nova_data)
    atualizar_data_nascimento = usuarios.get(cpf)
    if atualizar_data_nascimento:
        res = usuarios[cpf]['Data_de_nascimento'] = nova_data
        print(f'Data de nascimento foi atualizada para: {res}')
    else:
        raise ValueError('O CPF inserido não esta registrado no sistema')


def excluir_conta(cpf: str):
    """
    Remove o usuário com base no CPF informado.

    Parâmetros:
        cpf (str): CPF do usuário.

    Levanta:
        ValueError: Se o CPF não estiver cadastrado.
    """
    apagar_conta = usuarios.get(cpf)
    if apagar_conta:
        del usuarios[cpf]
        print('Usuário foi excluído com sucesso')
    else:
        raise ValueError('Essa conta não está no sistema')


if __name__ == '__main__':...