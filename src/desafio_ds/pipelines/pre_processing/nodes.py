"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.12
"""

import pandas as pd

def rename_column (df: pd.DataFrame):
    """Este nó renomeia a coluna em que constam os valores do PIB para 'ano'
    
    Args:
        df: dataframe original
        
    Returns:
        df_renamed: dataframe com a coluna renomeada"""
    
    df_renamed = df.rename(columns={'Real GDP growth (Annual percent change)': 'ano'})

    return df_renamed


def drop_null_rows(df_renamed: pd.DataFrame):
    """Este nó identifica linhas que contém somente valores nulos, e não se referem a países, e as excluem do dataframe
    
    Args:
        df_renamed: dataframe com a coluna renomeada
        
    Returns:
        df_full: dataframe somente com as linhas referentes a países"""

    df_full = df_renamed.copy()

    # Identifica as linhas nulas
    linhas_nulas = df_full[df_full.isnull().any(axis=1)]

    #Identifica os índices das linhas nulas
    indices = linhas_nulas.index

    # Exclui as linhas nulas e reordena os índices
    df_full.drop(indices, inplace = True)
    df_full.reset_index(drop = True, inplace = True)

    return df_full


def replace_w_null (df_full: pd.DataFrame):
    """Este nó substitui os valores com a string 'no data' para valores nulos (None), para serem preenchidos posteriormente
    
    Args:
        df: dataframe só com as linhas dos países
        
    Returns:
        df_w_null: dataframe com None nos valores que não possuem dados"""
    
    df_w_null = df_full.copy()

    df_w_null.replace('no data', None, inplace = True)

    return df_w_null


def format_df (df_w_null: pd.DataFrame, lista_regioes):
    """Este nó formata o dataframe para que feature engineering e modelagem com as seguintes etapas: 
        - transforma as colunas de países para uma coluna chamada país, 
        - preserva somente os países para a modelagem das séries temporais e 
        - organiza em ordem alfabética e cronológica
    
    Args:
        df_w_null: dataframe com None nos valores que não possuem dados
        lista_grupos: lista com os agrupamentos contidos no dataframe original
        
    Returns:
        df_formatted: dataframe formatado para os próximos pipelines"""
    
    # Transforma as colunas dos paises em uma coluna com os valores dos países e renomeia as colunas
    df_formatted = df_w_null.melt(id_vars='ano', var_name='pais', value_name='pib')
    df_formatted = df_formatted.rename(columns={'ano':'pais', 'pais':'ano'})

    # Filtra somente os países ao excluir as linhas referentes a agrupamentos, como regiões econômicas
    df_formatted = df_formatted[~df_formatted['pais'].isin(lista_regioes)]

    # Organiza as linhas dos países por ordem alfabética e cronológica, respectivamente
    df_formatted = df_formatted.sort_values(by=['pais', 'ano'])
    
    return df_formatted