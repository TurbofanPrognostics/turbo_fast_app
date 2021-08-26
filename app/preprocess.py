import pandas as pd
import numpy as np


def drop_empty_cols(df: pd.DataFrame) -> pd.DataFrame:
    """
    Drops empty columns from dataframe
    """
    na_by_col = df.isna().sum()
    row_cnt = df.shape[0]
    cols_to_keep = [True if na_cnt != row_cnt else False for na_cnt in na_by_col]
    return df.iloc[:, cols_to_keep]


def preprocess(df: pd.DataFrame) -> np.ndarray:
    """
    Cleaning input data before training or inference;
    dropping columns that do not have much predictive power; 
    see analysis described below:
    https://towardsdatascience.com/predictive-maintenance-of-turbofan-engines-ec54a083127
    """
    SENSOR_COLS_TO_DROP = [f'sensor_{i}' for i in (1, 5, 6, 10, 16, 18, 19)]
    SETTING_COLS_TO_DROP = [f'op_setting_{i}' for i in range(1, 3+1)]
    COLS_TO_DROP = SENSOR_COLS_TO_DROP + SETTING_COLS_TO_DROP + ['unit_number', 'time']
    return (df.pipe(drop_empty_cols)
              .drop(columns=COLS_TO_DROP))
