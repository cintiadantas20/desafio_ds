"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from desafio_ds.pipelines import (
    pre_processing,
    feature_engineering,
    training,
    inferencing,
)

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    pre_processing_pipeline = pre_processing.create_pipeline()
    feature_engineering_pipeline = feature_engineering.create_pipeline()
    training_pipeline = training.create_pipeline()
    inferencing_pipeline = inferencing.create_pipeline()

    default_pipelines = (
        pre_processing_pipeline
        + feature_engineering_pipeline
        + training_pipeline
        + inferencing_pipeline
    )

    return {
        "pre_processing": pre_processing_pipeline,
        "feature_engineering": feature_engineering_pipeline,
        "training": training_pipeline,
        "inferencing": inferencing_pipeline, 
        "__default__": default_pipelines
    }