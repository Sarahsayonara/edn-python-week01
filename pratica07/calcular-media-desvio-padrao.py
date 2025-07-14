# Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
# Calcule a média e o desvio padrão do tempo de exercução constantes.

import re
import statistics

def analisar_log(caminho_arquivo):
    tempos = []

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            match = re.search(r"tempo de execução\s*:\s*(\d+(?:\.\d+)?)", linha.lower())
            if match:
                tempos.append(float(match.group(1)))

    if tempos:
        media = statistics.mean(tempos)
        desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0.0
        print(f"Média do tempo de execução: {media:.2f} segundos")
        print(f"Desvio padrão: {desvio:.2f}")
    else:
        print("Nenhum tempo de execução encontrado.")
