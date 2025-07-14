# Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
# O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv

def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(f"Nome: {linha['Nome']}, Idade: {linha['Idade']}, Cidade: {linha['Cidade']}")
