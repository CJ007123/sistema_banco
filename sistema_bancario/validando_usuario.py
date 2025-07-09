import string
from datetime import datetime

class Validador:
    """
    Classe com métodos estáticos responsáveis por validar os dados inseridos
    durante o cadastro e movimentações bancárias.
    """

    @staticmethod
    def validar_nome(nome: str):
        """
        Valida o nome completo do usuário.

        Regras:
        - Deve ser uma string.
        - Não pode estar vazio.
        - Não pode conter números.
        - Deve conter pelo menos nome e sobrenome.
        - Não pode conter caracteres especiais.
        """
        if not isinstance(nome, str):
            raise TypeError('O nome precisa ser uma caracter e não pode conter números')
        
        if not nome.strip():
            raise ValueError('O nome não pode estar vazio')
        
        nome_com_numeros = any(c.isdigit() for c in nome)
        nome_com_caracteres_especiais = any(caracter in string.punctuation for caracter in nome)

        if nome_com_numeros:
            raise ValueError('Nome não pode ter números')

        if len(nome.split()) < 2:
            raise ValueError('Deve conter nome e sobrenome nesse campo')
        
        if nome_com_caracteres_especiais:
            raise ValueError('O nome não pode ter caracteres especiais')

    @staticmethod
    def validar_cpf(cpf: str):
        """
        Valida o CPF do usuário.

        Regras:
        - Deve ser uma string numérica.
        - Deve conter exatamente 11 dígitos.
        """
        if not isinstance(cpf, str):
            raise TypeError('O CPF precisa ser uma string contendo apenas números')
        
        if not cpf.strip():
            raise ValueError('O CPF está vazio')
    
        if not cpf.isdigit():
            raise ValueError('O CPF só pode conter números inteiros')
        
        if len(cpf) != 11:
            raise ValueError('CPF inválido! Deve conter exatamente 11 números')

    @staticmethod
    def validar_logradouro(logradouro: str):
        """
        Valida o logradouro do endereço.

        Regras:
        - Deve ser uma string.
        - Deve ter pelo menos 5 caracteres.
        - Não pode estar vazio.
        """
        if not isinstance(logradouro, str):
            raise TypeError('Logradouro precisa ser um texto')
        
        if not logradouro.strip():
            raise ValueError('Logradouro não pode estar em branco')
        
        if len(logradouro) < 5:
            raise ValueError('O logradouro não pode ter menos de 5 caracteres')

    @staticmethod
    def validar_numero_residencia(numero: int | float):
        """
        Valida o número da residência.

        Regras:
        - Deve ser uma string (apesar de ser número, pode conter letras como "123A").
        - Não pode estar vazio.
        - Deve conter no máximo 15 caracteres.
        """
        if not isinstance(numero, str):
            raise TypeError('O número da residência precisa ser uma string')
        
        if not numero.strip():
            raise ValueError('Número da residência não pode estar vazio')
        
        if len(numero) > 15:
            raise ValueError('O número da residência deve ter no máximo 15 caracteres')

    @staticmethod
    def validar_bairro(bairro: str):
        """
        Valida o nome do bairro.

        Regras:
        - Deve ser uma string.
        - Não pode estar vazio.
        """
        if not isinstance(bairro, str):
            raise TypeError('O bairro precisa ser um texto')
        
        if not bairro.strip():
            raise ValueError('O bairro não pode estar vazio')

    @staticmethod
    def validar_estado(estado: str):
        """
        Valida o estado (sigla).

        Regras:
        - Deve ser uma string com duas letras maiúsculas (ex: SP, RJ).
        """
        maiuscula = any(m.isupper() for m in estado)

        if not isinstance(estado, str):
            raise TypeError('O estado precisa ser uma string')
        
        if not estado.strip():
            raise ValueError('O estado não pode estar vazio')
        
        if len(estado) != 2 or not maiuscula:
            raise ValueError('O estado deve conter duas letras maiúsculas (ex: SP)')

    @staticmethod   
    def validar_deposito_saque(deposito: int | float):
        """
        Valida valores para depósito ou saque.

        Regras:
        - Não pode ser string.
        - Não pode ser nulo.
        - Deve ser maior que zero.
        """
        if isinstance(deposito, str):
            raise TypeError('O depósito precisa ser um número')
    
        if deposito is None:
            raise ValueError('É necessário inserir um valor para o depósito')
    
        if deposito <= 0:
            raise ValueError('Por favor, deposite apenas valores positivos')

    @staticmethod
    def validando_data_nascimento(data_nascimento: datetime):
        """
        Valida o formato da data de nascimento.

        Regras:
        - Deve seguir o formato: DD/MM/AAAA
        """
        try:
            datetime.strptime(data_nascimento, '%d/%m/%Y')
        except ValueError:
            raise ValueError('A data de nascimento é inválida. Use o formato: DD/MM/AAAA')

    
        
    