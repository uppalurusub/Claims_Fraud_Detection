from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.fraud_router import router as fraud_router


app = FastAPI(

    title="Healthcare Claims Fraud Detection API",

    description="""
    Healthcare Claims Fraud Detection System

    Features:
    - KPI Analytics
    - Fraud Detection
    - Fraud Risk Scoring
    - Diagnostic Analytics
    - Predictive Analytics
    - Anomaly Detection
    - Executive Reporting
    - Dashboard APIs
    """,

    version="1.0.0",

    docs_url="/docs",

    redoc_url="/redoc"
)


# ==================================================
# CORS
# ==================================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ==================================================
# ROOT
# ==================================================

@app.get("/")
def home():

    return {

        "application":
            "Healthcare Claims Fraud Detection",

        "version":
            "1.0.0",

        "status":
            "Running"
    }


# ==================================================
# HEALTH CHECK
# ==================================================

@app.get("/health")
def health():

    return {

        "status":
            "healthy"
    }





# ==================================================
# ROUTERS
# ==================================================

app.include_router(
    fraud_router
)