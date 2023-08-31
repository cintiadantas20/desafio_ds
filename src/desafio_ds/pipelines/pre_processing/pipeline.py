"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.12
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import (
    rename_column,
    drop_null_rows,
    replace_w_null,
    format_df,
)

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=rename_column,
            inputs={"df": "pib"},
            outputs="df_renamed",
            name="rename_column",
        ),
       node(
            func=drop_null_rows,
            inputs={"df_renamed": "df_renamed"},
            outputs="df_full",
            name="drop_null_rows",
        ), 
       node(
            func=replace_w_null,
            inputs={"df_full": "df_full"},
            outputs="df_w_null",
            name="replace_w_null",
        ), 
       node(
            func=format_df,
            inputs={"df_w_null": "df_w_null",
                    'lista_regioes': 'params:lista_regioes'},
            outputs="df_formatted",
            name="format_df",
        ),         
    ])
