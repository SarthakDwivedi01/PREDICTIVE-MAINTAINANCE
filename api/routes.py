from fastapi import APIRouter
from src.predictor import predict_failure
from src.recommendation import get_maintenance_action

router = APIRouter()

@router.post("/predict")
def make_prediction(sensor_data: dict):
    # 1. Get the prediction
    prediction = predict_failure(sensor_data)
    
    # 2. Get the actionable recommendation based on the prediction
    action = get_maintenance_action(prediction)
    
    # 3. Return the combined response
    return {
        "prediction": prediction,
        "recommended_action": action
    }