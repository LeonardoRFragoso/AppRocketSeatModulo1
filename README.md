
# 📒 Agenda de Contatos

Este projeto é uma agenda de contatos que permite adicionar, visualizar, editar, marcar/desmarcar como favorito, visualizar favoritos e apagar contatos. A interface gráfica é criada utilizando `tkinter`, e os dados são armazenados em um banco de dados SQLite.

## 📋 Funcionalidades

- **Adicionar Contato**: Adicione um novo contato com nome, telefone e email.
- **Visualizar Lista de Contatos**: Exibe todos os contatos cadastrados.
- **Editar Contato**: Permite editar as informações de um contato existente.
- **Marcar/Desmarcar Favorito**: Marca ou desmarca um contato como favorito.
- **Ver Lista de Contatos Favoritos**: Exibe todos os contatos marcados como favoritos.
- **Apagar Contato**: Remove um contato da lista.

## 🛠 Requisitos

- Python 3.6 ou superior
- `tkinter`: Biblioteca padrão para a criação de interfaces gráficas em Python.
- `sqlite3`: Biblioteca padrão para interação com banco de dados SQLite em Python.

## 🚀 Como Utilizar

### Passo 1: Clonar o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/LeonardoRFragoso/AppRocketSeatModulo1.git
cd AppRocketSeatModulo1
```

### Passo 2: Instalar Dependências

Instale as bibliotecas necessárias (caso não estejam instaladas).

No Windows, `tkinter` geralmente já está instalado com a instalação do Python. Se não estiver, você pode instalar via pip:

```bash
pip install tk
```

### Passo 3: Executar o Programa

Execute o script Python principal para iniciar a aplicação:

```bash
python app.py
```

### Passo 4: Utilizar a Interface Gráfica

A interface gráfica aparecerá com as seguintes opções:

- **Adicionar Contato**: Clique para adicionar um novo contato. Preencha os campos nome, telefone e email nos diálogos que aparecerão e clique em "OK".
- **Visualizar Lista de Contatos**: Clique para ver todos os contatos cadastrados. Uma mensagem com a lista será exibida.
- **Editar Contato**: Clique para editar um contato existente. Insira o índice do contato que deseja editar e, em seguida, preencha os novos dados.
- **Marcar/Desmarcar Favorito**: Clique para marcar ou desmarcar um contato como favorito. Insira o índice do contato desejado.
- **Ver Lista de Contatos Favoritos**: Clique para ver todos os contatos favoritos.
- **Apagar Contato**: Clique para apagar um contato. Insira o índice do contato que deseja apagar.

## 📂 Estrutura do Código

- `app.py`: Arquivo principal que contém todo o código da aplicação, incluindo a definição das classes `Contato`, `Agenda`, `CustomDialog` e `App`.

## 🗃 Estrutura do Banco de Dados

O banco de dados SQLite `agenda.db` possui uma tabela chamada `contatos` com a seguinte estrutura:

- `id`: Identificador único do contato (INTEGER PRIMARY KEY).
- `nome`: Nome do contato (TEXT).
- `telefone`: Telefone do contato (TEXT).
- `email`: Email do contato (TEXT).
- `favorito`: Status de favorito do contato (BOOLEAN).

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.
