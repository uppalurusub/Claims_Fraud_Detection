from fastapi import APIRouter, HTTPException

from services.fraud_service import FraudService


router = APIRouter(
    prefix="/fraud",
    tags=["Healthcare Claims Fraud Detection"]
)

service = FraudService()


# =====================================================
# DASHBOARD
# =====================================================

@router.get("/dashboard")
def dashboard():

    try:

        return service.dashboard()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# =====================================================
# KPI ENDPOINTS
# =====================================================

@router.get("/kpis")
def kpis():

    try:

        return service.kpis()

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@router.get("/total-claims")
def total_claims():

    return {
        "total_claims":
            service.total_claims()
    }


@router.get("/fraud-claims")
def fraud_claims():

    return {
        "fraud_claims":
            service.fraud_claims()
    }


@router.get("/fraud-rate")
def fraud_rate():

    return {
        "fraud_rate_pct":
            service.fraud_rate()
    }


@router.get("/fraud-amount")
def fraud_amount():

    return {
        "fraud_amount":
            service.fraud_amount()
    }


# =====================================================
# DESCRIPTIVE ANALYTICS
# =====================================================

@router.get("/fraud-by-state")
def fraud_by_state():

    return service.fraud_by_state()


@router.get("/fraud-by-provider")
def fraud_by_provider():

    return service.fraud_by_provider()


@router.get("/fraud-by-procedure")
def fraud_by_procedure():

    return service.fraud_by_procedure()


# =====================================================
# TREND ANALYSIS
# =====================================================

@router.get("/fraud-trend")
def fraud_trend():

    return service.fraud_trend()


# =====================================================
# DIAGNOSTIC ANALYSIS
# =====================================================

@router.get("/root-cause-analysis")
def root_cause_analysis():

    result = service.root_cause_analysis()
    
    return result

    #return service.root_cause_analysis()


# =====================================================
# PREDICTIVE ANALYTICS
# =====================================================

@router.post("/train-model")
def train_model():

    return service.train_model()


@router.get("/model-metrics")
def model_metrics():

    return service.model_metrics()


@router.get("/feature-importance")
def feature_importance():

    return service.feature_importance()


# =====================================================
# ANOMALY DETECTION
# =====================================================

@router.get("/anomaly-detection")
def anomaly_detection():

    return service.anomaly_detection()


# =====================================================
# RISK ANALYSIS
# =====================================================

@router.get("/risk-distribution")
def risk_distribution():

    return service.risk_distribution()


# =====================================================
# VISUALIZATION
# =====================================================

@router.get("/charts")
def charts():

    return service.generate_charts()


# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

@router.get("/executive-summary")
def executive_summary():

    return service.executive_summary()


# =====================================================
# REPORTS
# =====================================================

@router.get("/fraud-report")
def fraud_report():

    result = service.fraud_report()
    print(result)

    return result

    #return service.fraud_report()


@router.get("/model-report")
def model_report():

    return service.model_report()