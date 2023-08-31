"""
This is a boilerplate pipeline 'inferencing'
generated using Kedro 0.18.12
"""

import pandas as pd
import matplotlib.pyplot as plt


def generate_prediction(dataframes_teste, modelos_arima):
    """Este nó gera a predição para o dataset de treino
    
    Args:
        dataframes_teste: dataset de teste para a previsão
        modelos_arima: dicionário com os modelos para cada dataframe
        
    Returns:
        dataframes_dados_teste: dataset com as previsões"""
    
    dataframes_dados_teste = dataframes_teste.copy()

    # Itera sobre o dicionário com os modelos para os dataframes de teste e fas as previsões para esse dataframe
    for pais, modelo in modelos_arima.items():
        df_teste = dataframes_dados_teste[pais]
        previsoes_teste = modelo.predict(start=df_teste.index.min(), end=df_teste.index.max())
        df_teste['prev_arima'] = previsoes_teste

    return dataframes_dados_teste


def save_prediction(dataframes_dados_teste, estacionarios, nao_estacionarios, df_filled):
    """Este nó salva as predições dos dados de teste (2024 a 2028) em um dataframe e une com o dataframe dos dados nulos preenchidos com o KNNImputer (1980 a 2023), para cumprir uma das entregas do projeto
    
    Args:
        dataframes_dados_teste: dataset de teste para a previsão
        estacionarios: lista dos países estacionários pelo teste ADF
        nao_estacionarios:lista dos países não estacionários pelo teste ADF
        df_filled: dataframe com os dados nulos preenchidos pelo KNNImputer
        
    Returns:
        df_previsoes: dataset entregável, com os dados preenchidos de 1980 a 2023 e os dados previstos de 2024 a 2028"""
    
    # Cria um dicionário para armazenar as previsões
    previsoes_dict = {}

    # Itera sobre as listas de países, faz as previsões para os anos de 2024 a 2028 e salva no dicionário
    for pais in estacionarios + nao_estacionarios:
        df_teste = dataframes_dados_teste[pais]
        previsoes = df_teste[df_teste.index.year >= 2024]['prev_arima']
        previsoes_dict[pais] = previsoes.tolist()

    # Leva as previsões para um dataframe
    df_previsoes = pd.DataFrame.from_dict(previsoes_dict, orient='index', columns=range(2024, 2029))

    # Muda o formato do arquivo df_filled, transformando-o em pivot, para que as colunas virem os anos e as linhas, os países
    df_filled['ano_str'] = df_filled['ano'].astype(str)
    df_pivot = df_filled.pivot_table(index='pais', columns='ano_str', values='pib')
    df_pivot.columns.name = None
    df_pivot.reset_index(inplace=True)

    # Junta os dataframes df_previsoes para os anos de 2024 a 2028, com o df_filled pivotado com base na coluna "país"
    df_previsoes_2024_2028 = df_previsoes[[2024, 2025, 2026, 2027, 2028]]
    df_previsoes = pd.merge(df_pivot, df_previsoes_2024_2028, left_on='pais', right_index=True, how='left')

    return df_previsoes