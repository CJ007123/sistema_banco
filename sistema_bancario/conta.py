from usuario import usuarios
import random
from validando_usuario import Validador

contas = {}
iniciando_limite = 0
LIMITE_MAXIMO = 3


def numero_agencia():
    """
    Gera um número de agência aleatório com 4 dígitos.

    Retorna:
        str: Número da agência no formato de quatro dígitos (ex: '0321').
    """
    agencia = f'{random.randint(1,9999):04d}'
    return agencia


def conta_concorrente(cpf:str):
    """
    Cria uma nova conta corrente associada a um CPF existente.

    Parâmetros:
        cpf (str): CPF do usuário já registrado.

    Levanta:
        ValueError: Se o CPF não estiver cadastrado.
    """
    if cpf not in usuarios:
        raise ValueError('Seu cpf não esta registrado no sistema')
    else:
        numero_conta = f"{len(contas) + 1:04d}-1"
        contas[numero_conta] = {'agencia': numero_agencia(), 'numero': numero_conta, 'cpf': cpf, 'saldo': 0.0, 'historico': []}
        print('Conta concorrente criada com sucesso')


def exibir_dados_da_conta():
    """
    Exibe todas as contas registradas com seus dados principais.

    Levanta:
        ValueError: Se nenhuma conta estiver cadastrada.
    """
    if not contas:
        raise ValueError('Nenhuma conta foi registrada')
    for conta in contas.values():
        print(f'Agencia: {conta["agencia"]}')
        print(f'Número: {conta["numero"]}')
        print(f'CPF: {conta["cpf"]}')
        print(f'Saldo: R${conta["saldo"]:.2f}')


def depositar_em_conta_concorrente(numero_conta:str, deposito: int | float):
    """
    Realiza um depósito em uma conta específica.

    Parâmetros:
        numero_conta (str): Número da conta a receber o depósito.
        deposito (int | float): Valor a ser depositado.

    Levanta:
        ValueError: Se a conta não existir ou o valor for inválido.
    """
    Validador.validar_deposito_saque(deposito)
    depositar_valor = contas.get(numero_conta)
    if depositar_valor:
        contas[numero_conta]['saldo'] += deposito
        
        print(f'Depósito de R${deposito:.2f} Reais')
        depositar_valor['historico'].append(f'Depósito de R${deposito:.2f} Reais')
    else:
        raise ValueError('Número da conta não existe')


def saque_em_conta_concorrente(numero_conta:str, saque: int | float):
    Validador.validar_deposito_saque(saque)
    global iniciando_limite

    if iniciando_limite >= LIMITE_MAXIMO:
        raise ValueError('O limite de saque chegou ao fim! Volte outro dia para sacar novamente')
    
    saque_valor = contas.get(numero_conta)
    if saque_valor:
        if  contas[numero_conta]['saldo'] >= saque:
            contas[numero_conta]['saldo'] -= saque
            iniciando_limite += 1
            
            print(f'Saque de -R${saque:.2f} Reais')
            saque_valor['historico'].append(f'Saque de -R${saque:.2f} Reais')
        else:
            raise ValueError('O saque não pode ser maior que o saldo')
    else:
        raise ValueError('Número da conta não existe')


def transferencia(origem:str, destino:str, valor: int | float):
    """
    Realiza uma transferência entre duas contas diferentes.

    Parâmetros:
        origem (str): Número da conta de origem.
        destino (str): Número da conta de destino.
        valor (int | float): Valor a ser transferido.

    Levanta:
        ValueError: Se as contas forem iguais, não existirem ou o saldo for insuficiente.
    """
    Validador.validar_deposito_saque(valor)

    passo_origem = contas.get(origem)
    passo_destino = contas.get(destino)
    
    if passo_origem == passo_destino:
        raise ValueError('A origem e o destino não podem ser a mesma conta')

    if passo_origem and passo_destino:
        if passo_origem['saldo'] >= valor:
            passo_origem['saldo'] -= valor
            passo_destino['saldo'] += valor  

            print(f"Transferência enviada de R${valor:.2f} para conta {passo_destino['numero']}")
            print(f'Transferência recebida de R${valor:.2f} da conta {passo_origem["numero"]}')

            passo_origem['historico'].append(f"Transferência enviada de R${valor:.2f} para conta {passo_destino['numero']}")
            passo_destino['historico'].append(f'Transferência recebida de R${valor:.2f} da conta {passo_origem["numero"]}')
        else:
            raise ValueError('Seu saldo precisa ser maior ou igual ao valor que deseja transferir')
    else:
        raise ValueError('A conta origem ou destino não estão registrados no sistema')


def exibir_extrato(conta_numero:str):
    """
    Exibe o extrato de uma conta, listando todas as movimentações e o saldo atual.

    Parâmetros:
        conta_numero (str): Número da conta.

    Levanta:
        ValueError: Se a conta não estiver registrada.
    """
    if conta_numero not in contas:
        raise ValueError('Essa conta não esta registado')

    valor = contas[conta_numero]['historico']
    if valor:
        print(f'=== Extrato da conta {conta_numero}  ===')
        for item in valor:
            print(item)
        print(f'Saldo atual: R${contas[conta_numero]["saldo"]:.2f}')
    else:
        print('Nenhuma movimentação foi feita aqui')

if __name__ == '__main__':...
"""
    Realiza um saque de uma conta específica, respeitando o limite diário.

    Parâmetros:
        numero_conta (str): Número da conta.
        saque (int | float): Valor a ser sacado.

    Levanta:
        ValueError: Se a conta não existir, o saldo for insuficiente ou o limite for excedido.
    """