import streamlit as st
import numpy as np
import joblib
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Happiness Predictor", page_icon="🌍", layout="centered")

# --- Load Model & Scaler ---
# We use st.cache_resource so it only loads the files once, making the app much faster
@st.cache_resource 
def load_models():
    model = joblib.load('happiness_model.joblib')
    scaler = joblib.load('scaler.joblib')
    return model, scaler

try:
    model, scaler = load_models()
except FileNotFoundError:
    st.error("⚠️ Model or Scaler not found! Please make sure you saved 'happiness_model.joblib' and 'scaler.joblib' in this Colab session.")
    st.stop()

# --- Main Header ---
st.title('🌍 World Happiness Score Predictor')
st.markdown("""
Welcome! This tool uses a Machine Learning model trained on the **World Happiness Report** to predict a country's happiness score based on 6 key indicators. 
*Adjust the sliders in the sidebar to see how different factors affect the final score.*
""")
st.divider()

# --- Sidebar Inputs ---
st.sidebar.header("⚙️ Adjust Indicators")
st.sidebar.write("Slide to set the country's metrics:")

# Added tooltips (help="") to explain what each metric means
gdp        = st.sidebar.slider('GDP per Capita',          0.0, 2.5, 1.0, 0.01, help="Economic production of a country")
social     = st.sidebar.slider('Social Support',          0.0, 2.0, 1.0, 0.01, help="Having someone to count on in times of trouble")
health     = st.sidebar.slider('Healthy Life Expectancy', 0.0, 1.5, 0.8, 0.01, help="Life expectancy at birth")
freedom    = st.sidebar.slider('Freedom',                 0.0, 1.0, 0.5, 0.01, help="Freedom to make life choices")
generosity = st.sidebar.slider('Generosity',              0.0, 1.0, 0.2, 0.01, help="Donations to charity, etc.")
corruption = st.sidebar.slider('Perceptions of Corruption',0.0, 1.0, 0.1, 0.01, help="Perceived lack of corruption in government/business")

st.sidebar.markdown("---")
st.sidebar.caption("By Qazi Anwar Ahmad")

# --- Main Content: Input Summary ---
st.subheader("Current Input Summary")
col1, col2, col3 = st.columns(3)
col1.metric("GDP per Capita", f"{gdp:.2f}")
col2.metric("Social Support", f"{social:.2f}")
col3.metric("Life Expectancy", f"{health:.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Freedom", f"{freedom:.2f}")
col5.metric("Generosity", f"{generosity:.2f}")
col6.metric("Corruption", f"{corruption:.2f}")

st.divider()

# --- Prediction Logic ---
if st.button('🔮 Predict Happiness Score', use_container_width=True):
    # Format inputs for the model
    input_data = np.array([[gdp, social, health, freedom, generosity, corruption]])
    input_scaled = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(input_scaled)[0]
    
    # Display dynamic results based on the score
    st.subheader("Prediction Result")
    if prediction >= 6.5:
        st.success(f"### 🎉 Predicted Happiness Score: {prediction:.2f}")
        st.balloons()
    elif prediction >= 4.5:
        st.info(f"### 😐 Predicted Happiness Score: {prediction:.2f}")
    else:
        st.error(f"### 😔 Predicted Happiness Score: {prediction:.2f}")
        
    st.caption("Note: The official World Happiness Score typically ranges from 2.5 to 8.0.")
