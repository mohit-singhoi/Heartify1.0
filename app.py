# app.py — Final Prediction App

import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


st.set_page_config(page_title="Heart Attack Prediction - Hertify1.0", page_icon="❤️")

st.title("❤️ Heart Attack Prediction System")
# st.subheader("Welcome to Heartify 1.0 - Your Companion for Heart Health")
st.markdown("###### Welcome to Heartify1.0 it helps you assess your risk of heart disease based on key health indicators. Please provide your details in the sidebar and click on 'Predict Heart Attack Risk' to see your results.");




FEATURES = [
    'age','sex','cp','trestbps','chol','fbs','restecg',
    'thalach','exang','oldpeak','slope','ca','thal'
]

# Load model
with open("model/heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/model_metrics.pkl", "rb") as f:
    metrics = pickle.load(f)


st.sidebar.header("🧍 Patient Details")

# -------------------------
# AGE
# -------------------------
age = st.sidebar.slider("Age (years)", 18, 90, 45)

# -------------------------
# SEX (TEXT → NUMBER)
# -------------------------
sex_text = st.sidebar.selectbox(
    "Sex",
    ["Male", "Female", "Other"]
)
sex = {"Male": 1, "Female": 0, "Other": 0}[sex_text]

# -------------------------
# CHEST PAIN TYPE
# -------------------------
cp_text = st.sidebar.selectbox(
    "Chest Pain Type",
    [
        "Typical Angina",
        "Atypical Angina",
        "Non-anginal Pain",
        "Asymptomatic"
    ]
)
cp = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}[cp_text]

# -------------------------
# RESTING BP
# -------------------------
trestbps = st.sidebar.slider(
    "Resting Blood Pressure (mm Hg)", 80, 200, 120
)

# -------------------------
# CHOLESTEROL
# -------------------------
chol = st.sidebar.slider(
    "Cholesterol (mg/dL)", 100, 400, 200
)

# -------------------------
# FASTING BLOOD SUGAR
# -------------------------
fbs_text = st.sidebar.radio(
    "Fasting Blood Sugar > 120 mg/dL",
    ["No", "Yes"]
)
fbs = {"No": 0, "Yes": 1}[fbs_text]

# -------------------------
# RESTING ECG
# -------------------------
restecg_text = st.sidebar.selectbox(
    "Resting ECG Result",
    [
        "Normal",
        "ST-T Wave Abnormality",
        "Left Ventricular Hypertrophy"
    ]
)
restecg = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}[restecg_text]

# -------------------------
# MAX HEART RATE
# -------------------------
thalach = st.sidebar.slider(
    "Maximum Heart Rate Achieved", 70, 210, 150
)

# -------------------------
# EXERCISE INDUCED ANGINA
# -------------------------
exang_text = st.sidebar.radio(
    "Exercise Induced Angina",
    ["No", "Yes"]
)
exang = {"No": 0, "Yes": 1}[exang_text]

# -------------------------
# OLDPEAK
# -------------------------
oldpeak = st.sidebar.slider(
    "ST Depression (oldpeak)", 0.0, 6.0, 1.0, step=0.1
)

# -------------------------
# SLOPE
# -------------------------
slope_text = st.sidebar.selectbox(
    "Slope of ST Segment",
    ["Upsloping", "Flat", "Downsloping"]
)
slope = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}[slope_text]

# -------------------------
# NUMBER OF VESSELS
# -------------------------
ca = st.sidebar.selectbox(
    "Number of Major Vessels (0–3)", [0, 1, 2, 3]
)

# -------------------------
# THALASSEMIA
# -------------------------
thal_text = st.sidebar.selectbox(
    "Thalassemia",
    ["Normal", "Fixed Defect", "Reversible Defect"]
)
thal = {
    "Normal": 1,
    "Fixed Defect": 2,
    "Reversible Defect": 3
}[thal_text]

# -------------------------
# FINAL DATAFRAME (MODEL INPUT)
# -------------------------
user_df = pd.DataFrame([{
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}])



# -------------------------
# PREDICTION BUTTON
# -------------------------
if st.sidebar.button("🔍 Predict Heart Attack Risk"):

    prediction = model.predict(user_df)[0]
    probability = model.predict_proba(user_df)[0][1]

    st.subheader("🩺 Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    st.write(f"**Risk Probability:** {probability * 100:.2f}%")
    
    # if st.sidebar.button("🔍 Predict Heart Attack Risk"):
    st.subheader("📌 Model Accuracy")
    st.success(f"Accuracy: {metrics['accuracy'] * 100:.2f}%")
    
    st.subheader("📊 Performance Metrics")

    report_df = pd.DataFrame(metrics["report"]).transpose()
    st.dataframe(report_df.style.format("{:.2f}"))
    
    st.subheader("🧮 Confusion Matrix")

    fig, ax = plt.subplots()
    disp = ConfusionMatrixDisplay(confusion_matrix=metrics["confusion_matrix"])
    disp.plot(ax=ax, cmap="Blues", colorbar=False)
    st.pyplot(fig)


    st.subheader("📈 Risk Probability Gauge")


    # Probability Gauge
    fig = go.Figure(go.Indicator( 
        mode="gauge+number",
        value=probability * 100,
        title={"text": "Heart Attack Risk"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "blue"},
            "steps": [
                {"range": [0, 50], "color": "lightgreen"},
                {"range": [50, 100], "color": "orange"}
            ]
        }
    ))
    st.plotly_chart(fig)  
    st.markdown("---")
st.markdown("Developed by Heartify Team ❤️")

#Footer
# st.markdown("© 2025 Heartify1.0. All rights reserved.");
st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; font-size:14.5px; color:#6c757d;">
     <b>Heartify – Future Ready Healthcare AI</b><br><br>
        <b>Real-World Deployment Vision</b><br>
        • Hospital Decision Support Systems<br>
        • IoT & Wearable Health Devices<br>
        • Cloud-based Patient Monitoring<br>
        • Doctor & Patient Dashboards<br><br>

 
        © 2026 Heartify1.0 | All Rights Reserved ❤️
    </div>
    """,
    unsafe_allow_html=True
)

