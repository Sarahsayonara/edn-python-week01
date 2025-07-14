# Crie um script em Python que leia e escreva dados em um arquivo JSON. 
# O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.

import json

def escrever_json(caminho_arquivo):
    pessoa = {
        "nome": "Carlos",
        "idade": 28,
        "cidade": "Curitiba"
    }

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print(f"Arquivo JSON '{caminho_arquivo}' criado com sucesso!")

def ler_json(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        pessoa = json.load(arquivo)
        print(f"Nome: {pessoa['nome']}")
        print(f"Idade: {pessoa['idade']}")
        print(f"Cidade: {pessoa['cidade']}")