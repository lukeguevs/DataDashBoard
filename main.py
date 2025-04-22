import pandas as pd
from reader.MultiDatasetReader import MultiDatasetReader
import matplotlib.pyplot as plt

reader = MultiDatasetReader()

reader.register_dataset(
    name="employment_rate",
    file_path="data/EmployementRate.csv",
    column_map={
        "year": "Jahr",
        "age_group_description": "AlterLang",
        "age_group_sort_order": "AlterSort",
        "gender_description": "GeschlechtLang",
        "gender_sort_order": "GeschlechtSort",
        "employment_type_description": "TEK1Lang",
        "employment_type_sort_order": "TEK1Sort",
        "rate": "EQT",
        "rate_lower_confidence_limit": "EQT_LowerCL",
        "rate_upper_confidence_limit": "EQT_UpperCL"
    }
)

reader.register_dataset(
    name="median_salary_per_person",
    file_path="data/MedianSalary.csv",
    column_map={
        "year": "StichtagDatJahr",
        "age_group_sort_order": "QuarSort",
        "age_group_description": "QuarCd",
        "gender_description": "QuarLang",
        "tax_sort": "SteuerTarifSort",
        "tax_description": "SteuerTarifLang",
        "tax_code": "SteuerTarifCd",
        "median_salary": "SteuerEinkommen_p50"
    }
)

reader.register_dataset(
    name="median_salary_per_person",
    file_path="data/MedianSalary.csv",
    column_map={
        "year": "StichtagDatJahr",
        "age_group_sort_order": "QuarSort",
        "age_group_description": "QuarCd",
        "gender_description": "QuarLang",
        "tax_sort": "SteuerTarifSort",
        "tax_code": "SteuerTarifCd",
        "tax_description": "SteuerTarifLang",
        "median_salary": "SteuerEinkommen_p50",
        "lower_quartile_salary": "SteuerEinkommen_p25",
        "upper_quartile_salary": "SteuerEinkommen_p75"
    }
)

reader.register_dataset(
    name="median_wealth_people",
    file_path="data/MedianWealthPeople.csv",
    column_map={
        "year": "StichtagDatJahr",
        "age_group_sort_order": "QuarSort",
        "age_group_description": "QuarCd",
        "gender_description": "QuarLang",
        "tax_sort": "SteuerTarifSort",
        "tax_code": "SteuerTarifCd",
        "tax_description": "SteuerTarifLang",
        "median_wealth": "SteuerVermoegen_p50",
        "lower_quartile_wealth": "SteuerVermoegen_p25",
        "upper_quartile_wealth": "SteuerVermoegen_p75"
    }
)

