import os
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import data
import pandas as pd


def load_df(name):
    data_path = os.path.join(data.__path__[0], name)
    return pd.read_csv(data_path)


def drop_df(X, dropped_columns):
    result = X.copy()
    for c in dropped_columns:
        result = result.drop(c, axis=1)
    return result


def plot_corr_matrix(df, columns):
    scatter_matrix(df[columns], diagonal="kde")
    plt.show()


def list_corr_matrix(df, identity_column):
    corr_matrix = df.corr()
    corr_matrix[identity_column].sort_values(ascending=False)
