import requests

def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Moeda: {info['name']}")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Valor mínimo: R$ {info['low']}")
            print(f"Valor máximo: R$ {info['high']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro na consulta.")

moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda_usuario)
