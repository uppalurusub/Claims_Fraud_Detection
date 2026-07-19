import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler


class ClaimsPreprocessor:

    def __init__(self, filepath):

        self.filepath = filepath

        self.df = pd.read_csv(filepath)

        self.label_encoders = {}

        #self.scaler = StandardScaler()

    # --------------------------------------------------
    # Load Data
    # --------------------------------------------------

    def load_data(self):

        return self.df

    # --------------------------------------------------
    # Basic Cleaning
    # --------------------------------------------------

    def clean_data(self):

        # Remove duplicates

        self.df.drop_duplicates(inplace=True)

        # Standardize column names

        self.df.columns = (
            self.df.columns
            .str.lower()
            .str.strip()
            .str.replace(" ", "_")
        )

        return self.df

    # --------------------------------------------------
    # Handle Missing Values
    # --------------------------------------------------

    def handle_missing_values(self):

        numeric_cols = self.df.select_dtypes(
            include=np.number
        ).columns

        categorical_cols = self.df.select_dtypes(
            exclude=np.number
        ).columns

        for col in numeric_cols:

            self.df[col].fillna(
                self.df[col].median()
            )

        for col in categorical_cols:

            self.df[col].fillna(
                self.df[col].mode()[0]
            )

        return self.df

    # --------------------------------------------------
    # Date Features
    # --------------------------------------------------

    def create_date_features(self):

        self.df["claim_date"] = pd.to_datetime(
            self.df["claim_date"]
        )

        self.df["claim_year"] = (
            self.df["claim_date"].dt.year
        )

        self.df["claim_month"] = (
            self.df["claim_date"].dt.month
        )

        self.df["claim_day"] = (
            self.df["claim_date"].dt.day
        )

        self.df["claim_weekday"] = (
            self.df["claim_date"].dt.day_name()
        )

        self.df["claim_quarter"] = (
            self.df["claim_date"].dt.quarter
        )

        return self.df

    # --------------------------------------------------
    # Fraud Features
    # --------------------------------------------------

    def create_fraud_features(self):

        self.df["high_claim_flag"] = np.where(
            self.df["claim_amount"] > 25000,
            1,
            0
        )

        self.df["many_prior_claims_flag"] = np.where(
            self.df["prior_claims"] > 15,
            1,
            0
        )

        self.df["many_procedures_flag"] = np.where(
            self.df["num_procedures"] > 5,
            1,
            0
        )

        self.df["hospitalization_risk"] = np.where(
            self.df["days_hospitalized"] > 10,
            1,
            0
        )

        return self.df

    # --------------------------------------------------
    # Provider Features
    # --------------------------------------------------

    def create_provider_features(self):

        provider_claims = (
            self.df.groupby("provider_id")
            .size()
            .reset_index(name="provider_claim_count")
        )

        self.df = self.df.merge(
            provider_claims,
            on="provider_id",
            how="left"
        )

        return self.df

    # --------------------------------------------------
    # Outlier Capping
    # --------------------------------------------------

    def cap_outliers(
        self,
        columns
    ):

        for col in columns:

            q1 = self.df[col].quantile(0.25)

            q3 = self.df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - (1.5 * iqr)

            upper = q3 + (1.5 * iqr)

            self.df[col] = np.clip(
                self.df[col],
                lower,
                upper
            )

        return self.df

    # --------------------------------------------------
    # Label Encoding
    # --------------------------------------------------

    def encode_categorical_columns(self):

        categorical_cols = [

            "gender",
            "state",
            "provider_id",
            "patient_id",
            "procedure_code",
            "diagnosis_code",
            "claim_weekday"

        ]

        for col in categorical_cols:

            if col in self.df.columns:

                le = LabelEncoder()

                self.df[col] = le.fit_transform(
                    self.df[col]
                )

                self.label_encoders[col] = le

        return self.df

    # --------------------------------------------------
    # Scaling
    # --------------------------------------------------

    def scale_features(self):

        scale_cols = [

            "claim_amount",
            "age",
            "days_hospitalized",
            "num_procedures",
            "prior_claims",
            "provider_claim_count"

        ]

        existing_cols = [
            col for col in scale_cols
            if col in self.df.columns
        ]

        self.df[existing_cols] = (
            self.scaler.fit_transform(
                self.df[existing_cols]
            )
        )

        return self.df

    # --------------------------------------------------
    # Final Dataset
    # --------------------------------------------------

    def get_model_dataset(self):

        drop_cols = [

            "claim_id"
            

        ]

        drop_cols = [
            col for col in drop_cols
            if col in self.df.columns
        ]

        return self.df.drop(
            columns=drop_cols
        )

    # --------------------------------------------------
    # Full Pipeline
    # --------------------------------------------------

    def process(self):

        self.clean_data()

        self.handle_missing_values()

        self.create_date_features()

        self.create_fraud_features()

        self.create_provider_features()

        self.cap_outliers([
            "claim_amount",
            "prior_claims"
        ])

        self.encode_categorical_columns()

        #self.scale_features()

        return self.get_model_dataset()