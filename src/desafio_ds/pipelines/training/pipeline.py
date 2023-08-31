"""
This is a boilerplate pipeline 'training'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    year_as_index,
    split_df_country,
    train_test_split,
    train_arima_model,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=year_as_index,
            inputs={"df_filled": "df_filled"},
            outputs="df_w_index",
            name="year_as_index",
        ),  
        node(
            func=split_df_country,
            inputs={"df_w_index": "df_w_index"},
            outputs="dataframes_por_pais",
            name="split_df_country",
        ),  
        node(
            func=train_test_split,
            inputs={"dataframes_por_pais": "dataframes_por_pais"},
            outputs=["dataframes_treino", "dataframes_teste"],
            name="train_test_split",
        ), 
        node(
            func=train_arima_model,
            inputs={"estacionarios": "estacionarios", 
                    "nao_estacionarios": "nao_estacionarios",
                    "dataframes_treino": "dataframes_treino"},
            outputs="modelos_arima",
            name="train_arima_model",
        ),                        
    ])
 