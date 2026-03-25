import pandas as pd
from faker import Faker
import os

fake = Faker('pt_BR')

def anonimizar_planilha(caminho_entrada, caminho_saida):
    print(f"Lendo dados de {caminho_entrada}...")

    if not os.path.exists(caminho_entrada):
        print(f"Erro: O arquivo não foi encontrado no caminho '{caminho_entrada}'")
        print("Verifique se você salvou o arquivo com o nome exato dentro da pasta 'data/'.")
        return

    try:
        df = pd.read_csv(caminho_entrada, sep=None, engine='python', encoding='utf-8')
    except Exception as e:
        print("Erro ao tentar ler o conteúdo do CSV: {e}")
        return
    
    print("Anonimizando dados sensíveis...")

    if 'Contato' in df.columns:
        df['Contato'] = [fake.company() for _ in range(len(df))]

    if 'Telefone' in df.columns:
        df['Telefone'] = [fake.phone_number() for _ in range(len(df))]

    df.to_csv(caminho_saida, index=False)
    print(f"Sucesso! Planilha anonimizada salva em: {caminho_saida}")

if __name__ == "__main__":
    arquivo_original = "data/clientes_reais.csv"
    arquivo_anonimizado = "data/clientes_anonimizados.csv"

    anonimizar_planilha(arquivo_original, arquivo_anonimizado)

