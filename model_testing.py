# model_testing.py

import pandas as pd
import pickle
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("Dataset/heart_attack_10000.csv")

df.head();
df.info();
df.describe();
df.columns();

FEATURES = [
    'age','sex','cp','trestbps','chol','fbs','restecg',
    'thalach','exang','oldpeak','slope','ca','thal'
]

X = df[FEATURES]
y = df['target']

# Same split as training
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Load trained model

with open("model/heart_model.pkl", "rb") as f:

    model = pickle.load(f)

# Predictions
preds = model.predict(X_test)

print("Accuracy :", accuracy_score(y_test, preds))
print("Precision:", precision_score(y_test, preds))
print("Recall   :", recall_score(y_test, preds))
print("F1 Score :", f1_score(y_test, preds))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, preds))

