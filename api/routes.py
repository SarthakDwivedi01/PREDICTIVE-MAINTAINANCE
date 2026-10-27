from fastapi import APIRouter
from src.predictor import predict_failure
from src.recommendation import get_maintenance_action

router = APIRouter()

@router.post("/predict")
def make_prediction(sensor_data: dict):

    prediction = predict_failure(sensor_data)

    action = get_maintenance_action(prediction)

    return {
        "prediction": prediction.get("prediction"),
        "failure_probability": prediction.get("failure_probability"),
        "status": prediction.get("status"),
        "message": prediction.get("message"),
        "recommended_action": action
    }