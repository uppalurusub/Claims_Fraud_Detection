from implementations.fraud_impl import FraudImplementation


class FraudService:

    def __init__(self):

        self.impl = FraudImplementation()

    # ==================================================
    # DASHBOARD
    # ==================================================

    def dashboard(self):

        return self.impl.dashboard()

    # ==================================================
    # KPI METHODS
    # ==================================================

    def kpis(self):

        return self.impl.kpis()

    def total_claims(self):

        return self.impl.total_claims()

    def fraud_claims(self):

        return self.impl.fraud_claims()

    def fraud_rate(self):

        return self.impl.fraud_rate()

    def fraud_amount(self):

        return self.impl.fraud_amount()

    def average_claim_amount(self):

        return self.impl.average_claim_amount()

    def average_fraud_amount(self):

        return self.impl.average_fraud_amount()

    def high_risk_claims(self):

        return self.impl.high_risk_claims()

    # ==================================================
    # DESCRIPTIVE ANALYTICS
    # ==================================================

    def fraud_by_state(self):

        return self.impl.fraud_by_state()

    def fraud_by_provider(self):

        return self.impl.fraud_by_provider()

    def fraud_by_procedure(self):

        return self.impl.fraud_by_procedure()

    # ==================================================
    # TREND ANALYSIS
    # ==================================================

    def fraud_trend(self):

        return self.impl.fraud_trend()

    # ==================================================
    # DIAGNOSTIC ANALYSIS
    # ==================================================

    def root_cause_analysis(self):

        result = self.impl.root_cause_analysis()
        

        return result
        #return self.impl.root_cause_analysis()

    # ==================================================
    # PREDICTIVE ANALYTICS
    # ==================================================

    def train_model(self):

        return self.impl.train_model()

    def model_metrics(self):

        return self.impl.model_metrics()

    def feature_importance(self):

        return self.impl.feature_importance()

    # ==================================================
    # ANOMALY DETECTION
    # ==================================================

    def anomaly_detection(self):

        return self.impl.anomaly_detection()

    # ==================================================
    # RISK ANALYSIS
    # ==================================================

    def risk_distribution(self):

        return self.impl.risk_distribution()

    # ==================================================
    # VISUALIZATION
    # ==================================================

    def generate_charts(self):

        return self.impl.generate_charts()

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    def executive_summary(self):

        return self.impl.executive_summary()

    # ==================================================
    # COMPLETE REPORT
    # ==================================================

    def fraud_report(self):

        return {

            "kpis":
                self.impl.kpis(),

            "fraud_by_state":
                self.impl.fraud_by_state(),

            "fraud_by_provider":
                self.impl.fraud_by_provider(),

            "fraud_by_procedure":
                self.impl.fraud_by_procedure(),

            "fraud_trend":
                self.impl.fraud_trend(),

            "root_cause_analysis":
                self.impl.root_cause_analysis(),

            "risk_distribution":
                self.impl.risk_distribution(),

            "executive_summary":
                self.impl.executive_summary()
        }

    # ==================================================
    # MODEL REPORT
    # ==================================================

    def model_report(self):

        return {

            "metrics":
                self.impl.model_metrics(),

            "feature_importance":
                self.impl.feature_importance(),

            "anomaly_detection":
                self.impl.anomaly_detection()
        }