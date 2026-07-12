import os

# Automatically find the root project directory (Predictive-Maintenance-AI)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data Paths
RAW_DATA_PATH = os.path.join(BASE_DIR, "data", "raw", "maintenance_data.csv")
PROCESSED_DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "cleaned_data.csv")

# Artifact Paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")