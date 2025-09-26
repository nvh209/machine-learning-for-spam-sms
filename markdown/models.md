# Machine Learning Model Overview

This document explains the steps and results for building and evaluating machine learning models to classify SMS messages as spam or not spam.

## Preprocessing

Preprocessing prepares the data for modeling:

### 1. Data Loading & Selection

- Load `spam_data.csv` using `pandas`.
- Clean column names (remove extra spaces).
- Select relevant columns: `target` (label) and `text` (message).
- Encode labels: replace `ham` with 0 and `spam` with 1.

### 2. Feature Engineering

- Add a `Count` column for message length.
- Use `Porter Stemmer` for word stemming.
- Tokenize messages, remove stopwords, and apply stemming.
- Build a corpus for vectorization.
- Transform corpus into numeric features using `CountVectorizer`.
- Save the vectorizer for future use.

## Data Preparation

- Split data into training and testing sets.
- Encode target labels with `LabelEncoder`.
- Scale features using `StandardScaler`.
- Specify test size for splitting.

## Model Training & Evaluation

Several models were trained and evaluated. Below are the steps and results for each:

### Logistic Regression (LR)

- Pipeline: scaling + logistic regression.
- Hyperparameter tuning with randomized search and stratified k-fold cross-validation.
- Best parameters and cross-validation score reported.
- Training time: 4m 39s.

**Results:**

```txt
Test Accuracy: 0.99
Confusion Matrix:
 [[1928    7]
 [  22  272]]
Classification Report:
               precision    recall  f1-score   support
           0       0.99      1.00      0.99      1935
           1       0.97      0.93      0.95       294
    accuracy                           0.99      2229
   macro avg       0.98      0.96      0.97      2229
weighted avg       0.99      0.99      0.99      2229
```

### Gaussian Naive Bayes (NB)

- Initialize and train Gaussian Naive Bayes classifier.
- Predict on test set.
- Training time: 45s.

**Results:**

```txt
Test Accuracy: 0.89
Confusion Matrix:
 [[1711  224]
 [  30  264]]
Classification Report:
               precision    recall  f1-score   support
           0       0.98      0.88      0.93      1935
           1       0.54      0.90      0.68       294
    accuracy                           0.89      2229
   macro avg       0.76      0.89      0.80      2229
weighted avg       0.92      0.89      0.90      2229
```

### Random Forest (RF)

- Initialize Random Forest classifier.
- Hyperparameter tuning with grid search.
- Best parameters and cross-validation score reported.
- Training time: 4m 23s.

**Results:**

```txt
Test Accuracy: 0.89
Confusion Matrix:
 [[1711  224]
 [  30  264]]
Classification Report:
               precision    recall  f1-score   support
           0       0.98      0.88      0.93      1935
           1       0.54      0.90      0.68       294
    accuracy                           0.89      2229
   macro avg       0.76      0.89      0.80      2229
weighted avg       0.92      0.89      0.90      2229
```

### Support Vector Machine (SVM)

- Pipeline: scaling + SVM classifier.
- Hyperparameter tuning with grid search.
- Best parameters and cross-validation score reported.
- Training time: 9m 28s.

**Results:**

```txt
Test Accuracy: 0.89
Confusion Matrix:
 [[1711  224]
 [  30  264]]
Classification Report:
               precision    recall  f1-score   support
           0       0.98      0.88      0.93      1935
           1       0.54      0.90      0.68       294
    accuracy                           0.89      2229
   macro avg       0.76      0.89      0.80      2229
weighted avg       0.92      0.89      0.90      2229
```

---

**Summary:**  

Logistic Regression achieved the highest accuracy (0.99) and best overall performance. Other models performed similarly, with slightly lower accuracy and recall for the spam class.
