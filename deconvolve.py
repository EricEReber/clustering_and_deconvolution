# import all libraries you need here
import pandas as pd
import numpy as np
import pathlib as pl
import scanpy as sc

path_data = pl.Path("/home/eric/ethz/sem3/mlg/tme/")

all_bulkified = pd.read_csv(path_data / "train_adata/bulkified_data.csv",index_col=0)

train_adata = sc.read_h5ad(path_data / "train_adata/train_adata.h5ad")
test_adata = sc.read_h5ad(path_data / "test_adata/test_adata.h5ad")
