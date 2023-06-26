from playwright.sync_api import Playwright, sync_playwright
import matplotlib.pyplot as plt
import sqlite3
import datetime


def save_to_DB(nome, preço_atual):
    conn = sqlite3.connect('banco.db')
    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute('INSERT INTO dados VALUES (?, ?, ?)', (str(nome), horario, preço_atual))
    conn.commit()
    conn.close()

def obter_dados():
    conn = sqlite3.connect('banco.db')
    cursor = conn.cursor()
    cursor.execute('SELECT produto, horario, precos FROM dados')
    dados = cursor.fetchall()
    conn.close()
    return dados

# Criação do banco de dados
conn = sqlite3.connect('banco.db')
cursor = conn.cursor()
conn.execute('''CREATE TABLE IF NOT EXISTS dados
                (produto TEXT, horario TIMESTAMP, precos REAL)''')

# Etapa de raspagem de dados
with sync_playwright() as sync_p:
    browser = sync_p.firefox.launch()
    page = browser.new_page()

    url = input('Digite o link do produto: ')
    
    page.goto(url)

    elemento_preço = page.query_selector('meta[itemprop="price"]')
    preço_atual = f"R$ {elemento_preço.get_attribute('content')}"

    elemento_nome = page.query_selector('h1.ui-pdp-title')
    nome = elemento_nome.inner_text().strip()

    save_to_DB(nome, preço_atual)

dados = obter_dados()
dados_por_produto = {}

for dado in dados:
    produto, horario, preco = dado
    if produto not in dados_por_produto:
        dados_por_produto[produto] = {'horarios': [], 'precos': []}
    dados_por_produto[produto]['horarios'].append(horario)
    dados_por_produto[produto]['precos'].append(preco)

for produto, dados_produto in dados_por_produto.items():
    horarios = dados_produto['horarios']
    precos = dados_produto['precos']
    plt.plot(horarios, precos, marker='o', label=produto)

plt.xlabel('Horario')
plt.xlabel('Preço')
plt.title('Variações de preços')
plt.legend()
plt.xticks(rotation=45)
plt.show()

conn.close()
