import streamlit as st
import requests

# Page Configuration
st.set_page_config(page_title="CNC Predictive Maintenance Dashboard", layout="centered")

st.title("⚙️ CNC Machine Predictive Maintenance Dashboard")
st.markdown("Enter your CNC machine telemetry parameters below to check its operational status via the FastAPI backend.")

# Form inputs for features
st.subheader("🎛️ Sensor Telemetry Inputs")

air_temp = st.number_input("Air Temperature [K]", min_value=250.0, max_value=350.0, value=298.0, step=0.1)
process_temp = st.number_input("Process Temperature [K]", min_value=250.0, max_value=360.0, value=308.5, step=0.1)
rotational_speed = st.number_input("Rotational Speed [rpm]", min_value=500, max_value=5000, value=1550, step=10)
torque = st.number_input("Torque [Nm]", min_value=0.0, max_value=150.0, value=40.0, step=0.5)
tool_wear = st.number_input("Tool Wear [min]", min_value=0, max_value=500, value=10, step=1)
machine_type = st.selectbox("Machine Type", ["L", "M", "H"])

# Prediction Trigger Button
if st.button("Send to API & Run Prediction"):
    payload = {
        "air_temperature": air_temp,
        "process_temperature": process_temp,
        "rotational_speed": rotational_speed,
        "torque": torque,
        "tool_wear": tool_wear,
        "machine_type": machine_type
    }
    
    try:
        # Send POST request to your running FastAPI backend
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.markdown("---")
            st.subheader("📊 API Analysis Result")
            
            # Safely get variables and guarantee they are strings/numbers
            status = result.get("status")
            if status is None:
                status = "Normal"  # Default fallback if key is missing
                
            confidence = result.get("confidence_score", 0.0)
            message = result.get("message", "Parameters look good.")
            
            # Safe checking conversion
            status_str = str(status)
            
            if "Warning" in status_str or "Failure" in status_str:
                st.error(f"🚨 **Status: {status}** (Confidence: {confidence}%)")
                st.markdown(f"**Recommendation:** {message}")
            else:
                st.success(f"✅ **Status: {status}** (Confidence: {confidence}%)")
                st.markdown(f"**Details:** {message}")