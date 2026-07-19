import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    roc_curve,
    auc,
    precision_recall_curve,
    confusion_matrix
)


class FraudVisualization:

    def __init__(self, df):

        self.df = df.copy()

        os.makedirs(
            "reports/charts",
            exist_ok=True
        )

        sns.set_style("whitegrid")

    # --------------------------------------------------
    # Save Chart
    # --------------------------------------------------

    def save_chart(
        self,
        filename
    ):

        filepath = (
            f"reports/charts/{filename}"
        )

        plt.tight_layout()

        plt.savefig(
            filepath,
            bbox_inches="tight"
        )

        plt.close()

        return filepath

    # --------------------------------------------------
    # Fraud Distribution
    # --------------------------------------------------

    def fraud_distribution(self):

        plt.figure(figsize=(8,5))

        sns.countplot(
            x="is_fraud",
            data=self.df
        )

        plt.title(
            "Fraud vs Non-Fraud Claims"
        )

        return self.save_chart(
            "fraud_distribution.png"
        )

    # --------------------------------------------------
    # Claim Amount Distribution
    # --------------------------------------------------

    def claim_amount_distribution(self):

        plt.figure(figsize=(10,5))

        sns.histplot(
            self.df["claim_amount"],
            kde=True,
            bins=30
        )

        plt.title(
            "Claim Amount Distribution"
        )

        return self.save_chart(
            "claim_amount_distribution.png"
        )

    # --------------------------------------------------
    # Fraud by State
    # --------------------------------------------------

    def fraud_by_state(self):

        fraud_state = (
            self.df.groupby("state")
            ["is_fraud"]
            .mean()
            .reset_index()
        )

        plt.figure(figsize=(10,5))

        sns.barplot(
            data=fraud_state,
            x="state",
            y="is_fraud"
        )

        plt.title(
            "Fraud Rate by State"
        )

        return self.save_chart(
            "fraud_by_state.png"
        )

    # --------------------------------------------------
    # Top Fraudulent Providers
    # --------------------------------------------------

    def top_fraud_providers(self):

        providers = (
            self.df[self.df["is_fraud"] == 1]
            .groupby("provider_id")
            .size()
            .reset_index(name="fraud_count")
            .sort_values(
                "fraud_count",
                ascending=False
            )
            .head(10)
        )

        plt.figure(figsize=(12,5))

        sns.barplot(
            data=providers,
            x="provider_id",
            y="fraud_count"
        )

        plt.title(
            "Top Fraudulent Providers"
        )

        plt.xticks(rotation=45)

        return self.save_chart(
            "top_fraud_providers.png"
        )

    # --------------------------------------------------
    # Fraud by Procedure Code
    # --------------------------------------------------

    def fraud_by_procedure(self):

        procedures = (
            self.df[self.df["is_fraud"] == 1]
            .groupby("procedure_code")
            .size()
            .reset_index(name="count")
            .sort_values(
                "count",
                ascending=False
            )
            .head(10)
        )

        plt.figure(figsize=(12,5))

        sns.barplot(
            data=procedures,
            x="procedure_code",
            y="count"
        )

        plt.title(
            "Top Fraudulent Procedures"
        )

        return self.save_chart(
            "fraud_by_procedure.png"
        )

    # --------------------------------------------------
    # Monthly Fraud Trend
    # --------------------------------------------------

    def monthly_fraud_trend(self):

        df = self.df.copy()

        df["claim_date"] = pd.to_datetime(
            df["claim_date"]
        )

        trend = (
            df.groupby(
                pd.Grouper(
                    key="claim_date",
                    freq="ME"
                )
            )["is_fraud"]
            .sum()
            .reset_index()
        )

        plt.figure(figsize=(12,5))

        sns.lineplot(
            data=trend,
            x="claim_date",
            y="is_fraud",
            marker="o"
        )

        plt.title(
            "Monthly Fraud Trend"
        )

        return self.save_chart(
            "monthly_fraud_trend.png"
        )

    # --------------------------------------------------
    # Claim Amount vs Fraud
    # --------------------------------------------------

    def claim_amount_vs_fraud(self):

        plt.figure(figsize=(8,5))

        sns.boxplot(
            data=self.df,
            x="is_fraud",
            y="claim_amount"
        )

        plt.title(
            "Claim Amount vs Fraud"
        )

        return self.save_chart(
            "claim_amount_vs_fraud.png"
        )

    # --------------------------------------------------
    # Correlation Heatmap
    # --------------------------------------------------

    def correlation_heatmap(self):

        numeric_df = (
            self.df.select_dtypes(
                include="number"
            )
        )

        plt.figure(figsize=(14,8))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            fmt=".2f",
            cmap="coolwarm"
        )

        plt.title(
            "Correlation Heatmap"
        )

        return self.save_chart(
            "correlation_heatmap.png"
        )

    # --------------------------------------------------
    # Fraud Risk Distribution
    # --------------------------------------------------

    def fraud_risk_distribution(self):

        if (
            "fraud_risk_score"
            not in self.df.columns
        ):
            return None

        plt.figure(figsize=(10,5))

        sns.histplot(
            self.df["fraud_risk_score"],
            bins=20,
            kde=True
        )

        plt.title(
            "Fraud Risk Score Distribution"
        )

        return self.save_chart(
            "fraud_risk_distribution.png"
        )

    # --------------------------------------------------
    # Age Group Fraud Analysis
    # --------------------------------------------------

    def age_group_fraud(self):

        age_groups = pd.cut(
            self.df["age"],
            bins=[0,18,35,50,65,100],
            labels=[
                "0-18",
                "19-35",
                "36-50",
                "51-65",
                "66+"
            ]
        )

        result = (
            self.df
            .assign(age_group=age_groups)
            .groupby("age_group")
            ["is_fraud"]
            .mean()
            .reset_index()
        )

        plt.figure(figsize=(8,5))

        sns.barplot(
            data=result,
            x="age_group",
            y="is_fraud"
        )

        plt.title(
            "Fraud Rate by Age Group"
        )

        return self.save_chart(
            "age_group_fraud.png"
        )

    # --------------------------------------------------
    # ROC Curve
    # --------------------------------------------------

    def roc_curve_chart(
        self,
        y_test,
        y_pred_prob
    ):

        fpr, tpr, _ = roc_curve(
            y_test,
            y_pred_prob
        )

        roc_auc = auc(
            fpr,
            tpr
        )

        plt.figure(figsize=(8,5))

        plt.plot(
            fpr,
            tpr,
            label=f"AUC={roc_auc:.3f}"
        )

        plt.plot(
            [0,1],
            [0,1],
            linestyle="--"
        )

        plt.title("ROC Curve")

        plt.legend()

        return self.save_chart(
            "roc_curve.png"
        )

    # --------------------------------------------------
    # Precision Recall Curve
    # --------------------------------------------------

    def precision_recall_chart(
        self,
        y_test,
        y_pred_prob
    ):

        precision, recall, _ = (
            precision_recall_curve(
                y_test,
                y_pred_prob
            )
        )

        plt.figure(figsize=(8,5))

        plt.plot(
            recall,
            precision
        )

        plt.title(
            "Precision Recall Curve"
        )

        return self.save_chart(
            "precision_recall_curve.png"
        )

    # --------------------------------------------------
    # Confusion Matrix
    # --------------------------------------------------

    def confusion_matrix_chart(
        self,
        y_test,
        y_pred
    ):

        cm = confusion_matrix(
            y_test,
            y_pred
        )

        plt.figure(figsize=(6,5))

        sns.heatmap(
            cm,
            annot=True,
            fmt="d"
        )

        plt.title(
            "Confusion Matrix"
        )

        return self.save_chart(
            "confusion_matrix.png"
        )

    # --------------------------------------------------
    # Dashboard Charts
    # --------------------------------------------------

    def generate_dashboard_charts(self):

        charts = {

            "fraud_distribution":
                self.fraud_distribution(),

            "claim_amount_distribution":
                self.claim_amount_distribution(),

            "fraud_by_state":
                self.fraud_by_state(),

            "top_fraud_providers":
                self.top_fraud_providers(),

            "fraud_by_procedure":
                self.fraud_by_procedure(),

            "monthly_fraud_trend":
                self.monthly_fraud_trend(),

            "claim_amount_vs_fraud":
                self.claim_amount_vs_fraud(),

            "correlation_heatmap":
                self.correlation_heatmap(),

            "fraud_risk_distribution":
                self.fraud_risk_distribution(),

            "age_group_fraud":
                self.age_group_fraud()

        }

        return charts