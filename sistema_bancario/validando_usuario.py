import string
from datetime import datetime

class Validador:
    @staticmethod
    def validar_nome(nome: str):
        if not isinstance(nome, str) :
            raise TypeError('O nome precisa ser uma caracter e não pode conter números')
        
        if not nome.strip():
            raise ValueError('O nome não pode estar vazio')
        
        nome_com_numeros = any(c.isdigit() for c in nome)
        nome_com_caracteres_especiais = any(caracter in string.punctuation for caracter in nome)

        if nome_com_numeros:
            raise ValueError('Nome não pode ter números')

        if len(nome.split()) < 2:
            raise ValueError('Deve conter nome sobrenome nesse campo')
        
        if nome_com_caracteres_especiais:
            raise ValueError('O nome não pode ter caracteres especiais')
        
        if not nome.strip():
            raise ValueError('O nome não pode estar vazio')

        
    @staticmethod
    def validar_cpf(cpf: str):
        if not isinstance(cpf,str):
            raise TypeError('O CPF precisa ser uma caracter com números')
        
        if not cpf.strip():
            raise ValueError('O CPF esta vazio')
    
        if not cpf.isdigit():
            raise ValueError('O CPF só pode conter números inteiros')
        
        if len(cpf) != 11:
            raise ValueError('CPF inválido! Só pode conter no máximo 11 números')
        
    

    @staticmethod
    def validar_logradouro(logradouro:str):
        if not isinstance(logradouro, str):
            raise TypeError('Logradouro precisa ser uma caracter')
        
        if not logradouro.strip():
            raise ValueError('Logradouro não estar com espaço vazio')
        
        if len(logradouro) < 5:
            raise ValueError('O Logradouro não pode ter menos de 5 caracteres')
    

    @staticmethod
    def validar_numero_residencia(numero: int | float):
        if not isinstance(numero, str):
            raise TypeError('O numero da residencia precisa ser uma caracter')
        
        if not numero.strip():
            raise ValueError('Número não pode estar vazio')
        
        if len(numero) > 15:
            raise ValueError('O número da residencia tem que ser no máximo 15 caracter')
        
    

    @staticmethod
    def validar_bairro(bairro: str):
        if not isinstance(bairro, str):
            raise TypeError('O bairro precisa ser uma caracter')
        
        if not bairro.strip():
            raise ValueError('Bairro não pode estar vazio')


    @staticmethod
    def validar_estado(estado: str):
        maiuscula = any(m.isupper() for m in estado)

        if not isinstance(estado, str):
            raise TypeError('O estado precisa ser uma caracter')
        
        if not estado.strip():
            raise ValueError('O estado não pode estar vazio')
        
        if len(estado) != 2 or not maiuscula:
            raise ValueError('O estado só pode conter duas síglas maíusculas')
        
        
    @staticmethod   
    def validar_deposito_saque(deposito: int | float):
        if isinstance(deposito, str):
            raise TypeError('O depósito precisa ser um número')
    
        if deposito is None:
            raise ValueError('É necessário inserir um valor para o depósito')
    
        if deposito <= 0:
            raise ValueError('Por favor, depósite apenas valores posítivos')
        
        
        
    @staticmethod
    def validando_data_nascimento(data_nascimento: datetime):
        try:
            tratanto_data = datetime.strptime(data_nascimento,'%d/%m/%Y')
        except ValueError:
            raise ValueError('A data de nascimento inválida. Data deve seguir esse seguinte formato: DD/MM/AAAA')



    
        
    