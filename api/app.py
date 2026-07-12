from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Predictive Maintenance API", version="1.0")

# Include the routes defined in routes.py
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Predictive Maintenance API is running."}