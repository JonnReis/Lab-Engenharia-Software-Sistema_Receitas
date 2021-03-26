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

## Requerimentos mínimos
- Python V3.6 ou >
- MySQL Database

## Iniciar projeto
- Clonar e atualizar repositório
```
git clone https://github.com/JonnReis/Lab-Engenharia-Software-Sistema_Receitas.git
cd Prototipo_receitas
git checkout master
git pull
```
- Inicializando ambiente virtual
```
 python -m venv env
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
MYSQL_PASSWORD=1234554321
```
- Criando Banco de dados (Collection)
``` 
python wsgi.py create_db
```
- Inicializando aplicação
```
wsgi.py
```
ou
``` 
flask run
```
- Inicializando aplicação com o Guinicorn

"# Lab-Engenharia-Software-Sistema_Receitas" 
"# Lab-Engenharia-Software-Sistema_Receitas" 
"# Lab-Engenharia-Software-Sistema_Receitas" 
