"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    fill_data,
    estac_test,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=fill_data,
            inputs={"df_formatted": "df_formatted",
                    'n_neighbors': 'params:n_neighbors',
                    'weights': 'params:weights'},
            outputs="df_filled",
            name="fill_data",
        ),
        node(
            func=estac_test,
            inputs={"df_filled": "df_filled"},
            outputs=["estacionarios", "nao_estacionarios"],
            name="estac_test",
        ),        
    ])
 