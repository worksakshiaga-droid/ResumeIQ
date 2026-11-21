

import os
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Load dataset
data = pd.read_csv("data/resume_job_data.csv")

# Prepare input text
data["combined_text"] = (
    "resume " + data["resume"].fillna("") +
    " job " + data["job_description"].fillna("")
)

X = data["combined_text"]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Model Evaluation
print("\n===== RESUMEIQ MODEL EVALUATION =====")

print("Accuracy:", round(
    accuracy_score(y_test, predictions), 2
))

print("Precision:", round(
    precision_score(
        y_test, predictions,
        average="macro",
        zero_division=0
    ), 2
))

print("Recall:", round(
    recall_score(
        y_test, predictions,
        average="macro",
        zero_division=0
    ), 2
))

print("F1 Score:", round(
    f1_score(
        y_test, predictions,
        average="macro",
        zero_division=0
    ), 2
))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

# Confusion Matrix
cm = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

print("\nConfusion Matrix:")
print(cm)

# Create confusion matrix image
os.makedirs("models", exist_ok=True)

display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)

display.plot(cmap="Purples")

plt.title("ResumeIQ - Confusion Matrix")
plt.tight_layout()

image_path = os.path.abspath(
    "models/confusion_matrix.png"
)

plt.savefig(image_path, dpi=150)
plt.close()

print("\nIMAGE PATH:", image_path)
print("FILE EXISTS:", os.path.exists(image_path))

# Save trained model
joblib.dump(
    model,
    "models/resume_match_model.pkl"
)

print("\nModel saved successfully!")
print("Confusion Matrix saved successfully!")
