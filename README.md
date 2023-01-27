<div align="center" id="top"> 
  <img src="./assets/images/logo_adote.png" alt="Adote" width="200px"/>
  <H1>ADO.TE</H1>
</div>
 
<p align="center">
  <a href="#sobre">Sobre</a> &#xa0; | &#xa0; 
  <a href="#funcionalidades">Funcionalidades</a> &#xa0; | &#xa0;
  <a href="#tecnologias">Tecnologias</a> &#xa0; | &#xa0;
  <a href="#pre-requisitos">Pré-requisitos</a> &#xa0; | &#xa0;
  <a href="#comecando">Começando</a>
</p>

<br>

<p align="center">
  <img alt="Cadastro" src="assets/images/pagina_de_cadastro.jpeg" width=250>
  <img alt="Login" src="assets/images/pagina_de_login.jpeg" width=250>
  <img alt="Seus pets" src="assets/images/seus_pets.jpeg" width=250>
  <img alt="Página de adoção" src="assets/images/pagina_de_adocao.jpeg" width=250>
  <img alt="Página de informações do pet" src="assets/images/informacoes_do_pet.jpeg" width=250>
  <img alt="Página de pedidos de adoção" src="assets/images/pedidos_de_adocao.jpeg" width=250>
  <img alt="Dashboard de doações" src="assets/images/pagina_de_dashboard.jpeg" width=250>
</p>

<br>

## <div id="sobre">🎯 Sobre</div>

Aplicação web para que pessoas e/ou ONGs possam cadastrar, gerenciar e adotar pets.

## <div id="funcionalidades">✨ Funcionalidades</div>

✔️ Sistema de autenticação (cadastro de usuários e login/logout);\
✔️ Envio de e-mails;\
✔️ Listagem de pets cadastrados pelo usuário;\
✔️ Listagem de pets disponíveis para adoção, com opções de filtragem;\
✔️ Página de detalhes do pet, na qual o usuário pode solicitar adoção;\
✔️ Página de pedidos de adoção, na qual o dono do pet pode aceitar ou recusar solicitações de adoção;\
✔️ Dashboard que mostra a quantidade de adoções por raça.

## <div id="tecnologias">🚀 Tecnologias</div>

As seguintes ferramentas foram utilizadas na construção do projeto:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Pillow](https://python-pillow.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/)


## <div id="pre-requisitos">✅ Pré-requisitos</div>

Antes de começar, você precisa ter o [Python](https://www.python.org/downloads/) instalado em sua máquina.


## <div id="comecando">🏁 Começando</div>

1° - Clone o repositório e entre na pasta do projeto:

```bash
# Clone este repositório
$ git clone https://github.com/raphael-araujo/adote

# Entre na pasta
$ cd adote
```

2° - Crie e ative um ambiente virtual:

```bash
# Para criar:
  # Linux
      $ python3 -m venv venv
  # Windows
      $ python -m venv venv

# Para ativar:
  # Linux
      $ source venv/bin/activate
  # Windows
      $ venv/Scripts/Activate

# Caso algum comando retorne um erro de permissão, execute o código abaixo e tente novamente:

  $ Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

3° - Instale as dependências:

```bash
# Linux
    $ pip3 install -r requirements.txt
# Windows
    $ pip install -r requirements.txt
```

4° - Faça as migrações:

```bash
# Linux
    $ python3 manage.py migrate
# Windows
    $ python manage.py migrate
```

5° - Crie um super usuário:

```bash
# Linux
    $ python3 manage.py createsuperuser
# Windows
    $ python manage.py createsuperuser
```

6° - Inicie a aplicação:

```bash
# Para iniciar o projeto
  # Linux
      $ python3 manage.py runserver
  # Windows
      $ python manage.py runserver

# O app será iniciado em <http://127.0.0.1:8000/>

# Para iniciar o projeto em uma porta especifica
    $ python manage.py runserver <porta>

# O app vai inicializar em <http://127.0.0.1:<porta>/>
```

&#xa0;

<a href="#top">Voltar para o topo</a>
