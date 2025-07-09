# 💰 Sistema Bancário em Python

Este é um projeto de sistema bancário simples, desenvolvido em Python com foco em **validações, organização modular, persistência de dados em JSON** e menus interativos.

## 📌 Funcionalidades

### 👤 Usuários
- Criar um novo usuário
- Exibir informações dos usuários cadastrados
- Atualizar dados (nome, logradouro, número, bairro, estado, data de nascimento)
- Excluir conta
- Salvar e carregar usuários via JSON

### 🏦 Contas
- Criar conta corrente vinculada a um CPF
- Depositar valores
- Realizar saques (limite de 3 por sessão)
- Transferência entre contas
- Exibir dados da conta
- Consultar extrato bancário
- Salvar e carregar contas via JSON

## 🧠 Tecnologias utilizadas

- `Python 3.10+`
- Manipulação de arquivos com `json`
- Validações com `try/except`
- Organização modular com múltiplos arquivos `.py`
- Lógica de menus com `input()` e `while True`

## 📁 Estrutura do Projeto

```bash
sistema_bancario/
│
├── main.py                    # Menu principal
├── main_usuario.py            # Menu de usuários
├── main_conta.py              # Menu de contas
│
├── usuario.py                 # Lógica de gerenciamento de usuários
├── contas.py                  # Lógica de gerenciamento de contas
├── validando_usuario.py       # Módulo de validações
│
├── usuario.json               # Banco de dados dos usuários
├── conta.json                 # Banco de dados das contas
│
└── README.md                  # Este arquivo 


▶️ Como executar

Clone o repositório:
git clone https://github.com/seu-usuario/seu-repo.git
cd sistema_bancario


Execute o menu principal:
python main.py



💡 Observações:

- O sistema salva automaticamente os dados ao sair dos menus.

- O limite de saques por sessão é de 3 vezes (reiniciado ao reiniciar o programa).

- Os dados dos usuários e contas são armazenados em arquivos JSON (usuario.json e conta.json).





