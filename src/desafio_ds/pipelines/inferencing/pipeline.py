"""
This is a boilerplate pipeline 'inferencing'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    generate_prediction,
    save_prediction,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=generate_prediction,
            inputs={"dataframes_teste": "dataframes_teste",
                    "modelos_arima": "modelos_arima"},
            outputs="dataframes_dados_teste",
            name="generate_prediction",
        ),          
        node(
            func=save_prediction,
            inputs={"dataframes_dados_teste": "dataframes_dados_teste",
                    "estacionarios": "estacionarios",
                    "nao_estacionarios": "nao_estacionarios",
                    "df_filled": "df_filled"},
            outputs="df_previsoes",
            # outputs=None,
            name="save_prediction",
        ),          
    ])