# 🚨 Healthcare Claims Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![React](https://img.shields.io/badge/React-19-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue)
![Vite](https://img.shields.io/badge/Vite-Latest-purple)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

Healthcare Claims Fraud Detection System is an end-to-end AI-powered analytics platform that detects potentially fraudulent healthcare insurance claims using Machine Learning and interactive dashboards.

The application combines:

- Machine Learning Fraud Detection
- FastAPI REST APIs
- React TypeScript Dashboard
- Executive Analytics
- Fraud Risk Analysis
- Interactive Charts
- KPI Monitoring

The solution is designed for healthcare insurance providers, hospitals, fraud investigators, and healthcare analytics teams.

---

# ✨ Features

## Backend

- FastAPI REST APIs
- Fraud Prediction
- Executive Summary APIs
- KPI Generation
- Fraud Analytics
- Data Preprocessing
- Feature Engineering
- ML Model Inference
- Interactive Reports
- Visualization Generation

---

## Frontend

- Modern React UI
- Responsive Dashboard
- Executive Summary
- KPI Cards
- Fraud Charts
- Fraud Distribution
- Risk Analysis
- Anomaly Detection
- Interactive Graphs
- Real-time API Integration

---

# 🏗 Project Architecture

```
                   +-----------------------+
                   |   React Dashboard     |
                   | React + TypeScript    |
                   +-----------+-----------+
                               |
                          Axios REST API
                               |
                    +----------v----------+
                    |      FastAPI        |
                    |   Fraud APIs        |
                    +----------+----------+
                               |
                     ML Prediction Engine
                               |
                  Fraud Detection Model (.pkl)
                               |
                      Claims Dataset (CSV)
```

---

# 📂 Project Structure

```
Claims_Fraud_Detection/

│
├── backend/
│   │
│   ├── claims-fraud-detection-python-app/
│   │   ├── config/
│   │   ├── implementations/
│   │   ├── models/
│   │   ├── routers/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── data/
│   │     claims.csv
│   │
│   ├── models/
│   │     fraud_detector.pkl
│   │
│   └── reports/
│         charts/
│
├── ui/
│   └── reactjs/
│       └── claims-fraud-detection-react-app/
│            ├── src/
│            │    ├── api/
│            │    ├── components/
│            │    ├── hooks/
│            │    ├── pages/
│            │    ├── styles/
│            │    ├── types/
│            │    ├── utils/
│            │    ├── App.tsx
│            │    └── main.tsx
│            │
│            ├── public/
│            └── package.json
│
└── requirements.txt
```

---

# 🛠 Technology Stack

## Backend

- Python
- FastAPI
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Matplotlib
- Plotly

---

## Frontend

- React 19
- TypeScript
- Vite
- Axios
- Chart.js
- React ChartJS
- Recharts
- Lucide React

---

# Machine Learning Pipeline

```
Claims Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Preprocessing
      │
      ▼
Fraud Detection Model
      │
      ▼
Prediction
      │
      ▼
Analytics Dashboard
```

---

# Backend Modules

```
config/
    Application configuration

routers/
    REST API endpoints

services/
    Business logic

implementations/
    Fraud detection implementation

models/
    Request/Response models

utils/
    Data loading
    Preprocessing
    Feature engineering
    Visualizations
```

---

# Frontend Modules

```
api/
    Axios API layer

components/
    Dashboard components
    KPI cards
    Charts
    Executive summary

hooks/
    API hooks

pages/
    Dashboard page

utils/
    Formatting
    Chart adapters

types/
    TypeScript interfaces
```

---

# REST API Flow

```
React Dashboard
        │
        ▼
Axios
        │
        ▼
FastAPI Router
        │
        ▼
Service Layer
        │
        ▼
Implementation
        │
        ▼
ML Model
        │
        ▼
Prediction Response
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/claims-fraud-detection.git

cd claims-fraud-detection
```

---

# Backend Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run FastAPI

```bash
cd backend/claims-fraud-detection-python-app

uvicorn main:app --reload
```

Backend URL

```
http://localhost:8000
```

Swagger

```
http://localhost:8000/docs
```

---

# Frontend Setup

Navigate to frontend

```bash
cd ui/reactjs/claims-fraud-detection-react-app
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Application

```
http://localhost:5173
```

---

# Available Scripts

```
npm run dev

npm run build

npm run preview

npm run lint
```

---

# Dashboard Features

✔ Executive Summary

✔ Fraud KPIs

✔ Fraud Risk Distribution

✔ Fraud by State

✔ Fraud by Procedure

✔ Claim Amount Analysis

✔ Monthly Fraud Trends

✔ Correlation Analysis

✔ Top Fraud Providers

✔ Age Group Analysis

---

# Reports Generated

```
Fraud Distribution

Fraud Risk Distribution

Claim Amount Distribution

Monthly Fraud Trend

Fraud by State

Fraud by Procedure

Age Group Fraud

Top Fraud Providers

Correlation Heatmap
```

---

# Sample Workflow

```
Claims Data
      │
      ▼
FastAPI
      │
      ▼
Fraud Prediction
      │
      ▼
Analytics
      │
      ▼
React Dashboard
```

---

# Future Enhancements

- JWT Authentication
- Role-Based Access Control
- PostgreSQL Support
- Docker Deployment
- Kubernetes Deployment
- CI/CD Pipeline
- MLflow Integration
- SHAP Explainability
- Model Monitoring
- Real-time Fraud Alerts
- Cloud Deployment (Azure / AWS / GCP)

---

# Best Practices

- Modular Architecture
- Layered Backend
- TypeScript Interfaces
- Separation of Concerns
- RESTful APIs
- Reusable Components
- Environment-based Configuration
- Scalable Folder Structure

---

# Contributors

Developed as a Healthcare AI & Machine Learning project demonstrating:

- FastAPI Development
- React TypeScript Development
- Machine Learning Deployment
- Fraud Detection Analytics
- Healthcare Dashboard Visualization

---

# License

This project is intended for educational and research purposes.

MIT License

---

# Screenshots

- Executive Dashboard
- Fraud KPIs
- Fraud Analytics
- Fraud Distribution
- Fraud Trends
- Fraud Risk Analysis
- Interactive Charts

(Add screenshots here after deployment.)

---

# Contact

For questions, enhancements, or contributions, please create an issue or submit a pull request.

⭐ If you find this project useful, please consider giving it a star on GitHub!