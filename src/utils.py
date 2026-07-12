import logging
import pickle
import os

# Centralized logger configuration
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(module)s - %(message)s"
)
logger = logging.getLogger("PredictiveMaintenanceLogger")

def save_object(file_path: str, obj):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)
        logger.info(f"Object successfully saved at {file_path}")
    except Exception as e:
        logger.error(f"Failed to save object to {file_path}: {e}")
        raise e

def load_object(file_path: str):
    try:
        with open(file_path, "rb") as f:
            obj = pickle.load(f)
        logger.info(f"Object successfully loaded from {file_path}")
        return obj
    except Exception as e:
        logger.error(f"Failed to load object from {file_path}: {e}")
        raise e