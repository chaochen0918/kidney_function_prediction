import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# --------------------------------------------------------------------------
# read data
# --------------------------------------------------------------------------
project_folder = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_folder, '..', 'data', 'kidney_dataset.csv')
df = pd.read_csv(data_path)

# --------------------------------------------------------------------------
# data overview
# --------------------------------------------------------------------------
df.describe(include='all')
df.info()
# classification output: CKD_Status (imbalanced)
# regression output: GFR
# missing data column: Medication
# numerical data: Creatinine, BUN, Urine_Output, Age, Protein_in_Urine, Water_Intake
# categorical data: Diabetes, Hypertension, Medication
# --------------------------------------------------------------------------
# visualization
# --------------------------------------------------------------------------
# univariate
numeric_cols = ['Creatinine', 'BUN', 'Urine_Output', 'Age', 'Protein_in_Urine', 'Water_Intake']
for col in numeric_cols:
    plt.scatter(x=df[col], y=df['CKD_Status'])
    plt.xlabel(col)
    plt.ylabel('CKD_Status')
    plt.show()


# Diabetes bar chart
df['Diabetes_Status'] = df['Diabetes'].map({0: 'No Diabetes', 1: 'Diabetes'})
df['CKD_Des'] = df['CKD_Status'].map({0: 'No CKD', 1: 'CKD'})

plt.figure(figsize=(10, 6))
# 'x' is the primary grouping, 'hue' is the secondary grouping
sns.countplot(x='Diabetes_Status', hue='CKD_Des', data=df, palette='Set1') 
plt.xlabel('Diabetes Status')
plt.ylabel('Count of Patients')
plt.legend(title='CKD Status')
plt.show()

# Hypertension
df['Hypertension_Status'] = df['Hypertension'].map({0: 'No Hypertension', 1: 'Hypertension'})
# df['CKD_Des'] = df['CKD_Status'].map({0: 'No CKD', 1: 'CKD'})

plt.figure(figsize=(10, 6))
# 'x' is the primary grouping, 'hue' is the secondary grouping
sns.countplot(x='Hypertension_Status', hue='CKD_Des', data=df, palette='Set1') 
plt.xlabel('Hypertension Status')
plt.ylabel('Count of Patients')
plt.legend(title='CKD Status')
plt.show()

# Medication
df['Medication_new'] = df['Medication'].fillna('Null')
plt.figure(figsize=(10, 6))
# 'x' is the primary grouping, 'hue' is the secondary grouping
sns.countplot(x='Medication_new', hue='CKD_Des', data=df, palette='Set1') 
plt.xlabel('Medication Type')
plt.ylabel('Count of Patients')
plt.legend(title='CKD Status')
plt.show()

# --------------------------------------------------------------------------
# summary classification
# --------------------------------------------------------------------------
# - imbalanced ckd label -> handle w/ imbalanced approach
# - Medication have missing data -> replace using 'Null'
# - right skewed: Creatinine, BUN, Protein_in_Urine -> ??? remove outlier ???
# - looks correlated: Creatinine, BUN, Urine_Output (another variable to split)

