import pytest
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs

from validclust.validclust import validclust


data, y = make_blobs(n_samples=500, centers=3, n_features=5, random_state=0)


def test_basic_run():
    out_df = validclust(data)
    assert isinstance(out_df, pd.DataFrame)
    assert not out_df.loc['kmeans', 2].isna().any()