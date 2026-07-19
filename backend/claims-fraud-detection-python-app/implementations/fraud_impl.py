import pandas as pd

from utils.preprocessing import ClaimsPreprocessor
from utils.feature_engineering import ClaimsFeatureEngineering
from utils.visualizations import FraudVisualization

from models.fraud_model import FraudDetectionModel


class FraudImplementation:

    def __init__(self):

        self.filepath = "../data/claims.csv"

        self.df = self._load_processed_data()

    # ==================================================
    # Data Pipeline
    # ==================================================

    def _load_processed_data(self):

        processor = ClaimsPreprocessor(
            self.filepath
        )

        df = processor.process()

        feature_engineering = (
            ClaimsFeatureEngineering(df)
        )

        df = feature_engineering.build_features()

        return df

    # ==================================================
    # KPI METHODS
    # ==================================================

    def total_claims(self):

        return len(self.df)

    def fraud_claims(self):

        return (
            int(self.df["is_fraud"].sum())
        )

    def fraud_rate(self):

        total = len(self.df)

        fraud = self.df["is_fraud"].sum()

        return float(round(
            fraud / total * 100,
            2
        ))

    def fraud_amount(self):

        amount = self.df[
            self.df["is_fraud"] == 1
        ]["claim_amount"].sum()

        return round(float(amount), 2)

    def average_claim_amount(self):

        return round(
            float(
                self.df["claim_amount"].mean()
            ),
            2
        )

    def average_fraud_amount(self):

        fraud_df = self.df[
            self.df["is_fraud"] == 1
        ]

        return round(
            float(
                fraud_df["claim_amount"].mean()
            ),
            2
        )

    def high_risk_claims(self):

        if "fraud_risk_score" not in self.df.columns:
            return 0

        return int(
            (
                self.df["fraud_risk_score"] >= 70
            ).sum()
        )

    # ==================================================
    # DASHBOARD KPIs
    # ==================================================

    def kpis(self):

        

        return {

            "total_claims":
                int(self.total_claims()),

            "fraud_claims":
                int(self.fraud_claims()),

            "fraud_rate_pct":
                float(self.fraud_rate()),

            "fraud_amount":
                float(self.fraud_amount()),

            "avg_claim_amount":
                float(self.average_claim_amount()),

            "avg_fraud_amount":
                float(self.average_fraud_amount()),

            "high_risk_claims":
                int(self.high_risk_claims())
        }

    # ==================================================
    # DESCRIPTIVE ANALYTICS
    # ==================================================

    def fraud_by_state(self):

        result = (

            self.df.groupby("state")
            ["is_fraud"]

            .agg([
                "count",
                "sum",
                "mean"
            ])

            .reset_index()

        )

        result.columns = [

            "state",
            "total_claims",
            "fraud_claims",
            "fraud_rate"

        ]

        return result.to_dict(
            orient="records"
        )

    def fraud_by_provider(self):

        result = (

            self.df.groupby("provider_id")
            ["is_fraud"]

            .agg([
                "count",
                "sum",
                "mean"
            ])

            .reset_index()

        )

        result.columns = [

            "provider_id",
            "total_claims",
            "fraud_claims",
            "fraud_rate"

        ]

        result = result.sort_values(
            by="fraud_claims",
            ascending=False
        )

        return result.head(
            20
        ).to_dict(
            orient="records"
        )

    def fraud_by_procedure(self):

        result = (

            self.df.groupby(
                "procedure_code"
            )

            ["is_fraud"]

            .sum()

            .reset_index()

            .sort_values(
                by="is_fraud",
                ascending=False
            )

        )

        return result.head(
            20
        ).to_dict(
            orient="records"
        )

    # ==================================================
    # TREND ANALYSIS
    # ==================================================

    def fraud_trend(self):

        df = self.df.copy()

        if "claim_date" not in df.columns:
            return []

        df["claim_date"] = pd.to_datetime(
            df["claim_date"]
        )

        result = (

            df.groupby(
                pd.Grouper(
                    key="claim_date",
                    freq="ME"
                )
            )

            ["is_fraud"]

            .sum()

            .reset_index()

        )

        return result.to_dict(
            orient="records"
        )

    # ==================================================
    # DIAGNOSTIC ANALYSIS
    # ==================================================

    def root_cause_analysis(self):

        top_provider = (

            self.df.groupby(
                "provider_id"
            )

            ["is_fraud"]

            .sum()

            .idxmax()

        )

        top_procedure = (

            self.df.groupby(
                "procedure_code"
            )

            ["is_fraud"]

            .sum()

            .idxmax()

        )

        

        return {

            "highest_fraud_provider":
                int(top_provider),

            "highest_fraud_procedure":
                int(top_procedure),

            "recommendation":
                "Audit provider and procedure immediately"

        }

    # ==================================================
    # PREDICTIVE ANALYTICS
    # ==================================================

    def train_model(self):

        model = FraudDetectionModel(
            self.df
        )

        results = (
            model.train_best_model()
        )

        model.save_model(
            "../models/fraud_detector.pkl"
        )

        return results

    # ==================================================
    # MODEL PERFORMANCE
    # ==================================================

    def model_metrics(self):

        model = FraudDetectionModel(
            self.df
        )

        results = (
            model.train_best_model()
        )

        return results["metrics"]

    # ==================================================
    # FEATURE IMPORTANCE
    # ==================================================

    def feature_importance(self):

        model = FraudDetectionModel(
            self.df
        )

        results = (
            model.train_best_model()
        )

        return results[
            "feature_importance"
        ]

    # ==================================================
    # ANOMALY DETECTION
    # ==================================================

    def anomaly_detection(self):

        model = FraudDetectionModel(
            self.df
        )

        model.prepare_data()

        return model.anomaly_detection()

    # ==================================================
    # FRAUD RISK DISTRIBUTION
    # ==================================================

    def risk_distribution(self):

        if (
            "risk_category"
            not in self.df.columns
        ):
            return []

        result = (

            self.df.groupby(
                "risk_category"
            )

            .size()

            .reset_index(
                name="count"
            )

        )

        return result.to_dict(
            orient="records"
        )

    # ==================================================
    # VISUALIZATION FILES
    # ==================================================

    def generate_charts(self):

        viz = FraudVisualization(
            self.df
        )

        return (
            viz.generate_dashboard_charts()
        )

    # ==================================================
    # EXECUTIVE SUMMARY
    # ==================================================

    def executive_summary(self):

        

        return {

            "total_claims":
                int(self.total_claims()),

            "fraud_claims":
                int(self.fraud_claims()),

            "fraud_rate":
                float(self.fraud_rate()),

            "fraud_amount":
                float(self.fraud_amount()),

            "high_risk_claims":
                int(self.high_risk_claims()),

            "key_finding":
                "Fraud concentrated among a small group of providers.",

            "business_action":
                "Prioritize provider audits and deploy predictive fraud scoring."

        }

    # ==================================================
    # COMPLETE DASHBOARD
    # ==================================================

    def dashboard(self):

        return {

            "kpis":
                self.kpis(),

            "fraud_by_state":
                self.fraud_by_state(),

            "fraud_by_provider":
                self.fraud_by_provider(),

            "fraud_by_procedure":
                self.fraud_by_procedure(),

            "risk_distribution":
                self.risk_distribution(),

            "executive_summary":
                self.executive_summary()
        }