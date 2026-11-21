## Model Evaluation

ResumeIQ uses a Logistic Regression model with TF-IDF vectorization to classify resume-job matches.

### Evaluation Metrics

| Metric | Score |
|---|---:|
| Accuracy | 0.56 |
| Precision (Macro) | 0.56 |
| Recall (Macro) | 0.56 |
| F1 Score (Macro) | 0.56 |

### Classification Report

The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report
- Confusion Matrix

### Confusion Matrix

A confusion matrix visualization is generated during model training and saved at:

`models/confusion_matrix.png`

### Note

The current dataset contains illustrative sample data. These evaluation scores are preliminary and should not be treated as real-world model performance.