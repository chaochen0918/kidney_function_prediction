import pandas as pd
import os

# --------------------------------------------------------------------------
# read data
# --------------------------------------------------------------------------
project_folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_folder, '..', 'data', 'kidney_dataset.csv')
df = pd.read_csv(data_path)

# --------------------------------------------------------------------------
# fill null values
# --------------------------------------------------------------------------
df['Medication'] = df['Medication'].fillna('Null')

# --------------------------------------------------------------------------
# output csv
# --------------------------------------------------------------------------
saved_path = os.path.join(project_folder, '..', 'data', 'kidney_data_processed.csv')
df.to_csv(saved_path)