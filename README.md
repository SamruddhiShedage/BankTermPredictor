# 📊 Bank Marketing Subscription Predictor

This is a **Streamlit web app** that predicts whether a customer will subscribe to a term deposit, based on features from the UCI Bank Marketing dataset. It uses a pre-trained **XGBoost model**.

---

## 🚀 Features

- 📋 Sidebar form to input customer details
- ⚡ Real-time prediction with confidence score
- 📈 Based on UCI’s real-world dataset
- 🧠 Uses XGBoost for accurate classification
- 🖥️ Deployable with Streamlit Cloud

---

## 🗂️ Project Structure

```
.
├── app.py                       # Streamlit web app
├── xgboost_bank_model.pkl       # Trained ML model
├── requirements.txt             # Python dependencies
│── bank-additional-full.csv     # Original dataset
└── README.md
```

---

## 🔧 Installation & Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/bank-marketing-streamlit.git
cd bank-marketing-streamlit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📚 Dataset Information

- Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/bank+marketing)
- Size: 41,188 records
- Goal: Predict if a client will subscribe to a term deposit

---
