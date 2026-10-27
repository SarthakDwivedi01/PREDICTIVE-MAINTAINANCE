# src/model_trainer.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# 1. Load the processed data
df = pd.read_csv('data/processed/cleaned_data.csv')

# 2. Prepare Features and Target
X = df.drop(['Machine failure'], axis=1)
y = df['Machine failure']

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)

# 5. Save the trained model for later use
joblib.dump(model, 'models/predictive_maintenance_model.pkl')
print("Model trained and saved to models/ folder!")