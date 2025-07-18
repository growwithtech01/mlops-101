import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load the dataset
data = pd.read_csv('../data/dataset.csv')

# Preprocess the data
X = data.drop('label', axis=1)  # Features
y = data['label']  # Labels

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'model.joblib')

print("Model training complete and saved as model.joblib")