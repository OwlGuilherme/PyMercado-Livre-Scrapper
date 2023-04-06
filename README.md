# PyMercado-Livre-Scrapper

> Status: Em desenvolvimento. ⚠️

Script em python para WebScrapping de preços de produtos no site Mercado Livre
Utiliza-se a biblioteca [PlayWright](https://playwright.dev/python/) para controlar as automações.
A aplicação recebe do usuário o link do produto, raspa seu preço e nome e salva em um arquivo json.
Caso o produto já esteja salvo, ele verifica se houve alteração no preço, caso haja, salva o novo preço.

## 💻 Pré-requisitos

Antes de começar, verifique os seguintes requisitos:

+ [Python](https://www.python.org/downloads/)
+ [Pip](https://pip.pypa.io/en/stable/installation/)

## 🧰 Linguagens utilizadas
+ ![GitHub top language](https://img.shields.io/github/languages/top/OwlGuilherme/PyMercado-Livre-Scrapper)

## ⚙️ Utilização
+ Abra o seu terminal
+ Faça o download do repositório com o comando:
```
git clone https://github.com/OwlGuilherme/PyMercado-Livre-Scrapper
```
+ Entre na pasta do projeto com o comando:
```
cd Python-Scrapper
```
+ Crie um ambiente virtual e ative o ambiente (opcional):
```
python -m venv scrapper-env && source scrapper-env/bin/activate
```
+ Instale as dependências do projeto:
```
pip install -r requirements.txt
```
+ Instale os navegadores do PlayWright:
```
playwright install
```
+ Execute a aplicação
```
python3 main.py
```
+ Com a aplicação rodando no terminal, insira o link do produto que deseja rapas
+ Após pressionar Enter, a aplicação irá salvar os dados no produto e encerrar a execução.

## 📮 Contribuindo com o PyMercado-Livre-Scrapper

Para contribuir com o projeto, siga estas etapas:

1. _Fork_ este repositório.
2. Clone o seu repositório _forkado_ com o comando _git clone <link do repositório>_.
3. Faça suas alterações e confirme-as: _git commit -m '<mensagem_commit>'_
4. Envie para o branch original: _git push origin <nome_do_projeto> / <local>_
5. Crie a solicitação de pull.

+ Caso queira me mandar uma mensagem, fique à vontade:

[E-mail](malito:guilhermesantos.adv@protonmail.com)
[Twitter](https://twitter.com/Guilher_me99)
