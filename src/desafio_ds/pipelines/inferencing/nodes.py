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
    """Este nó gera a predição para o dataset de treino
    
    Args:
        dataframes_dados_teste: dataset de teste para a previsão
        modelos_arima: dicionário com os modelos para cada dataframe
        
    Returns:
        previsoes_teste: dataset com as previsões"""
    
    # Criar um dicionário para armazenar as previsões
    previsoes_dict = {}

    for pais in estacionarios + nao_estacionarios:
        df_teste = dataframes_dados_teste[pais]
        
        print(df_teste)

        # Selecionar as previsões para os anos 2024 a 2028
        previsoes = df_teste[df_teste.index.year >= 2024]['prev_arima']
        
        previsoes_dict[pais] = previsoes.tolist()

    # Criar um DataFrame com as previsões
    df_previsoes = pd.DataFrame.from_dict(previsoes_dict, orient='index', columns=range(2024, 2029))


    # MUDA O FORMATO DO DF_FILLED
    # Primeiro, crie uma coluna com o ano em formato de string
    df_filled['ano_str'] = df_filled['ano'].astype(str)

    # Use a função pivot_table para reorganizar o DataFrame
    df_pivot = df_filled.pivot_table(index='pais', columns='ano_str', values='pib')

    # Renomeie as colunas para remover o nome do índice
    df_pivot.columns.name = None

    # Reset o índice para mover "pais" para uma coluna
    df_pivot.reset_index(inplace=True)

    # Exiba o DataFrame pivotado
    print(df_pivot)



    # FAZ O MERGE DOS DOIS
    # Filtrar o df_previsoes para manter apenas os anos de 2024 a 2028
    df_previsoes_2024_2028 = df_previsoes[[2024, 2025, 2026, 2027, 2028]]

    # Realizar a junção dos DataFrames com base na coluna "Pais"
    df_previsoes = pd.merge(df_pivot, df_previsoes_2024_2028, left_on='pais', right_index=True, how='left')

    # Exibir o DataFrame resultante
    print(df_previsoes)


    return df_previsoes