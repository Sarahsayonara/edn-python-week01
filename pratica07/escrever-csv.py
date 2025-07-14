# Crie um script em Python que escreva dados em um arquivo CSV.
# O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.

import csv

def escrever_csv(caminho_arquivo):
    dados = [
        {"Nome": "Maria", "Idade": 25, "Cidade": "São Paulo"},
        {"Nome": "João", "Idade": 30, "Cidade": "Rio de Janeiro"},
        {"Nome": "Ana", "Idade": 22, "Cidade": "Belo Horizonte"}
    ]

    with open(caminho_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        campos = ["Nome", "Idade", "Cidade"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados)

    print(f"Dados escritos em {caminho_arquivo} com sucesso!")