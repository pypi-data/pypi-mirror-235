import logging
import os
import pandas as pd

logger = logging.getLogger(__name__)


class ExcelUtil:
    """ExcelUtil"""

    def __init__(self):
        pass

    @staticmethod
    def get_abstract(file_path: str) -> str:
        _, file_extension = os.path.splitext(file_path)
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension == '.dta':
            df = pd.read_stata(file_path)
        else:
            df = pd.read_excel(file_path)

        num_rows, num_columns = df.shape
        column_names = df.columns.tolist()
        abstract = f"Dataset1 contains {num_rows} rows and {num_columns} columns.\n"
        for column in column_names:
            if pd.api.types.is_numeric_dtype(df[column]):
                mean_value = df[column].mean()
                std_dev = df[column].std()
                max_value = df[column].max()
                min_value = df[column].min()
                abstract += f"The column '{column}' is a continuous variable, with a mean of {mean_value:.2f}, standard deviation of {std_dev:.2f}, maximum value of {max_value:.2f}, and minimum value of {min_value:.2f}\n"
            else:
                unique_values = ", ".join(df[column].unique())
                abstract += f"The column '{column}' contains categorical variables, with unique categories: {unique_values}\n"
        return abstract
