Sistema de Gerenciamento de Biblioteca em Django

Esse projeto é um Sistema de Gerenciamento de Biblioteca, desenvolvido em python com o framework Django
Utilizando banco de dados MYSQL para armazenar informações de livros, usuários e empréstimos, nos permitindo cadastros, controle de empréstimos e devoluções por meio de uma API REST. Projeto para fins acadêmicos.

# O que o sistema permite

* Cadastro de livros e usuários
* Consulta de livros cadastrados
* Registro de empréstimos de livros
* Registro de devoluções
* Atualização automática do status do livro (disponível / emprestado)
* Listagem de livros, usuários e empréstimos
* Persistência dos dados em banco de dados MySQL
* Acesso administrativo através do superusuário

# Estrutura do Projeto

Descrição dos principais arquivos

`manage.py`: arquivo principal do Django, ele é responsável por executar comandos administrativos como: rodar servidor, migrações, criação de usuário administrador, etc.
`requirements.txt`: lista todas as dependências necessárias para executar o projeto.
`script.sql`: script SQL para inserção de livros iniciais no banco de dados.
`mainProject/`: diretório principal de configuração do projeto Django.

# Dependências necessárias

# Requisitos

* Ter python 3 instalado
* MySQL Server
* MySQL Workbench (não obrigatório, mas interessante para visualização dos dados)
* VS Code recomendado

# Banco de Dados

Em nosso sistema utilizamos MYSQL como banco de dados.

As configurações básicas são:

1. Criar um banco de dados com nome `biblioteca`
2. Configurar usuário, senha e nome do banco no arquivo `settings.py`
3. Executar as migrações do Django através do terminal

python manage.py makemigrations
python manage.py migrate

Se quiser facilitar a inserção de livros automaticamente no banco, execute o arquivo `script.sql` no MySQL Workbench.

# Como Executar o Projeto

1 - Abra o terminal na pasta do projeto

2 - Ative o ambiente virtual

3 - Inicie o servidor Django

python manage.py runserver

Após isso, o projeto vai estar funcionando. Também é possível acessar através de: http://127.0.0.1:8000/

Para acesso administrativo, crie um superusuario rodando:

python manage.py createsuperuser

# Executar as migrações no terminal

As migrações criam as tabelas necessárias no banco de dados:

python manage.py makemigrations, 
python manage.py migrate
python manage.py migrate biblioteca, 
python manage.py migrate users

# Como criar um superusuário

python manage.py createsuperuser

Esse usuário será utilizado para acesso administrativo e autenticação da API.

# Funcionalidades da API:

Livros:

* Buscar todos os livros
* Cadastrar um livro
* Deletar um livro

Usuários:

* Buscar todos os usuários
* Cadastrar usuário
* Deletar usuário

Empréstimos:

* Registrar empréstimos
* Listar empréstimos
* Registrar devoluções

## API Documentation

# Buscar todos os livros

```http
  GET /api/livros/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

# Adicionar um livro 

```http
  POST /api/livros/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `titulo, autor, ano, isbn`      | `JSON` | **Required - Basic Auth** |

# Deletar um livro 

```http
  DELETE /api/livros/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

# Buscar todos os usuários

```http
  GET /api/usuarios/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

# Adicionar um usuário

```http
  POST /api/usuarios/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username, email, password`      | `JSON` | **Required - Basic Auth** |

# Deletar um usuário 

```http
  DELETE /api/usuarios/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

# Buscar todos os empréstimos

```http
  GET /api/usuarios/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

# Adicionar um empréstimo

```http
  POST /api/emprestimos/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_fk, livro_fk` | `JSON` | **Required - Basic Auth** |

# Deletar um empréstimo 

```http
  DELETE /api/emprestimos/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

# Adicionar uma devolução

```http
  POST /api/devolucao/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `emprestimo_id, usuario_fk, livro_fk, data_retirada, status` | `string` | **Required - Basic Auth** |


# Como Testar

1. Verificar se o MySQL está em execução
2. Execute o projeto com `runserver`
3. Utilize a ferramenta Postman ou Insomnia para testar os endpoints da API
4. Se quiser uma melhor visualização, utilizar o MYSQL Workbench

---

# Visualização no MySQL Workbench

1. Abrir o MySQL Workbench
2. Conecte ao banco biblioteca
3. Executar comandos SQL, por exemplo:

sql:
SELECT * FROM livros;
SELECT * FROM usuarios;
SELECT * FROM emprestimos;

# Autores

Carla Cristina Neves Rocha,
Edilma Santana de Jesus,
Gustavo Pereira Gonçalves de Campos, 
Ivan Miguel da Silva e
Wellington Camargo

Projeto acadêmico – Sistema de Gerenciamento de Biblioteca em Django
