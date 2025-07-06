from datetime import date

def idade_em_dias(ano_nascimento):
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

print(f"Idade em dias: {idade_em_dias(1987)}")