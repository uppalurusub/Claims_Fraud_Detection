# 🚨 Healthcare Claims Fraud Detection System

## 📌 Project Overview

The **Healthcare Claims Fraud Detection System** is an end-to-end Machine Learning and Analytics application that identifies potentially fraudulent healthcare insurance claims using predictive analytics, descriptive analytics, anomaly detection, and interactive dashboards.

The solution combines **FastAPI**, **Streamlit**, **Scikit-Learn**, **Plotly**, and **Python** to provide healthcare organizations with actionable fraud insights through REST APIs and a modern web dashboard.

---

# Business Problem

Healthcare insurance fraud costs billions of dollars annually. Manual claim investigation is expensive, slow, and unable to detect complex fraud patterns.

This project helps organizations:

- Detect fraudulent claims
- Prioritize high-risk claims
- Identify suspicious providers
- Analyze fraud trends
- Reduce financial losses
- Improve operational efficiency

---

# Objectives

- Detect fraudulent healthcare claims
- Build predictive fraud detection models
- Perform fraud analytics
- Visualize fraud patterns
- Provide REST APIs
- Build an interactive Streamlit dashboard
- Generate executive-level KPIs

---

# Solution Architecture

```
                Healthcare Claims Dataset
                         │
                         ▼
              Data Preprocessing Pipeline
                         │
                         ▼
             Feature Engineering Pipeline
                         │
                         ▼
             Fraud Detection ML Model
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
   FastAPI REST APIs               Streamlit Dashboard
         ▼                               ▼
  Business Analytics              Executive Reporting
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.x |
| Backend | FastAPI |
| Frontend | Streamlit |
| ML | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Plotly, Matplotlib |
| Model Storage | Pickle |
| API Testing | Swagger UI |
| Deployment | Uvicorn |

---

# Project Structure

```
Claims_Fraud_Detection
│
├── data/
│   └── claims.csv
│
├── models/
│   └── fraud_detector.pkl
│
├── reports/
│   └── charts/
│
├── src/
│   ├── app/
│   │
│   ├── config/
│   │     settings.py
│   │
│   ├── routers/
│   │     fraud_router.py
│   │
│   ├── services/
│   │     fraud_service.py
│   │
│   ├── implementations/
│   │     fraud_impl.py
│   │
│   ├── models/
│   │     fraud_model.py
│   │
│   ├── utils/
│   │     preprocessing.py
│   │     feature_engineering.py
│   │     visualizations.py
│   │
│   └── main.py
│
├── ui/
│     streamlit_app.py
│
├── requirements.txt
│
└── README.md
```

---

# Features

## Executive Dashboard

- Total Claims
- Fraud Claims
- Fraud Rate
- Fraud Amount
- Average Claim Amount
- High Risk Claims

---

## Descriptive Analytics

- Fraud by State
- Fraud by Provider
- Fraud by Procedure
- Fraud Distribution
- Fraud Risk Distribution

---

## Trend Analysis

- Monthly Fraud Trend
- Fraud Growth Analysis
- Historical Fraud Monitoring

---

## Diagnostic Analytics

- Root Cause Analysis
- Provider Analysis
- Procedure Analysis
- Geographic Analysis

---

## Predictive Analytics

- Fraud Prediction
- Fraud Probability
- Feature Importance
- Model Evaluation

---

## Anomaly Detection

Detect unusual claims using statistical and machine learning techniques.

---

# Machine Learning Pipeline

```
Claims Data
      │
      ▼
Missing Value Handling
      │
      ▼
Categorical Encoding
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
Fraud Detection Model
      │
      ▼
Prediction
```

---

# API Endpoints

## Dashboard

| Endpoint | Description |
|-----------|-------------|
| GET /fraud/dashboard | Complete dashboard |

---

## KPIs

| Endpoint | Description |
|-----------|-------------|
| GET /fraud/kpis | Executive KPIs |
| GET /fraud/total-claims | Total Claims |
| GET /fraud/fraud-claims | Fraud Claims |
| GET /fraud/fraud-rate | Fraud Rate |
| GET /fraud/fraud-amount | Fraud Amount |

---

## Analytics

| Endpoint | Description |
|-----------|-------------|
| GET /fraud/fraud-by-state | State Analytics |
| GET /fraud/fraud-by-provider | Provider Analytics |
| GET /fraud/fraud-by-procedure | Procedure Analytics |
| GET /fraud/fraud-trend | Fraud Trend |

---

## Diagnostic Analysis

| Endpoint | Description |
|-----------|-------------|
| GET /fraud/root-cause-analysis | Root Cause Analysis |

---

## Machine Learning

| Endpoint | Description |
|-----------|-------------|
| POST /fraud/train-model | Train Fraud Model |
| GET /fraud/model-metrics | Model Performance |
| GET /fraud/feature-importance | Feature Importance |

---

## Anomaly Detection

| Endpoint | Description |
|-----------|-------------|
| GET /fraud/anomaly-detection | Detect Anomalies |

---

# Dashboard

The Streamlit dashboard provides:

- Executive KPIs
- Fraud Visualizations
- Provider Analytics
- Procedure Analytics
- Geographic Analytics
- Trend Charts
- Predictive Insights

---

# Generated Reports

The application automatically generates charts including:

- Fraud Distribution
- Fraud by State
- Fraud by Provider
- Fraud by Procedure
- Age Group Fraud
- Monthly Fraud Trend
- Correlation Heatmap
- Fraud Risk Distribution
- Claim Amount Distribution
- Claim Amount vs Fraud

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Claims_Fraud_Detection.git

cd Claims_Fraud_Detection
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
cd src/app

uvicorn main:app --reload
```

API:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

---

## Run Streamlit

```bash
cd src/ui

streamlit run streamlit_app.py
```

Dashboard:

```
http://localhost:8501
```

---

# Expected Workflow

```
Claims Dataset
      │
      ▼
Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Fraud Model
      │
      ▼
REST APIs
      │
      ▼
Streamlit Dashboard
      │
      ▼
Business Decision Making
```

---

# Current Project Components

- FastAPI Backend
- Streamlit Dashboard
- Fraud Detection Model
- Feature Engineering
- Data Preprocessing
- Fraud Analytics
- Executive Dashboard
- Visualization Reports
- Model Persistence

---

# Future Enhancements

- MLflow Experiment Tracking
- Model Registry
- SHAP Explainable AI
- LIME Interpretability
- XGBoost and LightGBM Models
- Hyperparameter Optimization
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- Authentication & Authorization
- Role-Based Access Control
- PostgreSQL Integration
- Real-time Fraud Monitoring
- Kafka Streaming
- Cloud Deployment (Azure/AWS/GCP)

---

# Business Value

This solution enables healthcare organizations to:

- Detect fraud earlier
- Reduce investigation costs
- Improve claim processing efficiency
- Identify suspicious providers
- Reduce financial losses
- Improve compliance
- Support executive decision-making with analytics

---

# Author

**Healthcare Claims Fraud Detection System**

Developed using:

- Python
- FastAPI
- Streamlit
- Scikit-Learn
- Plotly
- Pandas
- Machine Learning
- Healthcare Analytics

---