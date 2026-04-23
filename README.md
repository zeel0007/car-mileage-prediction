# 🚗 Car Mileage Prediction (End-to-End Data Science Project)

Welcome to the **Car Mileage Prediction** project! This project demonstrates a complete end-to-end Data Science workflow — from data analysis to machine learning model deployment using a Django web application.

---

## 📌 Project Overview

This project predicts the fuel efficiency (KMPL) of a car based on various features such as cylinders, horsepower, weight, etc.

It includes:

* Data Analysis (EDA)
* Machine Learning Model (Random Forest)
* Django Web Application for real-time prediction

---

## 🎯 Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning & Feature Engineering
* 🤖 Machine Learning Model (Random Forest Regressor)
* 🌐 Django Web Application
* ⚡ Real-time Mileage Prediction

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-Learn
* Joblib
* Django
* HTML, CSS

---

## 📂 Project Structure

```
car-mileage-prediction/
│
├── data/                 # Dataset (auto-mpg.data)
├── notebooks/            # Jupyter Notebook (EDA + Training)
├── models/               # Trained ML Model (.joblib)
├── webapp/               # Django Web Application
├── train_model.py        # Script to train model
├── requirements.txt
└── README.md
```

---

## ⚙️ How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/zeel0007/car-mileage-prediction.git
cd car-mileage-prediction
```

---

### 2️⃣ Create Virtual Environment

**macOS / Linux:**

```
python3 -m venv venv
source venv/bin/activate
```

**Windows:**

```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```
pip install django pandas numpy scikit-learn joblib matplotlib seaborn
```

---

### 4️⃣ Train Model (if not already present)

```
python train_model.py
```

---

### 5️⃣ Run Django Server

```
cd webapp
python manage.py migrate
python manage.py runserver
```

---

### 6️⃣ Open in Browser

```
http://127.0.0.1:8000/
```

---

## 📈 Model Details

* Algorithm: Random Forest Regressor
* Target: KMPL (Kilometers Per Liter)
* Input Features:

  * Cylinders
  * Displacement
  * Horsepower
  * Weight
  * Acceleration
  * Model Year
  * Origin

---

## 📸 Output Screenshots

(Add your screenshots here)

---

## 🚀 Future Improvements

* Deploy on cloud (Render / Railway)
* Improve model accuracy
* Add authentication system
* Enhance UI

---

## 👨‍💻 Author

Zeel

MCA Student | Data Science & Web Development Enthusiast

🔗 GitHub: https://github.com/zeel0007

---


