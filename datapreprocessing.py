import pandas as pd

# Load the dataset
file_path = 'data/Indian_Context_Data_Updated.csv'
data = pd.read_csv(file_path)

# Identify numeric columns and fill missing values with the mean
numeric_columns = data.select_dtypes(include=['number']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# Drop rows where the target variable is missing
data.dropna(subset=['Lint Yield (Kg/Harvested Hectare)'], inplace=True)

# Save the preprocessed data
preprocessed_file_path = 'data/preprocessed_data.csv'
data.to_csv(preprocessed_file_path, index=False)

print(f'Preprocessed data saved to {preprocessed_file_path}')
