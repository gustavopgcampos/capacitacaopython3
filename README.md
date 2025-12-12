# Como rodar o projeto
##### 1. Clone o repositório do projeto:
```bash
  git clone https://github.com/gustavopgcampos/capacitacaopython3.git
```
##### 2. Abra o projeto no VSCODE, aperte CTRL + J e rode o seguinte comando abaixo para baixar as dependências do PIP:
```bash
  pip install -r requirements.txt
```

##### 3. Entre dentro do ambiente criado pelo venv:
```bash
  source venv/bin/active ou ./venv/Scripts/Activate
```

##### 4. Crie um banco com o nome de biblioteca 

##### 5. Dentro da pasta mainProject, crie um arquivo chamado settings.py com a seguinte estrutura e coloque as informações referentes ao seu banco de dados. [Clique aqui para ver a estrutura](https://pastebin.com/GG0xDR1s)

##### 6. Rode as migrations com os seguintes comandos abaixo:
```bash
  python manage.py makemigrations
  python manage.py migrate biblioteca
  python manage.py migrate users
```

##### 7. Para criar um superusuário para ter acesso a API:
```bash
  python manage.py createsuperuser
```

##### 8. Após feito todas essas etapas, basta rodar o comando abaixo dentro do ambiente virtual do python para iniciar o projeto:
```bash
  python manage.py runserver
```
___

## API Documentation

#### Buscar todos os livros

```http
  GET /api/livros/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

#### Adicionar um livro 

```http
  POST /api/livros/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `titulo, autor, ano, isbn`      | `JSON` | **Required - Basic Auth** |

#### Deletar um livro 

```http
  DELETE /api/livros/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

#### Buscar todos os usuários

```http
  GET /api/usuarios/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

#### Adicionar um usuário

```http
  POST /api/usuarios/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username, email, password`      | `JSON` | **Required - Basic Auth** |

#### Deletar um usuário 

```http
  DELETE /api/usuarios/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

#### Buscar todos os empréstimos

```http
  GET /api/usuarios/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `authorization` | `string` | **Required - Basic Auth** |

#### Adicionar um empréstimo

```http
  POST /api/emprestimos/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `usuario_fk, livro_fk` | `JSON` | **Required - Basic Auth** |

#### Deletar um empréstimo 

```http
  DELETE /api/emprestimos/<id>/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required - Basic Auth** |

___

#### Adicionar uma devolução

```http
  POST /api/devolucao/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `emprestimo_id, usuario_fk, livro_fk, data_retirada, status` | `string` | **Required - Basic Auth** |
