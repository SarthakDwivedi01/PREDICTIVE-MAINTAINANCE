import pandas as pd
import joblib
import os

from src.utils import logger
from src.config import BASE_DIR


# Use the existing trained model
MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "predictive_maintenance_model.pkl"
)


def predict_failure(sensor_data: dict):
    try:
        logger.info("Initiating prediction sequence...")

        # Load the trained Random Forest model
        model = joblib.load(MODEL_PATH)

        # Get machine type
        machine_type = sensor_data["machine_type"]

        if machine_type not in ["L", "M", "H"]:
            raise ValueError("Machine type must be L, M, or H")

        # Prepare input in the same format used during training
        input_data = pd.DataFrame([{
            "Air temperature [K]": sensor_data["air_temperature"],
            "Process temperature [K]": sensor_data["process_temperature"],
            "Rotational speed [rpm]": sensor_data["rotational_speed"],
            "Torque [Nm]": sensor_data["torque"],
            "Tool wear [min]": sensor_data["tool_wear"],

            # Failure mode features
            "TWF": 0,
            "HDF": 0,
            "PWF": 0,
            "OSF": 0,
            "RNF": 0,

            # Machine type encoding
            "Type_L": 1 if machine_type == "L" else 0,
            "Type_M": 1 if machine_type == "M" else 0
        }])

        # Match exact order expected by trained model
        input_data = input_data[model.feature_names_in_]

        # Actual ML prediction
        prediction = int(model.predict(input_data)[0])

        # Actual probability
        probabilities = model.predict_proba(input_data)[0]

        # Class 1 = machine failure
        failure_probability = float(probabilities[1])

        failure_percentage = round(
            failure_probability * 100,
            2
        )

        # Determine status
        if failure_probability >= 0.70:

            status = "Critical"

            message = (
                "High probability of machine failure. "
                "Immediate maintenance is recommended."
            )

        elif failure_probability >= 0.40:

            status = "Warning"

            message = (
                "Elevated failure probability detected. "
                "Schedule maintenance soon."
            )

        else:

            status = "Normal"

            message = (
                "Machine is operating within the "
                "predicted normal range."
            )

        logger.info(
            f"Prediction successful: "
            f"{failure_percentage}% failure probability, "
            f"prediction={prediction}, "
            f"status={status}"
        )

        return {
            "prediction": prediction,
            "failure_probability": failure_percentage,
            "status": status,
            "message": message
        }

    except Exception as e:

        logger.error(
            f"Prediction failed: {e}"
        )

        raise