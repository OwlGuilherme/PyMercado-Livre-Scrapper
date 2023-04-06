from playwright.sync_api import Playwright, sync_playwright
import json

jsonFile = 'produtos.json'


with sync_playwright() as sync_p:
    browser = sync_p.firefox.launch()
    page = browser.new_page()

    url = input('Digite o link do produto: ')

    # Verifica os produtos já cadastrados, caso exista algum
    try:
        with open(jsonFile, 'r') as f:
            produtos = json.load(f)
    except FileExistsError:
        produtos = []

    # Verifica as informações do produto
    produto_cadastrado = None
    for produto in produtos:
        if produto['url'] == url:
            produto_cadastrado = produto
            break

    # Verifica se houve alteração no preço do produto
    if produto_cadastrado:
        page.goto(url)
        elemento_preço = page.query_selector('meta[itemprop="price"]')
        preço_atual = f"R$ {elemento_preço.get_attribute('content')}"

        if preço_atual != produto_cadastrado['preco']:
            # Atualiza o preço do produto
            produto_cadastrado['preco'] = preço_atual
            with open(jsonFile, 'w') as f:
                json.dump(produtos, f)
                print('Atualização do preço realizada com sucesso!!!')

        else:
            print('Não houve alteração no preço do produto')

    else:
        # Produto novo
        page.goto(url)

        elemento_preço = page.query_selector('meta[itemprop="price"]')
        preço_atual = f"R$ {elemento_preço.get_attribute('content')}"

        elemento_nome = page.query_selector('h1.ui-pdp-title')
        nome = elemento_nome.inner_text().strip()

        produto_novo = {'url': url, 'nome': nome, 'preco': preço_atual}
        produtos.append(produto_novo)

        with open(jsonFile, 'w') as f:
            json.dump(produtos, f)
            print('Produto adicionado com sucesso!!!')

    browser.close()
