import pandas as pd
import numpy as np


class ClaimsFeatureEngineering:

    def __init__(self, df):

        self.df = df.copy()

    # --------------------------------------------------
    # Claim Amount Features
    # --------------------------------------------------

    def claim_amount_features(self):

        self.df["claim_amount_log"] = np.log1p(
            self.df["claim_amount"]
        )

        self.df["high_value_claim"] = np.where(
            self.df["claim_amount"] > 25000,
            1,
            0
        )

        self.df["very_high_value_claim"] = np.where(
            self.df["claim_amount"] > 50000,
            1,
            0
        )

        return self

    # --------------------------------------------------
    # Age Features
    # --------------------------------------------------

    def age_features(self):

        self.df["senior_citizen"] = np.where(
            self.df["age"] >= 65,
            1,
            0
        )

        self.df["child_patient"] = np.where(
            self.df["age"] < 18,
            1,
            0
        )

        self.df["age_group"] = pd.cut(
            self.df["age"],
            bins=[0,18,35,50,65,120],
            labels=[
                "0-18",
                "19-35",
                "36-50",
                "51-65",
                "66+"
            ]
        )

        self.df["age_group"] = (
            self.df["age_group"]
            .cat.codes
        )

        return self

    # --------------------------------------------------
    # Hospitalization Features
    # --------------------------------------------------

    def hospitalization_features(self):

        self.df["long_stay_flag"] = np.where(
            self.df["days_hospitalized"] > 10,
            1,
            0
        )

        self.df["extreme_stay_flag"] = np.where(
            self.df["days_hospitalized"] > 20,
            1,
            0
        )

        return self

    # --------------------------------------------------
    # Procedure Features
    # --------------------------------------------------

    def procedure_features(self):

        self.df["multiple_procedures_flag"] = np.where(
            self.df["num_procedures"] >= 5,
            1,
            0
        )

        self.df["procedure_per_day"] = (
            self.df["num_procedures"] /
            (self.df["days_hospitalized"] + 1)
        )

        return self

    # --------------------------------------------------
    # Prior Claims Features
    # --------------------------------------------------

    def prior_claim_features(self):

        self.df["frequent_claimant"] = np.where(
            self.df["prior_claims"] > 15,
            1,
            0
        )

        self.df["super_frequent_claimant"] = np.where(
            self.df["prior_claims"] > 30,
            1,
            0
        )

        return self

    # --------------------------------------------------
    # Provider Features
    # --------------------------------------------------

    def provider_features(self):

        provider_count = (
            self.df.groupby("provider_id")
            .size()
            .reset_index(
                name="provider_claim_count"
            )
        )

        self.df = self.df.merge(
            provider_count,
            on="provider_id",
            how="left"
        )

        provider_avg_claim = (
            self.df.groupby("provider_id")
            ["claim_amount"]
            .mean()
            .reset_index(
                name="provider_avg_claim"
            )
        )

        self.df = self.df.merge(
            provider_avg_claim,
            on="provider_id",
            how="left"
        )

        return self

    # --------------------------------------------------
    # Patient Features
    # --------------------------------------------------

    def patient_features(self):

        patient_claim_count = (
            self.df.groupby("patient_id")
            .size()
            .reset_index(
                name="patient_claim_count"
            )
        )

        self.df = self.df.merge(
            patient_claim_count,
            on="patient_id",
            how="left"
        )

        return self

    # --------------------------------------------------
    # State Features
    # --------------------------------------------------

    def state_features(self):

        state_avg_claim = (
            self.df.groupby("state")
            ["claim_amount"]
            .mean()
            .reset_index(
                name="state_avg_claim"
            )
        )

        self.df = self.df.merge(
            state_avg_claim,
            on="state",
            how="left"
        )

        return self

    # --------------------------------------------------
    # Time Features
    # --------------------------------------------------

    def time_features(self):

        self.df["claim_date"] = pd.to_datetime(
            self.df["claim_date"]
        )

        self.df["claim_year"] = (
            self.df["claim_date"].dt.year
        )

        self.df["claim_month"] = (
            self.df["claim_date"].dt.month
        )

        self.df["claim_quarter"] = (
            self.df["claim_date"].dt.quarter
        )

        self.df["claim_week"] = (
            self.df["claim_date"].dt.isocalendar().week
        )

        self.df["month_end_claim"] = np.where(
            self.df["claim_date"].dt.day >= 25,
            1,
            0
        )

        return self

    # --------------------------------------------------
    # Fraud Risk Score
    # --------------------------------------------------

    def fraud_risk_score(self):

        score = (
            self.df["high_value_claim"] * 30
            + self.df["multiple_procedures_flag"] * 20
            + self.df["frequent_claimant"] * 25
            + self.df["long_stay_flag"] * 15
        )

        self.df["fraud_risk_score"] = score

        self.df["risk_category"] = pd.cut(
            score,
            bins=[-1,30,60,100],
            labels=[
                "Low",
                "Medium",
                "High"
            ]
        )

        return self

    # --------------------------------------------------
    # Ratio Features
    # --------------------------------------------------

    def ratio_features(self):

        self.df["claim_per_procedure"] = (
            self.df["claim_amount"] /
            (self.df["num_procedures"] + 1)
        )

        self.df["claim_per_day"] = (
            self.df["claim_amount"] /
            (self.df["days_hospitalized"] + 1)
        )

        return self

    # --------------------------------------------------
    # Interaction Features
    # --------------------------------------------------

    def interaction_features(self):

        self.df["amount_x_prior_claims"] = (
            self.df["claim_amount"] *
            self.df["prior_claims"]
        )

        self.df["amount_x_procedures"] = (
            self.df["claim_amount"] *
            self.df["num_procedures"]
        )

        return self

    # --------------------------------------------------
    # Complete Feature Engineering
    # --------------------------------------------------

    def build_features(self):

        return (
            self.claim_amount_features()
            .age_features()
            .hospitalization_features()
            .procedure_features()
            .prior_claim_features()
            .provider_features()
            .patient_features()
            .state_features()
            .time_features()
            .fraud_risk_score()
            .ratio_features()
            .interaction_features()
            .df
        )