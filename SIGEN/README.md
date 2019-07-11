# Solução para o desafio técnico: Aplicação



## Ativando a Venv:


A partir do diretório raiz deste projeto, executar:
```
    source serasa/bin/activate
```


## Instalando o pacote:


A partir do diretório onde este documento está localizado, executar:
```
    pip install .
```

## Configurando o banco de dados:


É necessário criar um banco de dados manualmento no mysql. As informações da URI do banco devem ser adicionadas no objeto DATABASA_CONFIG, que encontra-se no arquivo app.py. A aplicação criará as tabelas automaticamente quando inicializada.


## Executando a aplicação:


```
    python -m serasa_app
```
A aplicação será executada em http://localhost:5000.


## Detalhes do Pacote:


### Models

    Conjunto de modelos de banco de dados. A aplicação inteira faz uso de sqlalchemy ORM
    1. Debt: Modelagem básica de uma cobrança em aberto.
    Campos:
        - id(integer): Identificador unico de uma cobrança em aberto.
        - cpf(string): O CPF do devedor
        - doc(string): O numero do documento referente a cobrança
        - company(string): Nome da empresa efetuando a cobrança
        - due_date(datetime.date): Data de vencimento do documento
        - amount(decimal): Valor do documento
    2. User: Modelagem de um usuário de sistema.
    Campos:
        - id(integer): Idenetificador numerico de usuarios
        - username(string): Nome de usuario utilizado para o Login
        - password(string): Senha do usuario
        - name(string): Nome completo do usuario
        - add(boolean): Indica se o usuario pode ou nao adicionar novas cobranças
        - edit(boolean): Indica se o usuario pode ou nao modificar cobranças existentes
        - delete(boolean): Indica se o usuario pode ou nao deletar cobrancas existentes
        - root(boolean): Indica se o usuario tem permissao de root(No caso dessa aplicacao, apenas usuarios root podem criar novos usuarios)

### Forms

    Conjunto de formulários utilizados pela aplicação, os formulários foram criados utilizando flask-wtforms
    1. add_debt: Formulário para criação de cobranças
    2. edit_edit: Formulário para modificação de cobranças
    3. findme: Formulário para busca por cpf
    4. create_user: Formulário para criação de usuários
    5. login: Formulário para login

### Views

    Conjunto de views utilizadas pela aplicação
    1. add_debt(endpoint: /add/): View de criação de cobranças. Apenas usuários com privilégio "add" podem acessar.
    2. edit_debt(endpoint: /edit/<debt_id>): View para edição de cobranças a partir do identificador unico da cobrança. Apenas usuários com privilégio "edit" podem acessar.
    3. delete(endpoint: /delete/<debt_id>): View para recomeção de cobranças a partir de identificador unico da cobrança. Apenas usuários com privilégio "delete" podem acessar.
    4. create_user(endpoint: /user/create/): View para criação de usuários. Apenas usuários com privilégio de root podem acessar.
    5. login(endpoint: /login/): View para login de usuarios
    6. logout(endpoint: /logout/): View para logout de usuarios
    7. manage(endpoint: /manage/): Painel de gerenciamento de cobranças. A disponibilidade operações neste painel depende dos privilégios do usuário.

### Templates

    Conjunto de templates utilizadas pelas views. Todos os htmls estão nesta pasta.

### Static

    Arquivos estáticos (css e imagens)

### Tests

    O diretório contém o arquivo tests.py que valida as views disponiveis.


## Detalhes de implementação e uso:


    Bibliotecas utilizadas:
        - Flask
        - Flask-Wtf
        - Flask-Login
        - Bcrypt
        - SqlAlchemy

    Banco de dados: MySQL(acessado pela aplicação através de sqlalchemy ORM)
    
    A aplicação foi construída como um pacote python, desta forma podendo ter seus recursos facilmente importados por outras aplicações, assim como permitindo a execução desta aplicação dentro de um docker.


## Recomendações de uso:


    Como credenciais de root são necessárias para a criação de usuários, o primeiro usuário do sistemas deve ser criado manualmente no banco de dados.


## Sugestões de melhorias


    1. Armazenar as cobranças em uma base de dados NoSQL(e.g dynamoDB) ou elasticsearch, uma vez que estes permitem maior flexibilidade para as informações armazenadas e, no caso do elasticsearch, oferecerem maior disponibilidade dos dados.
    2. Fazer uso de amazon SQS para executar ações de usuário como criação, e remoção de cobranças, de forma assincrona, diminuindo assim acessos simultaneos no banco de dados
    3. Incluir mais mensagens de erro e notificações em geral
    4. Refazer as views de login utilizando OAuth, para garantir maior segurança para a aplicação, além de possibilitar a integração das ids de usuários de outras aplicações.
    5. Aprimorar a validação dos formulários
