import streamlit as st
import requests

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------

st.set_page_config(
    page_title="CNC Predictive Maintenance",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(0, 150, 255, 0.08), transparent 25%),
        radial-gradient(circle at 90% 90%, rgba(0, 255, 170, 0.05), transparent 25%),
        #071018;
    color: #e6edf3;
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1450px;
}

/* Main title */
.main-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.1rem;
    font-weight: 700;
    letter-spacing: -1px;
    color: #f0f6fc;
    margin-bottom: 0.2rem;
}

.subtitle {
    color: #7d8b99;
    font-size: 0.9rem;
    font-family: 'JetBrains Mono', monospace;
}

/* Header status */
.system-status {
    border: 1px solid #1d394b;
    background: rgba(9, 24, 34, 0.85);
    padding: 12px 18px;
    border-radius: 8px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #7ee787;
    text-align: center;
}

/* Section headings */
.section-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.9rem;
    font-weight: 600;
    color: #58a6ff;
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid #1c303c;
    padding-bottom: 10px;
    margin-top: 20px;
    margin-bottom: 18px;
}

/* Panels */
.panel {
    background: rgba(10, 23, 32, 0.92);
    border: 1px solid #1d394b;
    border-radius: 10px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

/* Metric cards */
.metric-card {
    background: #0b1923;
    border: 1px solid #1d394b;
    border-radius: 8px;
    padding: 18px;
    min-height: 105px;
}

.metric-label {
    color: #718596;
    font-size: 0.72rem;
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.8px;
}

.metric-value {
    color: #e6edf3;
    font-size: 1.55rem;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    margin-top: 8px;
}

.metric-unit {
    color: #58a6ff;
    font-size: 0.75rem;
}

/* Result panel */
.result-normal {
    border: 1px solid #238636;
    background: rgba(35, 134, 54, 0.08);
    border-radius: 10px;
    padding: 22px;
}

.result-warning {
    border: 1px solid #d29922;
    background: rgba(210, 153, 34, 0.08);
    border-radius: 10px;
    padding: 22px;
}

.result-critical {
    border: 1px solid #f85149;
    background: rgba(248, 81, 73, 0.08);
    border-radius: 10px;
    padding: 22px;
}

/* Technical text */
.tech-text {
    font-family: 'JetBrains Mono', monospace;
    color: #9da9b3;
    font-size: 0.8rem;
}

/* Button */
.stButton > button {
    width: 100%;
    height: 48px;
    background: #0d419d;
    color: white;
    border: 1px solid #58a6ff;
    border-radius: 7px;
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    letter-spacing: 0.5px;
    transition: 0.2s;
}

.stButton > button:hover {
    background: #1558c0;
    border-color: #79c0ff;
}

/* Input fields */
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #0b1923 !important;
    color: #e6edf3 !important;
    border-color: #1d394b !important;
}

/* Progress */
.stProgress > div > div {
    background-color: #58a6ff;
}

/* Hide Streamlit footer/menu */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

header_col1, header_col2 = st.columns([4, 1])

with header_col1:

    st.markdown(
        '<div class="main-title">⚙ CNC MACHINE / PREDICTIVE MAINTENANCE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'AI-BASED INDUSTRIAL CONDITION MONITORING SYSTEM // v1.0'
        '</div>',
        unsafe_allow_html=True
    )

with header_col2:

    st.markdown(
        '<div class="system-status">● SYSTEM ONLINE<br>'
        '<span style="color:#718596">API : 8000</span></div>',
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# SYSTEM OVERVIEW
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">SYSTEM OVERVIEW</div>',
    unsafe_allow_html=True
)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Model</div>
        <div class="metric-value">RF-100</div>
        <div class="metric-unit">RANDOM FOREST</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Inference</div>
        <div class="metric-value">ONLINE</div>
        <div class="metric-unit">REAL-TIME API</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Machine</div>
        <div class="metric-value">CNC</div>
        <div class="metric-unit">INDUSTRIAL UNIT</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-label">Protocol</div>
        <div class="metric-value">HTTP</div>
        <div class="metric-unit">FASTAPI BACKEND</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------------

left, right = st.columns([1.1, 0.9], gap="large")


# =========================================================
# LEFT - SENSOR INPUTS
# =========================================================

