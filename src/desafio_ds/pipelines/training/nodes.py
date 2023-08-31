"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.12
"""

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def year_as_index (df_filled: pd.DataFrame):
    """Este nó formata o dataframe para que o seu índice seja o ano, no formato datetime, para a modelagem
    
    Args:
        df_filled: dataframe com os valores nulos preenchidos
        
    Returns:
        df_w_index: dataframe com o ano como índice"""
    
    df_w_index = df_filled.copy()
    df_w_index.set_index("ano", inplace=True)
    df_w_index.index = pd.to_datetime(df_w_index.index, format="%Y").to_period("A")

    return df_w_index 


def split_df_country (df_w_index: pd.DataFrame):
    """Este nó cria um dicionário de dataframes, um para cada país, para o treino do modelo
    
    Args:
        df_w_index: dataframe com o ano como índice
        
    Returns:
        dataframes_por_pais: dicionário com um dataframe por país, com as colunas ano (índice), país e pib"""
    
    # Cria um dicionário para receber os dataframes
    dataframes_por_pais = {}

    # Agrupa o dataframe preenchido por país
    grupo_paises = df_w_index.groupby('pais')

    # Itera sobre os grupos dos países, seleciona as colunas que serão mantidas, cria um dataframe para cada país e armazena em um dicionário chamado 'dataframes_por_pais'
    for pais, grupo in grupo_paises:
        df_pais = grupo.copy()
        dataframes_por_pais[pais] = df_pais

    return dataframes_por_pais 


def train_test_split (dataframes_por_pais):
    """Este nó cria dois dicionários, um para os dataframes de treino e outro para os dataframes de teste, sendo um dataframe para cada país
    
    Args:
        dataframes_por_pais: dicionário com um dataframe por país, com as colunas ano, país e pib
        
    Returns:
        dataframes_treino: dicionário com um dataframe por país, para a etapa de treino do modelo
        dataframes_teste: dicionário com um dataframe por país para o a etapa de teste (previsões)"""
    
    # Cria os dicionários para armazenar os dataframes de treino e de teste
    dataframes_treino = {}
    dataframes_teste = {}

    # Itera sobre o dicionário da função anterior e separa os dataframes para treino e teste, sendo de treino dos anos 1980 a 2023 e teste de 2024 a 2028
    for nome, df_parte in dataframes_por_pais.items():
        df_treino = df_parte[df_parte.index <= pd.Period('2023', freq='A')].copy()
        df_teste = df_parte[df_parte.index > pd.Period('2023', freq='A')].copy()
        dataframes_treino[nome] = df_treino
        dataframes_teste[nome] = df_teste

    return dataframes_treino, dataframes_teste


def train_arima_model (estacionarios, nao_estacionarios, dataframes_treino):
    """Este nó cria um dicionário para armazenar o modelo ARIMA para cada país, uma vez que os parâmetros do modelo são diferentes para os países estacionários e não estacionários
    
    Args:
        estacionarios: lista dos países estacionários pelo teste ADF
        nao_estacionarios:lista dos países não estacionários pelo teste ADF
        dataframes_treino: dicionário com um dataframe por país, para a etapa de treino do modelo
        
    Returns:
        modelos_arima: dicionário com um modelo ARIMA por país"""
    
    # Cria um dicionário para armazenar os modelos para cada dataframe
    modelos_arima = {}

    # Itera sobre os países que estão na lista dos estacionários e treina o modelo ARIMA para cada dataframe
    for pais in estacionarios:
        df_treino = dataframes_treino[pais]
        modelo = ARIMA(endog=df_treino['pib'], order=(1, 0, 1)).fit()
        modelos_arima[pais] = modelo

    # Itera sobre os países que estão na lista dos não estacionários e treina o modelo ARIMA para cada dataframe
    for pais in nao_estacionarios:
        df_treino = dataframes_treino[pais]
        modelo = ARIMA(endog=df_treino['pib'], order=(1, 1, 1)).fit()
        modelos_arima[pais] = modelo

    return modelos_arima