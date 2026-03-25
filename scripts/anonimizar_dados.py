import pandas as pd
from faker import Faker
import os
import random
from datetime import datetime, timedelta

fake = Faker('pt_BR')

def anonimizar_e_preencher_planilha(caminho_entrada, caminho_saida):
    print(f"Lendo dados de: {caminho_entrada}...")
    
    if not os.path.exists(caminho_entrada):
        print(f"Erro: O arquivo não foi encontrado no caminho '{caminho_entrada}'.")
        return

    try:
        df = pd.read_csv(caminho_entrada, sep=None, engine='python', encoding='utf-8')
    except Exception as e:
        print(f"Erro ao ler o CSV: {e}")
        return

    print("Anonimizando dados sensíveis e gerando dados financeiros de teste...")
    
    if 'Contato' in df.columns:
        df['Contato'] = [fake.company() for _ in range(len(df))]
        
    if 'Telefone' in df.columns:
        df['Telefone'] = [fake.phone_number() for _ in range(len(df))]

    coluna_valor = 'Valor Compra Semanal'
    if coluna_valor in df.columns:
        vazios = df[coluna_valor].isna() 
        df.loc[vazios, coluna_valor] = [f"{random.uniform(150.0, 800.0):.2f}".replace('.', ',') for _ in range(vazios.sum())]

    coluna_data = 'Data da Última Compra'
    if coluna_data in df.columns:
        df[coluna_data] = df[coluna_data].astype('object')
        vazios = df[coluna_data].isna()
        hoje = datetime.now()
        datas_fake = [(hoje - timedelta(days=random.randint(1, 60))).strftime('%d/%m/%Y') for _ in range(vazios.sum())]
        df.loc[vazios, coluna_data] = datas_fake

    coluna_status = 'Status'
    if coluna_status in df.columns:
        vazios = df[coluna_status].isna()
        df.loc[vazios, coluna_status] = [random.choice(['Ativo', 'Ativo', 'Ativo', 'Inativo']) for _ in range(vazios.sum())]

    df.to_csv(caminho_saida, index=False)
    print(f"Sucesso! Planilha pronta salva em: {caminho_saida}")

if __name__ == "__main__":
    arquivo_original = "data/clientes_reais.csv" 
    arquivo_anonimizado = "data/clientes_anonimizados.csv"
    
    anonimizar_e_preencher_planilha(arquivo_original, arquivo_anonimizado)

