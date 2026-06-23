
# 🚗 Car Resale Value Predictor

An interactive **Streamlit web app** that predicts car resale values using a **Linear Regression model** trained with scikit‑learn.  
This portfolio project demonstrates end‑to‑end ML deployment: data preprocessing, feature engineering, model training, saving with pickle, and serving predictions through a clean UI.

---

## ✨ Features
- Predict resale value based on:
  - Year of manufacture
  - Mileage
  - Number of owners
  - Transmission type (manual / automatic / unknown)
  - Car model (Honda / Toyota / BMW)
  - Fuel type (Petrol / Gas / Electric / Unknown)
- Uses **StandardScaler** for consistent predictions
- Interactive UI built with **Streamlit**
- Ready for deployment on **Streamlit Cloud**

---

## 📂 Project Structure
dirty_cars_linear_regression_model/
├── app.py                # Streamlit app
├── linear_model.pkl      # Saved model + scaler
├── requirements.txt      # Dependencies
├── README.md             # Project description
└── .gitignore            # Ignore unnecessary files


