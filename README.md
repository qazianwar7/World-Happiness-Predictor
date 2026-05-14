# 🌍 World Happiness Score Predictor

## 📌 Overview
This project is an end-to-end Data Science workflow that analyzes the World Happiness Report (2015-2019) and uses a Machine Learning model to predict a country's happiness score based on its socio-economic indicators. It concludes with an interactive web application built using Streamlit.

## 🛠️ Features
* **Exploratory Data Analysis (EDA):** Cleaned and merged multiple datasets, handling missing values and duplicates.
* **Data Visualization:** Identified correlations between GDP, social support, and happiness using scatter plots, histograms, and heatmaps.
* **Predictive Modeling:** Built and evaluated a Multiple Linear Regression model.
* **Interactive Dashboard:** Deployed a user-friendly Streamlit web app where users can adjust specific country metrics to see the predicted happiness score in real-time.

## 💻 Tech Stack
* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression, StandardScaler)
* **Deployment:** Streamlit, pyngrok, joblib

## 📊 Model Performance
The predictive model was evaluated using the following metrics:
* **R² Score:** 0.75+ (indicating a strong fit)
* **Root Mean Squared Error (RMSE):** ~0.55

## 🚀 How to Run the App (Via Google Colab)
Because the app uses Streamlit and Ngrok for tunneling, it is designed to run directly from a Google Colab environment.
1. Open the `.ipynb` notebook in Google Colab.
2. Run all cells sequentially to train the model and save the `.joblib` files.
3. In the final cell, replace `'YOUR_NGROK_TOKEN_HERE'` with your free personal Auth Token from [ngrok.com](https://ngrok.com/).
4. Run the cell and click the generated public URL to access the web dashboard.

## 💡 Key Insights
* **Wealth Matters, But Isn't Everything:** GDP per capita shows the highest correlation with happiness, but Social Support follows very closely.
* **Health and Freedom:** Healthy life expectancy is a massive driver for top-tier happy countries compared to bottom-tier countries.
