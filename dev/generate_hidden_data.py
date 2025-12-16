import pandas as pd
import os

# --------------------------------------------------------------------------
# read data
# --------------------------------------------------------------------------
project_folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_folder, '..', 'data', 'kidney_dataset.csv')
df = pd.read_csv(data_path)

# --------------------------------------------------------------------------
# create hidden dataset
# --------------------------------------------------------------------------
df_hidden = df.sample(frac=0.2, random_state=44)
df_open = df.drop(df_hidden.index)
df_hidden = df_hidden.reset_index(drop=True)
df_open = df_open.reset_index(drop=True)
# --------------------------------------------------------------------------
# output to csv
# --------------------------------------------------------------------------
saved_path_hidden = os.path.join(project_folder, '..', 'data', 'kidney_dataset_hidden.csv')
saved_path_open = os.path.join(project_folder, '..', 'data', 'kidney_dataset_open.csv')
df_hidden.to_csv(saved_path_hidden, index=False)
df_open.to_csv(saved_path_open, index=False)