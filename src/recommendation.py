from src.utils import logger

def get_maintenance_action(prediction_result: dict):
    try:
        logger.info("Generating maintenance recommendation...")
        # [LOGIC: If probability > threshold, recommend action]
        return "Schedule immediate maintenance for motor bearing."
    except Exception as e:
        logger.error(f"Failed to generate recommendation: {e}")
        raise e