import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the dataset
df = pd.read_csv('Data/Crop_recommendation.csv')

X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Model with 20 estimators (matches the existing model)
RF = RandomForestClassifier(n_estimators=20, random_state=42)
RF.fit(X_train, y_train)

# Evaluate
acc = RF.score(X_test, y_test)
print(f"Model trained! Accuracy: {acc*100:.2f}%")

# Save the model
model_path = 'models/RandomForest.pkl'
with open(model_path, 'wb') as f:
    pickle.dump(RF, f)

print(f"Model saved to {model_path} with scikit-learn version!")