with left:

    st.markdown(
        '<div class="section-title">◈ SENSOR TELEMETRY INPUT</div>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    air_temp = st.number_input(
        "Air Temperature [K]",
        min_value=250.0,
        max_value=350.0,
        value=298.0,
        step=0.1
    )

    process_temp = st.number_input(
        "Process Temperature [K]",
        min_value=250.0,
        max_value=360.0,
        value=308.5,
        step=0.1
    )

    rotational_speed = st.number_input(
        "Rotational Speed [rpm]",
        min_value=500,
        max_value=5000,
        value=1550,
        step=10
    )

    torque = st.number_input(
        "Torque [Nm]",
        min_value=0.0,
        max_value=150.0,
        value=40.0,
        step=0.5
    )

    tool_wear = st.number_input(
        "Tool Wear [min]",
        min_value=0,
        max_value=500,
        value=10,
        step=1
    )

    machine_type = st.selectbox(
        "Machine Type",
        ["L", "M", "H"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        '<div class="tech-text">'
        'INPUT SOURCE :: MANUAL TELEMETRY<br>'
        'PROCESSING :: FASTAPI INFERENCE ENGINE'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    run_prediction = st.button(
        "▶  EXECUTE ML PREDICTION"
    )


# =========================================================
# RIGHT - MACHINE VISUALIZATION
# =========================================================

with right:

    st.markdown(
        '<div class="section-title">◈ MACHINE MONITOR</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="panel" style="text-align:center;">

        <div style="
            font-family:'JetBrains Mono';
            color:#58a6ff;
            font-size:0.8rem;
            margin-bottom:20px;">
            MACHINE UNIT // CNC-001
        </div>

        <div style="
            font-size:110px;
            line-height:1;
            margin:20px;">
            ⚙️
        </div>

        <div style="
            color:#7d8b99;
            font-family:'JetBrains Mono';
            font-size:0.75rem;">
            ROTATIONAL SYSTEM<br>
            INDUSTRIAL CNC ASSEMBLY
        </div>

        <div style="
            margin-top:25px;
            padding:12px;
            border:1px solid #1d394b;
            border-radius:6px;
            background:#08141d;">
            <span style="color:#7ee787;">●</span>
            <span style="
                font-family:'JetBrains Mono';
                color:#9da9b3;">
                TELEMETRY READY
            </span>
        </div>

    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

if run_prediction:

    payload = {
        "air_temperature": air_temp,
        "process_temperature": process_temp,
        "rotational_speed": rotational_speed,
        "torque": torque,
        "tool_wear": tool_wear,
        "machine_type": machine_type
    }

    with st.spinner("Running Random Forest inference..."):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload,
                timeout=10
            )

            if response.status_code == 200:

                result = response.json()

                status = result.get("status", "Unknown")
                probability = result.get(
                    "failure_probability",
                    0
                )
                message = result.get(
                    "message",
                    "No analysis available."
                )
                recommendation = result.get(
                    "recommended_action",
                    "No recommendation available."
                )

                st.markdown(
                    '<div class="section-title">◈ AI INFERENCE RESULT</div>',
                    unsafe_allow_html=True
                )

                if status == "Critical":

                    st.markdown(
                        f"""
                        <div class="result-critical">
                            <div class="metric-label">
                                MACHINE CONDITION
                            </div>
                            <div style="
                                font-family:'JetBrains Mono';
                                font-size:1.8rem;
                                font-weight:700;
                                color:#f85149;
                                margin-top:8px;">
                                ⚠ CRITICAL
                            </div>
                            <div class="tech-text" style="margin-top:10px;">
                                FAILURE PROBABILITY :: {probability}%
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                elif status == "Warning":

                    st.markdown(
                        f"""
                        <div class="result-warning">
                            <div class="metric-label">
                                MACHINE CONDITION
                            </div>
                            <div style="
                                font-family:'JetBrains Mono';
                                font-size:1.8rem;
                                font-weight:700;
                                color:#d29922;
                                margin-top:8px;">
                                ⚠ WARNING
                            </div>
                            <div class="tech-text" style="margin-top:10px;">
                                FAILURE PROBABILITY :: {probability}%
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                else:

                    st.markdown(
                        f"""
                        <div class="result-normal">
                            <div class="metric-label">
                                MACHINE CONDITION
                            </div>
                            <div style="
                                font-family:'JetBrains Mono';
                                font-size:1.8rem;
                                font-weight:700;
                                color:#7ee787;
                                margin-top:8px;">
                                ✓ NORMAL
                            </div>
                            <div class="tech-text" style="margin-top:10px;">
                                FAILURE PROBABILITY :: {probability}%
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.write("")

                # Probability
                st.markdown(
                    '<div class="panel">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="metric-label">'
                    'FAILURE PROBABILITY'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.progress(
                    min(float(probability) / 100, 1.0)
                )

                st.markdown(
                    f"""
                    <div style="
                        font-family:'JetBrains Mono';
                        font-size:2rem;
                        font-weight:700;
                        color:#58a6ff;
                        margin-top:8px;">
                        {probability}%
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)

                # Analysis
                st.markdown(
                    '<div class="panel">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="metric-label">AI ANALYSIS</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="tech-text" style="margin-top:10px;">'
                    f'{message}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)

                # Recommendation
                st.markdown(
                    '<div class="panel">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="metric-label">'
                    'MAINTENANCE RECOMMENDATION'
                    '</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="tech-text" style="margin-top:10px;">'
                    f'{recommendation}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)

            else:

                st.error(
                    f"API ERROR :: HTTP {response.status_code}"
                )

                st.code(response.text)

        except requests.exceptions.ConnectionError:

            st.error(
                "CONNECTION ERROR :: FASTAPI SERVER NOT AVAILABLE"
            )

        except requests.exceptions.Timeout:

            st.error(
                "TIMEOUT :: PREDICTION SERVER DID NOT RESPOND"
            )

        except Exception as e:

            st.error(
                f"UNEXPECTED ERROR :: {str(e)}"
            )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    """
    <div style="
        margin-top:50px;
        border-top:1px solid #1c303c;
        padding-top:15px;
        text-align:center;
        color:#52616d;
        font-family:'JetBrains Mono';
        font-size:0.7rem;">
        PREDICTIVE MAINTENANCE AI // RANDOM FOREST INFERENCE ENGINE
        // FASTAPI + STREAMLIT
    </div>
    """,
    unsafe_allow_html=True
)