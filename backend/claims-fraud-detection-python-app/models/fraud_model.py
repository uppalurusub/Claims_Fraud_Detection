import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    IsolationForest
)

from sklearn.linear_model import LogisticRegression

from xgboost import XGBClassifier


class FraudDetectionModel:

    def __init__(self, df):

        self.df = df

        self.model = None

        self.X_train = None
        self.X_test = None

        self.y_train = None
        self.y_test = None

    # --------------------------------------------------
    # Prepare Dataset
    # --------------------------------------------------

    def prepare_data(self):

        target = "is_fraud"

        drop_cols = []

        for col in [

            "claim_id",
            "claim_date",
            "risk_category"

        ]:

            if col in self.df.columns:
                drop_cols.append(col)

        model_df = self.df.drop(
            columns=drop_cols,
            errors="ignore"
        )

        X = model_df.drop(
            columns=[target]
        )

        y = model_df[target]

        self.X_train, self.X_test, \
        self.y_train, self.y_test = train_test_split(

            X,
            y,

            test_size=0.20,

            random_state=42,

            stratify=y
        )

        return X, y

    # --------------------------------------------------
    # Logistic Regression
    # --------------------------------------------------

    def train_logistic_regression(self):

        self.model = LogisticRegression(
            max_iter=1000
        )

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # --------------------------------------------------
    # Random Forest
    # --------------------------------------------------

    def train_random_forest(self):

        self.model = RandomForestClassifier(

            n_estimators=200,

            max_depth=10,

            random_state=42,

            n_jobs=-1
        )

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # --------------------------------------------------
    # Gradient Boosting
    # --------------------------------------------------

    def train_gradient_boosting(self):

        self.model = GradientBoostingClassifier(

            n_estimators=200,

            random_state=42
        )

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # --------------------------------------------------
    # XGBoost
    # --------------------------------------------------

    def train_xgboost(self):

        self.model = XGBClassifier(

            n_estimators=300,

            max_depth=6,

            learning_rate=0.05,

            subsample=0.8,

            colsample_bytree=0.8,

            eval_metric="logloss",

            random_state=42
        )

        self.model.fit(
            self.X_train,
            self.y_train
        )

        return self.model

    # --------------------------------------------------
    # Evaluate Model
    # --------------------------------------------------

    def evaluate(self):

        y_pred = self.model.predict(
            self.X_test
        )

        y_prob = self.model.predict_proba(
            self.X_test
        )[:, 1]

        return {

            "accuracy":
                round(
                    accuracy_score(
                        self.y_test,
                        y_pred
                    ),
                    4
                ),

            "precision":
                round(
                    precision_score(
                        self.y_test,
                        y_pred
                    ),
                    4
                ),

            "recall":
                round(
                    recall_score(
                        self.y_test,
                        y_pred
                    ),
                    4
                ),

            "f1_score":
                round(
                    f1_score(
                        self.y_test,
                        y_pred
                    ),
                    4
                ),

            "roc_auc":
                round(
                    roc_auc_score(
                        self.y_test,
                        y_prob
                    ),
                    4
                ),

            "confusion_matrix":
                confusion_matrix(
                    self.y_test,
                    y_pred
                ).tolist(),

            "classification_report":
                classification_report(
                    self.y_test,
                    y_pred,
                    output_dict=True
                )
        }

    # --------------------------------------------------
    # Feature Importance
    # --------------------------------------------------

    def feature_importance(self):

        if not hasattr(
            self.model,
            "feature_importances_"
        ):
            return []

        importance = pd.DataFrame({

            "feature":
                self.X_train.columns,

            "importance":
                self.model.feature_importances_

        })

        importance = importance.sort_values(
            by="importance",
            ascending=False
        )

        return (
            importance.head(20)
            .to_dict(
                orient="records"
            )
        )

    # --------------------------------------------------
    # Predict Fraud
    # --------------------------------------------------

    def predict(self, X):

        prediction = self.model.predict(X)

        probability = (
            self.model.predict_proba(X)
            [:, 1]
        )

        return {

            "prediction":
                prediction.tolist(),

            "fraud_probability":
                probability.tolist()
        }

    # --------------------------------------------------
    # Fraud Risk Score
    # --------------------------------------------------

    def fraud_risk_score(self, X):

        prob = (
            self.model.predict_proba(X)
            [:, 1]
        )

        score = np.round(
            prob * 100,
            0
        )

        risk = []

        for s in score:

            if s <= 30:
                risk.append("Low")

            elif s <= 70:
                risk.append("Medium")

            else:
                risk.append("High")

        return {

            "fraud_score":
                score.tolist(),

            "risk_category":
                risk
        }

    # --------------------------------------------------
    # Save Model
    # --------------------------------------------------

    def save_model(
        self,
        filepath="models/fraud_model.pkl"
    ):

        joblib.dump(
            self.model,
            filepath
        )

        return filepath

    # --------------------------------------------------
    # Load Model
    # --------------------------------------------------

    @staticmethod
    def load_model(filepath):

        return joblib.load(filepath)

    # --------------------------------------------------
    # Isolation Forest
    # --------------------------------------------------

    def anomaly_detection(self):

        model = IsolationForest(

            contamination=0.05,

            random_state=42
        )

        predictions = model.fit_predict(

            self.X_train
        )

        return {

            "normal_claims":
                int(
                    (predictions == 1).sum()
                ),

            "anomalies":
                int(
                    (predictions == -1).sum()
                )
        }

    # --------------------------------------------------
    # Train Best Model
    # --------------------------------------------------

    def train_best_model(self):

        self.prepare_data()

        self.train_xgboost()

        metrics = self.evaluate()

        return {

            "metrics": metrics,

            "feature_importance":
                self.feature_importance()
        }