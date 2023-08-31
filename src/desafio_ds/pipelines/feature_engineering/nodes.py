"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.12
"""

import pandas as pd
from sklearn.impute import KNNImputer
from statsmodels.tsa.stattools import adfuller


def fill_data (df_formatted: pd.DataFrame, n_neighbors, weights):
    """Este nó preenche os dados nulos com o algoritmo KNNImputer
    
    Args:
        df_formatted: dataframe formatado para esta etapa e a modelagem
        
    Returns:
        df_filled: dataframe com os valores nulos preenchidos"""
    
    knn_imputer = KNNImputer(n_neighbors=n_neighbors, weights=weights)
    df_filled = df_formatted.copy()
    df_filled['pib'] = knn_imputer.fit_transform(df_filled[['pib']])

    return df_filled 


def estac_test (df_filled: pd.DataFrame):
    """Este nó aplica o teste de Dickey-Fuller aumentado (ADF) para avaliar a estacionariedade das séries temporais e, a partir daí, cria duas listas, separando as séries estacionárias das não estacionárias
    
    Args:
        df_filled: dataframe com os valores nulos preenchidos
        
    Returns:
        estacionarios: lista dos países estacionários conforme o teste ADF
        nao_estacionarios: lista dos países não estacionários conforme o teste ADF"""
    
    # Retorna os valores únicos da coluna 'pais', que são os países do dataframe
    paises = df_filled['pais'].unique()

    # Cria as listas para receber os resultados do teste ADF e a significância do teste
    estacionarios = []
    nao_estacionarios = []
    significancia = 0.05

    # Aplica o teste em todas as séries temporais e salva o resultado na lista respectiva
    for pais in paises:
        data_for_pais = df_filled[df_filled['pais'] == pais]['pib']
        teste_fuller_estac = adfuller(data_for_pais)
        if teste_fuller_estac[1] <= significancia: 
            estacionarios.append(pais)
        else:
            nao_estacionarios.append(pais)

    return estacionarios, nao_estacionarios 