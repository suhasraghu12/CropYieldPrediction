import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

# Load the preprocessed data
preprocessed_file_path = 'data/preprocessed_data.csv'
data = pd.read_csv(preprocessed_file_path)

# Select features and target variable
features = data.drop(columns=['State', 'Year', 'Lint Yield (Kg/Harvested Hectare)'])
target = data['Lint Yield (Kg/Harvested Hectare)']

# Ensure all feature columns are numeric
features = features.select_dtypes(include=['number'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train a Random Forest Regressor model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the trained model
model_file_path = 'app/models/trained_model.pkl'
joblib.dump(model, model_file_path)

print(f'Model saved to {model_file_path}')
