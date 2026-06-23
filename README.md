# 🚗 Car Resale Value Predictor

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikit-learn)
![License: MIT](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo
Try the app here: [Car Resale Value Predictor](https://dirtycarslinearregressionmodel-pwddhmzbjug2udqqswarib.streamlit.app/)

---

## 📖 Project Overview
This project predicts the **resale value of cars** based on features such as:
- Year of manufacture  
- Mileage  
- Number of owners  
- Transmission type  
- Car model  
- Fuel type  

It uses **Linear Regression** with preprocessing via `StandardScaler` to generate accurate predictions.  
The app is built with **Streamlit** for interactive deployment.

---

## 🗂️ Repository Structure
```txt
.
├── app.py                # Streamlit app entry point
├── linear_model.pkl      # Saved model (and scaler if included)
├── requirements.txt      # Dependencies for deployment
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore            # Ignore unnecessary files
└── .devcontainer/        # Dev container setup (optional)


