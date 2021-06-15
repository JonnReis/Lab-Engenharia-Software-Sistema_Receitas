# Sistema Receitas 

## Aluno
- Jonatas dos Reis Ferreira

## Objetivo
- Desenvolver um sistema Web para criação de receitas em Python

## Tecnologias
- MySQL
- Flask
- SQLAlchemy
- Jinja2
- Gunicorn
- HTML5
- CSS
- Javascript

# Configuração

## Requisitos mínimos
- Python V3.6 ou superior
- MySQL Database

## Iniciar projeto
- Clonar e atualizar repositório
```
git clone https://github.com/JonnReis/Lab-Engenharia-Software-Sistema_Receitas.git
cd Prototipo_receitas
git checkout master
git pull
```
- Intalando o virtualenv
``` 
pip install virtualenv
```
- Inicializando ambiente virtual
```
 python -m venv env
 env\Scripts\activate
```

- Instalação das dependências
```
pip install -r requirements.txt
```

- Configurando ambiente

Configure a conexão com o MySQL criando o arquivo **.env** na raiz do projeto de acordo com o exemplo a seguir
```
MYSQL_DATABASE=receitas
MYSQL_HOST=localhost
MYSQL_PORT=3307
MYSQL_USERNAME=root
MYSQL_PASSWORD=12345
```
 **Obs: Se necessário, altere a senha do campo "MYSQL_PASSWORD" de acordo com o seu usuário root**

- Criando Banco de dados (Collection) e iniciando aplicação
``` 
python wsgi.py create_db
```
- Inicializando aplicação com o BD ja criado

Gunicorn (Terminal Unix)
```
gunicorn --bind IP:PORTA wsgi:app

gunicorn --bind 0.0.0.0:1234 wsgi:app
```
WSGI (Terminal Windows)
```
python wsgi.py
```

- Acessando aplicação

Acesse http://127.0.0.1:5000/

### Vídeo explicativo [Entrega_1](https://youtu.be/mVbQp_XvaVI)

"# Lab-Engenharia-Software-Sistema_Receitas" 
"# Lab-Engenharia-Software-Sistema_Receitas" 
"# Lab-Engenharia-Software-Sistema_Receitas" 
