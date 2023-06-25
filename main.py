from playwright.sync_api import Playwright, sync_playwright
import matplotlib.pyplot as plt
import sqlite3
import datetime

# Função para salvar dados no banco de dados
def save_to_DB(nome, preço_atual):
    conn = sqlite3.connect('banco.db')
    horario = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute('INSERT INTO dados VALUES (?, ?, ?)', (str(nome), horario, preço_atual))
    conn.commit()
    conn.close()

# Função para obter os dados do banco de dados
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
produtos, horarios, precos = zip(*dados)
horarios = [datetime.datetime.strptime(h, '%Y-%m-%d %H:%M:%S') for h in horarios]

# Plotar o gráfico
plt.plot(horarios, precos, marker='o')
plt.xlabel('Horário')
plt.ylabel('Preço')
plt.title('Variação de Preços')
plt.xticks(rotation=45)
plt.show()

conn.close()
