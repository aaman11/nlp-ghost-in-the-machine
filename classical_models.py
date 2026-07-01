from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def train_classical_models(df, feature_cols, label_col="label", test_size=0.2, seed=42):
    X = df[feature_cols].fillna(0)
    y = df[label_col]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=seed, stratify=y
    )

    rf = RandomForestClassifier(n_estimators=300, random_state=seed, class_weight="balanced")
    rf.fit(X_train, y_train)
    rf_pred = rf.predict(X_test)

    xgb = XGBClassifier(
        n_estimators=300,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.9,
        colsample_bytree=0.9,
        random_state=seed,
        eval_metric="mlogloss"
    )
    xgb.fit(X_train, y_train)
    xgb_pred = xgb.predict(X_test)

    results = {
        "rf_accuracy": accuracy_score(y_test, rf_pred),
        "xgb_accuracy": accuracy_score(y_test, xgb_pred),
        "rf_report": classification_report(y_test, rf_pred, output_dict=True),
        "xgb_report": classification_report(y_test, xgb_pred, output_dict=True),
        "rf_confusion": confusion_matrix(y_test, rf_pred).tolist(),
        "xgb_confusion": confusion_matrix(y_test, xgb_pred).tolist(),
    }
    return rf, xgb, results, X_test, y_test, rf_pred, xgb_pred
