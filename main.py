from playwright.sync_api import Playwright, sync_playwright
import json

jsonFile = 'produtos.json'


def formata_preço(preço: str) -> str:
    span_preço = preço.split()
    reais = int(span_preço[0])
    centavos = int(span_preço[3])
    return f'R$ {reais},{centavos:02d}'


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
        elemento_preço = page.query_selector('span.andes-visually-hidden')
        preço_atual = elemento_preço.inner_text()
        preço_atual_formatado = formata_preço(preço_atual)

        if preço_atual_formatado != produto_cadastrado['preco']:
            # Atualiza o preço do produto
            produto_cadastrado['preco'] = preço_atual_formatado
            with open(jsonFile, 'w') as f:
                json.dump(produtos, f)
                print(f'''Houve mudança no produto: {produto_cadastrado}
                      Preço atual: {preço_atual_formatado}''')

        else:
            print('Não houve alteração no preço do produto')

    else:
        # Produto novo
        page.goto(url)
        elemento_preço = page.query_selector('span.andes-visually-hidden')
        preço = elemento_preço.inner_text()
        preço_formatdo = formata_preço(preço)

        elemento_nome = page.query_selector('h1.ui-pdp-title')
        nome = elemento_nome.inner_text().strip()

        produto_novo = {'url': url, 'nome': nome, 'preco': preço_formatdo}
        produtos.append(produto_novo)

        with open(jsonFile, 'w') as f:
            json.dump(produtos, f)
            print(f'''Produto adicionado com sucesso!!!
                  Nome: {produto_novo}''')

    browser.clone()
