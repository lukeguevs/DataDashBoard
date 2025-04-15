import pandas as pd
from typing import Dict, Optional

class MultiDatasetReader:
    def __init__(self):
        self.datasets: Dict[str, pd.DataFrame] = {}
        self.column_maps: Dict[str, Dict[str, str]] = {}

    def register_dataset(self, name: str, file_path: str, column_map: Dict[str, str]):
        df = pd.read_csv(file_path)
        self.datasets[name] = df
        self.column_maps[name] = column_map

    def get_column(self, dataset: str, key: str) -> str:
        return self.column_maps[dataset].get(key, key)

    def get_unique_values(self, dataset: str, key: str):
        df = self.datasets[dataset]
        col = self.get_column(dataset, key)
        return df[col].unique()

    def filter(self, dataset: str, **kwargs) -> pd.DataFrame:
        df = self.datasets[dataset].copy()
        for key, value in kwargs.items():
            col = self.get_column(dataset, key)
            df = df[df[col] == value]
        return df

    def get_filtered_for_plot(self, dataset: str, **kwargs) -> pd.DataFrame:
        df = self.filter(dataset, **kwargs)
        sort_col = self.column_maps[dataset].get('age_sort')
        if sort_col and sort_col in df.columns:
            df = df.sort_values(by=sort_col)
        return df
