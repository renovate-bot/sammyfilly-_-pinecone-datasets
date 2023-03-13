__version__ = "0.2.4-alpha"

import warnings

from .dataset import Dataset
from .catalog import Catalog
from . import cfg


catalog = Catalog.load()


def load_dataset(dataset_id: str, **kwargs) -> Dataset:
    """
        Load a dataset from the catalog

        Args:
            dataset_id (str): The name of the dataset to load
            **kwargs: Additional keyword arguments to pass to the Dataset constructor, e.g. `engine='polars'`
    e
        Returns:
            Dataset: A Dataset object

        Examples:
            from pinecone_datasets import load_dataset
            dataset = load_dataset("dataset_name")
    """
    if dataset_id not in catalog.list_datasets(as_df=False):
        raise FileNotFoundError(f"Dataset {dataset_id} not found in catalog")
    else:
        return Dataset(dataset_id, should_load_metadata=True, **kwargs)


def list_datasets(as_df=False) -> list:
    return catalog.list_datasets(as_df=as_df)
