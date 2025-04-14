import pandas as pd

class EmploymentDataReader:
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)
        self.column_map = {
            'year': 'Jahr',
            'age_label': 'AlterLang',
            'age_sort': 'AlterSort',
            'gender': 'GeschlechtLang',
            'gender_sort': 'GeschlechtSort',
            'employment_type': 'TEK1Lang',
            'employment_type_sort': 'TEK1Sort',
            'rate': 'EQT',
            'rate_lower': 'EQT_LowerCL',
            'rate_upper': 'EQT_UpperCL',
        }

    def get_column(self, key: str):
        return self.column_map.get(key, key)

    def get_unique_values(self, key: str):
        col = self.get_column(key)
        return self.df[col].unique()

    def filter(self, **kwargs):
        query_df = self.df.copy()
        for key, value in kwargs.items():
            col = self.get_column(key)
            query_df = query_df[query_df[col] == value]
        return query_df

    def get_filtered_for_plot(self, year: str, gender: str, employment_type: str):
        filtered = self.filter(year=year, gender=gender, employment_type=employment_type)
        return filtered.sort_values(by=self.get_column('age_sort'))
